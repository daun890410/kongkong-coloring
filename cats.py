# 마음대로 색칠 카테고리 — 하나의 원본. python cats.py → tales/cats.json (앱) · 빠진 그림 요청(--요청)
import json, sys
from pathlib import Path
CATS = [
 ("animal","동물","🐶",[("f01","사자",None),("f02","아기 코끼리",None),("f03","기린",None),("f04","펭귄",None),("f05","강아지",None),("f06","아기 고양이",None),("f07","곰돌이",None),
   ("a01","토끼","a cute bunny sitting with a carrot"),("a02","판다","a cute baby panda eating bamboo"),("a03","원숭이","a cute monkey holding a banana"),("a04","돼지","a cute round piglet in mud puddle")]),
 ("dino","공룡","🦖",[("f16","아기 공룡",None),("d01","티라노","a cute friendly baby tyrannosaurus rex smiling"),("d02","트리케라톱스","a cute triceratops with three horns"),
   ("d03","브라키오사우루스","a cute long-neck brachiosaurus eating leaves from a tree"),("d04","스테고사우루스","a cute stegosaurus with big back plates"),
   ("d05","프테라노돈","a cute pteranodon flying over a volcano"),("d06","안킬로사우루스","a cute ankylosaurus with a club tail"),("d07","공룡알","three big dinosaur eggs in a nest, one cracking open")]),
 ("car","자동차","🚗",[("f08","소방차",None),("f09","기차",None),("f10","비행기",None),("f11","돛단배",None),("f12","포크레인",None),
   ("c01","경찰차","a cute police car with a siren light"),("c02","버스","a cute school bus with big windows"),("c03","구급차","a cute ambulance"),
   ("c04","트럭","a cute dump truck carrying rocks"),("c05","헬리콥터","a cute helicopter with big rotor"),("c06","자전거","a child's bicycle with a basket")]),
 ("build","건물","🏠",[("b01","우리 집","a cozy house with a door, two windows, chimney and a fence"),("b02","성","a fairy tale castle with towers and flags"),
   ("b03","학교","a small school building with a clock and a flag"),("b04","병원","a small hospital building with a cross sign"),("b05","소방서","a fire station with a big garage door"),
   ("b06","등대","a lighthouse on rocks by the sea"),("b07","한옥","a traditional Korean hanok house with a curved tiled roof"),("b08","풍차","a windmill on a hill with flowers")]),
 ("sea","바다","🐟",[("o01","물고기","two cute fish with big fins and bubbles"),("o02","고래","a cute whale spouting water"),("o03","문어","a cute smiling octopus"),
   ("o04","거북이","a cute sea turtle swimming"),("o05","상어","a cute friendly smiling shark, not scary"),("o06","해마","a cute seahorse"),
   ("o07","불가사리","a starfish and seashells on the sand"),("o08","게","a cute crab with big claws")]),
 ("sword","칼","⚔️",[("w01","해적 칼","a toy pirate sword made of plastic with a round guard, next to a pirate hat"),("w02","기사 칼과 방패","a wooden toy knight sword and a round shield with a star"),
   ("w03","반짝 장난감 칼","a toy sword with stars and a heart on the handle, sparkles"),("w04","닌자 장난감 칼","a toy ninja sword and a ninja headband, cartoon"),
   ("w05","왕자의 칼","a toy prince sword with a crown and a jewel on the handle")]),
 ("gun","총","🔫",[("g01","물총","a toy water gun squirting water drops"),("g02","비눗방울 총","a toy bubble gun making many soap bubbles"),
   ("g03","우주 광선총","a toy space ray gun with rings and a star, cartoon"),("g04","스펀지 다트 총","a toy foam dart blaster with three soft darts"),
   ("g05","꽃 나오는 총","a toy gun with a flower popping out of the barrel, funny")]),
 ("food","음식","🍙",[("f15","딸기",None),("n01","김밥","a plate of Korean gimbap rolls cut into slices"),("n02","피자","a whole pizza with slices and toppings"),
   ("n03","햄버거","a big hamburger with cheese and lettuce"),("n04","주먹밥","two Korean rice balls with seaweed and a cute face"),("n05","떡볶이","a bowl of Korean tteokbokki rice cakes"),
   ("n06","과일 바구니","a basket of apples, bananas, grapes and oranges"),("n07","채소","a carrot, a broccoli, a corn and a tomato")]),
 ("dessert","디저트","🍰",[("f13","생일 케이크",None),("f14","아이스크림",None),("e01","도넛","two donuts with sprinkles"),("e02","컵케이크","a cupcake with cream and a cherry"),
   ("e03","막대사탕","three swirl lollipops"),("e04","쿠키","a plate of cookies with chocolate chips"),("e05","마카롱","a stack of macarons"),
   ("e06","붕어빵","two Korean fish-shaped bungeoppang pastries"),("e07","팥빙수","a bowl of Korean bingsu shaved ice with fruit on top")]),
 ("clean","청소도구","🧹",[("h01","빗자루","a broom and a dustpan with a smile"),("h02","청소기","a cute vacuum cleaner"),("h03","대걸레","a mop and a bucket with bubbles"),
   ("h04","세탁기","a cute washing machine with clothes"),("h05","먼지떨이","a feather duster and a spray bottle"),("h06","스펀지","a sponge, a soap bar and bubbles"),
   ("h07","분리수거","three recycling bins for paper, plastic and cans"),("h08","고무장갑","a pair of rubber gloves and a cleaning bucket")]),
 ("city","도시","🏙️",[("y01","빌딩","a city with tall buildings and windows"),("y02","신호등","a traffic light and a crosswalk with a car"),("y03","놀이터","a playground with a slide and swings"),
   ("y04","공원","a park with a bench, trees and a fountain"),("y05","기차역","a train station with a train arriving"),("y06","마트","a supermarket shop front with a shopping cart"),
   ("y07","놀이공원","an amusement park ferris wheel and a carousel"),("y08","도로","a road with cars, a bus and a tunnel")]),
 ("country","나라","🗼",[("r01","한국 경복궁","the Gyeongbokgung palace gate in Seoul Korea"),("r02","프랑스 에펠탑","the Eiffel Tower in Paris with trees"),
   ("r03","이집트 피라미드","the Egyptian pyramids and a camel"),("r04","미국 자유의 여신상","the Statue of Liberty holding a torch"),
   ("r05","영국 빅벤","the Big Ben clock tower in London with a red bus"),("r06","일본 후지산","Mount Fuji with a cherry blossom tree"),
   ("r07","이탈리아 피사의 탑","the Leaning Tower of Pisa"),("r08","중국 만리장성","the Great Wall of China on mountains")]),
 ("flag","국기","🏳️",[("x01","대한민국",None),("x02","일본",None),("x03","미국",None),("x04","영국",None),("x05","프랑스",None),("x06","이탈리아",None),
   ("x07","독일",None),("x08","스위스",None),("x09","스웨덴",None),("x10","그리스",None)]),
]
FLAG_TIP={"x01":"흰 바탕, 가운데 빨강과 파랑 태극, 네 귀퉁이 검은 괘","x02":"흰 바탕에 빨간 동그라미","x03":"빨강 흰 줄무늬, 왼쪽 위 파랑에 흰 별",
 "x04":"파랑 바탕에 흰 줄과 빨간 십자","x05":"파랑 · 흰 · 빨강 세로 줄","x06":"초록 · 흰 · 빨강 세로 줄","x07":"검정 · 빨강 · 노랑 가로 줄",
 "x08":"빨강 바탕에 흰 십자","x09":"파랑 바탕에 노란 십자","x10":"파랑 흰 줄무늬, 왼쪽 위 파랑에 흰 십자"}
if __name__=="__main__":
    out={"cats":[{"id":c,"name":n,"emoji":e,"items":[[i,nm] for i,nm,_ in it]} for c,n,e,it in CATS],"flagTip":FLAG_TIP}
    Path("tales/cats.json").write_text(json.dumps(out,ensure_ascii=False,indent=0),encoding="utf-8")
    new=[(i,p) for c,n,e,it in CATS for i,nm,p in it if p and not Path(f"img/{i}.png").exists()]
    print("카테고리",len(CATS),"· 그림",sum(len(x[3]) for x in CATS),"· 새로 뽑을 것",len(new))
    if "--요청" in sys.argv and new:
        sys.path.insert(0,"C:/Users/momop/dev/aiClaude/auto"); import 이미지자동출력툴 as t
        B=("Simple coloring page for a 3-year-old. EXTRA THICK bold black marker outlines, pure white background, every area left WHITE and empty. "
           "No black fills, no gray, no shading, no hatching, no texture, no text. Maximum 12 large closed shapes. Main subject BIG and centered, "
           "cute rounded friendly cartoon style, nothing scary or realistic. Subject: ")
        Path("그림/카테고리").mkdir(parents=True,exist_ok=True)
        for k in range(0,len(new),50):
            print(t.요청('색칠놀이','콩콩이숲',f'카테고리{k//50+1}',[{"id":i,"prompt":B+p} for i,p in new[k:k+50]],str(Path('그림/카테고리').resolve()),'1:1'))
