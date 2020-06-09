const CACHE_NAME = 'version-1';
const urlsToCache = ['index.html', 'offline.html'];

const self  = this;

// INSTALL SW
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then((cache) => {
            console.log('Opened cache');

            return cache.addAll(urlsToCache);
        })
    );
});

// LISTEN FOR REQUEST
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
        .then(() =>{
            return fetch(event.request)
                .catch(() => caches.match('offline.html'))
        })
    )
});

// ACTIVATE THE SW
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [];
    cacheWhitelist.push(CACHE_NAME);

    caches.keys().then((cacheName) => Promise.all(
        cacheName.map((cacheName) => {
            if(!cacheWhitelist.includes(cacheName)){
                return caches.delete(cacheName);
            }
        })
    ))
});