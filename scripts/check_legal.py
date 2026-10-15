"""Verify legal navigation and, optionally, parity with the Android source.
Run: python scripts/check_legal.py --app PATH_TO_FLUTTER_REPOSITORY
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,re

class Text(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.parts=[]; self.feed(source)
    def handle_data(self, data): self.parts.append(data)

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--app',type=Path);args=parser.parse_args()
for page in (root/'site').glob('*.html'):
    source=page.read_text(encoding='utf-8')
    footer=source.split('<footer>',1)[1]
    for link in ['terms.html','privacy.html']:
        assert f'href="{link}"' in footer, f'{page.name}: missing footer link {link}'
    text=' '.join(Text(source).parts).lower()
    for obsolete in ['independent backup alarm','supplementary reminders','consumer rights act 2022','governed by irish law']:
        assert obsolete not in text, f'{page.name}: outdated notice: {obsolete}'
if args.app:
    dart=(args.app/'lib/legal/shift_plus_legal_text.dart').read_text(encoding='utf-8')
    for constant,page in [('termsOfUse','terms.html'),('privacyInformation','privacy.html')]:
        value=re.search(rf"{constant}\s*=\s*'''(.*?)''';",dart,re.S).group(1)
        source=(root/'site'/page).read_text(encoding='utf-8')
        web=' '.join(''.join(Text(source).parts).split())
        for paragraph in value.strip().split('\n\n')[1:]:
            for line in paragraph.splitlines():
                assert ' '.join(line.split()) in web, f'{page}: app/website difference: {line}'
    version=re.search(r"workAlarmTermsVersion = '(.*?)'",dart).group(1)
    assert version in (root/'site/terms.html').read_text(encoding='utf-8')
print('PASS: legal/footer links, retired wording and requested app/website parity')
