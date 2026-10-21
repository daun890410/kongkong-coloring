// 한 번 받은 그림 · 소리 · 목소리는 기기에 저장해 두고 먼저 꺼내 쓴다. 앱 본체(index.html · 목록)는 새 것이 있으면 새 것으로.
const V='kk-20261022072649';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(V).then(c=>c.addAll(['./','index.html','tales/tales.json','tales/cats.json','manifest.webmanifest']).catch(()=>{})))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
  if(/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)){e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{const c=res.clone();caches.open(V).then(x=>x.put(r,c));return res})));return}
  if(u.origin!==location.origin)return;
  const fresh=/\/$|\.html$|\.json$|\.webmanifest$/.test(new URL(r.url).pathname);
  if(fresh){e.respondWith(fetch(r).then(res=>{const c=res.clone();caches.open(V).then(x=>x.put(r,c));return res}).catch(()=>caches.match(r)));return}
  e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{if(res.ok&&res.status===200){const c=res.clone();caches.open(V).then(x=>x.put(r,c))}return res})))});
