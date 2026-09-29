'use strict';
document.querySelectorAll('[data-configuration]').forEach((group) => {
  const buttons = group.querySelectorAll('button[data-view]');
  const pictures = group.querySelectorAll('[data-panel]');
  buttons.forEach((button) => button.addEventListener('click', () => {
    buttons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    pictures.forEach((picture) => { picture.hidden = picture.dataset.panel !== button.dataset.view; });
  }));
});
