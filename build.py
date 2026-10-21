# coloring.html(아티팩트용 본문) → index.html(어디서나 열리는 완성 페이지 · 깃허브 페이지용)
from pathlib import Path
body=Path('coloring.html').read_text(encoding='utf-8')
head=('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="theme-color" content="#dff3f6">'
      '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192.png"><link rel="icon" href="icon-192.png">'
      '<style>[hidden]{display:none!important}html,body{margin:0}:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}</style>'
      '</head><body>\n')
sw='<script>if("serviceWorker" in navigator)navigator.serviceWorker.register("sw.js").catch(()=>{})</script>'
Path('index.html').write_text(head+body+'\n'+sw+'\n</body></html>\n',encoding='utf-8'); print('index.html 만듦')
