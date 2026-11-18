'use strict';
// Compatibility only: the supplied design and content do not require JavaScript.
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
const fragmentAliases = {"ostra": {"section-1": "s1", "section-2": "s2", "section-3": "s3", "section-4": "s4"}, "balance": {"section-1": "s1", "section-2": "s2", "section-3": "s3", "section-4": "s4"}, "butterfly": {"section-1": "s1", "section-2": "s2", "section-3": "s3", "section-4": "s4", "section-5": "s5"}, "alter": {"section-01": "s1", "section-02": "s2", "section-03": "s3", "section-04": "s4"}, "straight-story": {"section-01": "s1", "section-02": "s2", "section-03": "s3"}, "laurel-poolside-terrace": {"process-01": "s1", "process-02": "s2", "process-03": "s3", "process-04": "s4"}, "laurel-layered-arrival": {"process-01": "s1", "process-02": "s2", "process-03": "s3"}, "laurel-garden": {"process-01": "s1", "process-02": "s2", "process-03": "s3"}, "laurel-pergola": {"process-01": "s1", "process-02": "s2", "process-03": "s3"}, "laurel-entry": {"process-01": "s1", "process-02": "s2", "process-03": "s3"}, "bare": {"section-1": "project-intro", "section-2": "s1", "section-3": "s2", "section-4": "s3", "section-5": "s4"}, "nucite": {"final-direction": "s5"}};
function followLegacySection() {
  let fragment;
  try { fragment = decodeURIComponent(location.hash.slice(1)); } catch { return; }
  if (!fragment || document.getElementById(fragment)) return;
  const targetId = (fragmentAliases[document.body.dataset.page] || {})[fragment];
  if (targetId) document.getElementById(targetId)?.scrollIntoView();
}
window.addEventListener('load', followLegacySection);
window.addEventListener('hashchange', followLegacySection);
