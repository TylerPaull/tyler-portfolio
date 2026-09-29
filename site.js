'use strict';
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
