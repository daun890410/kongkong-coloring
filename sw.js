// 앱은 저장해 둔 것으로 바로 연다. 앱 본체(html · json)는 뒤에서 새로 받아 두었다가 다음에 열 때 쓴다 (기다리지 않음).
// 그림 · 소리 · 목소리 · 글꼴은 한 번 받으면 저장본을 쓴다. 판 번호(V)는 build.py 가 올릴 때마다 바꾼다 → 새 판이 깔리면서 본체를 미리 받아 둔다.
const V='kk-20261022182932';
const CORE=['./','index.html','tales/tales.json','tales/cats.json','manifest.webmanifest','icon-192-v2.png'];
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(V).then(c=>c.addAll(CORE.map(u=>new Request(u,{cache:'reload'})))).catch(()=>{}))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
function put(r,res){if(res&&(res.ok||res.type==='opaque')){const c=res.clone();caches.open(V).then(x=>x.put(r,c))}return res}
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
  const font=/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname);if(!font&&u.origin!==location.origin)return;
  const core=!font&&/\/$|\.html$|\.json$|\.webmanifest$/.test(u.pathname);
  e.respondWith(caches.match(r,{ignoreSearch:core}).then(m=>{
    const net=fetch(r).then(res=>put(r,res)).catch(()=>m);
    if(m){if(core)e.waitUntil(net);return m}   // 저장본 바로 · 본체는 뒤에서 새로
    return net}))});
