'use strict';
// Keep folder pages canonical while supporting direct local-file previews.
if (location.protocol === 'http:' || location.protocol === 'https:') {
  if (location.pathname.endsWith('/index.html')) {
    history.replaceState(history.state, '', location.pathname.slice(0, -10) + location.search + location.hash);
  }
} else if (location.protocol === 'file:') {
  document.querySelectorAll('a[href]').forEach((link) => {
    const target = new URL(link.getAttribute('href'), document.baseURI);
    if (target.protocol === 'file:' && target.pathname.endsWith('/')) {
      target.pathname += 'index.html';
      link.href = target.href;
    }
  });
}
// With JavaScript disabled, both seating photographs remain visible.
document.querySelectorAll('[data-configuration]').forEach((group) => {
  const controls = group.querySelector('.toggle');
  const buttons = group.querySelectorAll('button[data-view]');
  const pictures = group.querySelectorAll('[data-panel]');
  const select = (button) => {
    buttons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    pictures.forEach((picture) => { picture.hidden = picture.dataset.panel !== button.dataset.view; });
  };
  controls.hidden = false;
  select(buttons[0]);
  buttons.forEach((button) => button.addEventListener('click', () => select(button)));
});
