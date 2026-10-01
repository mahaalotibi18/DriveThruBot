/* =====================================================================
   قبطان — العامل الخدمي (Service Worker)
   يخزّن واجهة التطبيق والخطوط عشان يشتغل بدون إنترنت.
   عند تحديث أي ملف: غيّري رقم VERSION حتى تتحدث النسخة المخزنة.
   ===================================================================== */
const VERSION = 'qaptan-v1.0.0';
const SHELL_CACHE = VERSION + '-shell';
const FONT_CACHE = 'qaptan-fonts-v1';
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon.svg',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
];

/* التثبيت: تخزين ملفات الواجهة */
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then((c) => c.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

/* التفعيل: حذف النسخ القديمة */
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== SHELL_CACHE && k !== FONT_CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* عرض النسخة المخزنة فوراً وتحديثها في الخلفية */
async function staleWhileRevalidate(request, cacheName, cacheKey) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(cacheKey || request, { ignoreSearch: true });
  const network = fetch(request)
    .then((res) => {
      if (res && (res.ok || res.type === 'opaque')) cache.put(cacheKey || request, res.clone()).catch(() => {});
      return res;
    })
    .catch(() => null);
  if (cached) return cached;
  const res = await network;
  if (res) return res;
  return new Response('', { status: 504, statusText: 'offline' });
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // الخطوط من Google Fonts
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    event.respondWith(staleWhileRevalidate(req, FONT_CACHE));
    return;
  }
  if (url.origin !== self.location.origin) return;

  // التنقل: الصفحة الرئيسية دائماً من الذاكرة
  if (req.mode === 'navigate') {
    event.respondWith(staleWhileRevalidate(req, SHELL_CACHE, './index.html'));
    return;
  }
  event.respondWith(staleWhileRevalidate(req, SHELL_CACHE));
});
