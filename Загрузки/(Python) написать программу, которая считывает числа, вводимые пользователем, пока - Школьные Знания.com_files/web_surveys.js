var _sTrackingAlreadyPresent = (typeof window._svd !== 'undefined' && typeof window._svc !== 'undefined');var _svc = window._svc || {};var _svd = window._svd || {};_svc.workspaceKey = _svc.workspaceKey || 'bkjxjKXBEOcOEcsHnhqzZcNwGRyXjvkT';_svd.flags = _svd.flags || {"async_consumers":true};_svd.surveys = _svd.surveys || [];_svd.themes = _svd.themes || [];_svd.permissions = _svd.permissions || {"targeting_javascript_api":false};_svd.audiences = _svd.audiences || [];_svd.integrations = _svd.integrations || [];_svd.installing = _svd.installing || false;_svd.translations = _svd.translations || null;// Generated at: 2022\u002D08\u002D04\u002011\u003A22\u003A56
(function () {
  if (_sTrackingAlreadyPresent) {
    return;
  }

  if (document && document.head) {
    var linkElement = document.createElement('link');
    linkElement.href = 'https\u003A\/\/surveys\u002Dstatic.survicate.com/fonts/fonts.css';
    linkElement.rel = 'stylesheet';
    linkElement.type = 'text/css';
    document.head.appendChild(linkElement);
  }

  var isIE = window.navigator.userAgent.indexOf('MSIE') !== -1 || window.navigator.userAgent.match(/Trident.*rv\:11\./);
  var isSafari = window.navigator.vendor && window.navigator.vendor.indexOf('Apple') > -1 && window.navigator.userAgent && window.navigator.userAgent.indexOf('CriOS') == -1 && window.navigator.userAgent.indexOf('FxiOS') == -1;

  var isOldSafari = false;
  if (isSafari && window.navigator.userAgent) {
    var match = window.navigator.userAgent.match(/Version.([0-9]+)\./);
    if (match && match.length === 2) {
      if (parseInt(match[1]) < 11) {
        isOldSafari = true;
      }
    }
  }
  var isOldEdge = window.navigator.userAgent.match(/Edge\/(15\.15|18\.18)/);

  var coreUrls = [''];
  var e = document.getElementsByTagName('script')[0];

  if (isIE || isOldSafari || isOldEdge) {
    coreUrls = coreUrls.map(function (url) {
      if (url.indexOf('preview') !== -1) {
        return url.replace(/preview-/, 'preview_babel-');
      }
      return url.replace(/core-/, 'core_babel-');
    })
  }

  for (var i = 0; i < coreUrls.length; i++) {
    var s = document.createElement('script');
    s.setAttribute('crossorigin', 'anonymous');
    s.src = coreUrls[i];
    s.async = true;
    e.parentNode.insertBefore(s, e);
  }
})();
