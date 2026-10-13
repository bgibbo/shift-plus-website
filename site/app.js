const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
function closeMenu() { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); }
menu.addEventListener('click', () => { const open = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(open)); });
nav.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); menu.focus(); } });
const tours = {
  calendar: ['Calendar with shift colours, alarm markers and other units', 'E, L, N and R identify shift types. Tap a date in the app to compare units; long-press to open the complete day preview.'],
  alarms: ['Work Alarms settings showing Book On and Book Off timing', 'Open Settings → Work Alarms. Enable the start and finish alarms you want, adjust their timing and run the 10-second Test Alarm on your phone.'],
  'alarm-centre': ['Alarm Centre showing active and silenced upcoming alarms', 'Open Alarm Centre using the bell on the calendar. Review upcoming Book On and Book Off alarms. The genuine capture shows both active and silenced entries.']
};
document.querySelectorAll('[data-tour]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-tour]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  const key = button.dataset.tour;
  const target = document.querySelector('.tour-visual .screenshot');
  target.dataset.enlarge = `assets/${key}.webp`;
  target.setAttribute('aria-label', `Enlarge ${tours[key][0]}`);
  target.querySelector('img').src = target.dataset.enlarge;
  target.querySelector('img').alt = tours[key][0];
  document.querySelector('#tour-description').textContent = tours[key][1];
}));
const viewer = document.querySelector('#image-viewer');
document.querySelectorAll('[data-enlarge]').forEach(button => button.addEventListener('click', () => {
  viewer.querySelector('img').src = button.dataset.enlarge;
  viewer.querySelector('img').alt = button.querySelector('img').alt;
  viewer.showModal();
}));
viewer.querySelector('button').addEventListener('click', () => viewer.close());
viewer.addEventListener('click', event => { if (event.target === viewer) viewer.close(); });
const search = document.querySelector('#faq-search');
if (search) {
  const filter = () => {
    const query = search.value.toLowerCase().trim(); let count = 0;
    document.querySelectorAll('.faq-list details').forEach(item => { item.hidden = !item.textContent.toLowerCase().includes(query); if (!item.hidden) count++; });
    document.querySelector('#faq-count').textContent = `${count} ${count === 1 ? 'answer' : 'answers'} found`;
    document.querySelector('#no-results').hidden = count !== 0;
  };
  search.addEventListener('input', filter); filter();
}
