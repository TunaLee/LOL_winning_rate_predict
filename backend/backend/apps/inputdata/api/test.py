import json, time
import requests
from urllib import parse
from bs4 import BeautifulSoup
from lxml import etree, html

#kor_list
id_name_kor_list = {"266": "아트록스", "103": "아리", "84": "아칼리", "12": "알리스타", "32": "아무무", 
                    "34": "애니비아", "1": "애니", "523": "아펠리오스", "22": "애쉬", "136": "아우렐리온 솔", 
                    "268": "아지르", "432": "바드", "53": "블리츠크랭크", "63": "브랜드", "201": "브라움", 
                    "51": "케이틀린", "164": "카밀", "69": "카시오페이아", "31": "초가스", "42": "코르키", 
                    "122": "다리우스", "131": "다이애나", "119": "드레이븐", "36": "문도 박사", "245": "에코", 
                    "60": "엘리스", "28": "이블린", "81": "이즈리얼", "9": "피들스틱", "114": "피오라", 
                    "105": "피즈", "3": "갈리오", "41": "갱플랑크", "86": "가렌", "150": "나르", "79": "그라가스", 
                    "104": "그레이브즈", "120": "헤카림", "74": "하이머딩거", "420": "일라오이", "39": "이렐리아", 
                    "427": "아이번", "40": "잔나", "59": "자르반 4세", "24": "잭스", "126": "제이스", "202": "진", 
                    "222": "징크스", "145": "카이사", "429": "칼리스타", "43": "카르마", "30": "카서스", "38": "카시딘", 
                    "55": "카타리나", "10": "케일", "141": "케인", "85": "케넨", "121": "카직스", "203": "킨드레드", 
                    "240": "클레드", "96": "코그모", "7": "르블랑", "64": "리 신", "89": "레오나", "876": "릴리아", 
                    "127": "리산드라", "236": "루시안", "117": "룰루", "99": "럭스", "54": "말파이트", "90": "말자하", 
                    "57": "마오카이", "11": "마스터 이", "21": "미스 포츈", "62": "오공", "82": "모데카이저", 
                    "25": "모르가나", "267": "나미", "75": "나서스", "111": "노틸러스", "518": "니코", "76": "니달리", 
                    "56": "녹턴", "20": "누누와 윌럼프", "2": "올라프", "61": "오리아나", "516": "오른", "80": "판테온", 
                    "78": "뽀삐", "555": "파이크", "246": "키아나", "133": "퀸", "497": "라칸", "33": "람머스", 
                    "421": "렉사이", "58": "레넥톤", "107": "렝가", "92": "리븐", "68": "럼블", "13": "라이즈", 
                    "360": "사미라", "113": "세주아니", "235": "세나", "147": "세라핀", "875": "세트", "35": "샤코", 
                    "98": "쉔", "102": "쉬바나", "27": "신지드", "14": "사이온", "15": "시비르", "72": "스카너", 
                    "37": "소나", "16": "소라카", "50": "스웨인", "517": "사일러스", "134": "신드라", "223": "탐 켄치", 
                    "163": "탈리야", "91": "탈론", "44": "타릭", "17": "티모", "412": "쓰레쉬", "18": "트리스타나", "48": "트런들", 
                    "23": "트린다미어", "4": "트위스티드 페이트", "29": "트위치", "77": "우디르", "6": "우르곳", "110": "바루스", 
                    "67": "베인", "45": "베이가", "161": "벨코즈", "254": "바이", "112": "빅토르", "8": "블라디미르", "106": "볼리베어", 
                    "19": "워윅", "498": "자야", "101": "제라스", "5": "신 짜오", "157": "야스오", "777": "요네", "83": "요릭", 
                    "350": "유미", "154": "자크", "238": "제드", "115": "직스", "26": "질리언", "142": "조이", "143": "자이라"}
#eng list
id_name_list = {"266": "Aatrox", "103": "Ahri", "84": "Akali", "12": "Alistar", "32": "Amumu", "34": "Anivia", 
                "1": "Annie", "523": "Aphelios", "22": "Ashe", "136": "Aurelion Sol", "268": "Azir", "432": "Bard", 
                "53": "Blitzcrank", "63": "Brand", "201": "Braum", "51": "Caitlyn", "164": "Camille", "69": "Cassiopeia", 
                "31": "Cho'Gath", "42": "Corki", "122": "Darius", "131": "Diana", "119": "Draven", "36": "Dr. Mundo", 
                "245": "Ekko", "60": "Elise", "28": "Evelynn", "81": "Ezreal", "9": "Fiddlesticks", "114": "Fiora", 
                "105": "Fizz", "3": "Galio", "41": "Gangplank", "86": "Garen", "150": "Gnar", "79": "Gragas", "104": "Graves",
                "120": "Hecarim", "74": "Heimerdinger", "420": "Illaoi", "39": "Irelia", "427": "Ivern", "40": "Janna", 
                "59": "Jarvan IV", "24": "Jax", "126": "Jayce", "202": "Jhin", "222": "Jinx", "145": "Kai'Sa", "429": "Kalista", 
                "43": "Karma", "30": "Karthus", "38": "Kassadin", "55": "Katarina", "10": "Kayle", "141": "Kayn", "85": "Kennen", 
                "121": "Kha'Zix", "203": "Kindred", "240": "Kled", "96": "Kog'Maw", "7": "LeBlanc", "64": "Lee Sin", "89": "Leona", 
                "876": "Lillia", "127": "Lissandra", "236": "Lucian", "117": "Lulu", "99": "Lux", "54": "Malphite", "90": "Malzahar", 
                "57": "Maokai", "11": "Master Yi", "21": "Miss Fortune", "62": "Wukong", "82": "Mordekaiser", "25": "Morgana", 
                "267": "Nami", "75": "Nasus", "111": "Nautilus", "518": "Neeko", "76": "Nidalee", "56": "Nocturne", 
                "20": "Nunu & Willump", "2": "Olaf", "61": "Orianna", "516": "Ornn", "80": "Pantheon", "78": "Poppy", "555": "Pyke", 
                "246": "Qiyana", "133": "Quinn", "497": "Rakan", "33": "Rammus", "421": "Rek'Sai", "58": "Renekton", "107": "Rengar", 
                "92": "Riven", "68": "Rumble", "13": "Ryze", "360": "Samira", "113": "Sejuani", "235": "Senna", "147": "Seraphine", 
                "875": "Sett", "35": "Shaco", "98": "Shen", "102": "Shyvana", "27": "Singed", "14": "Sion", "15": "Sivir", 
                "72": "Skarner", "37": "Sona", "16": "Soraka", "50": "Swain", "517": "Sylas", "134": "Syndra", "223": "Tahm Kench", 
                "163": "Taliyah", "91": "Talon", "44": "Taric", "17": "Teemo", "412": "Thresh", "18": "Tristana", "48": "Trundle", 
                "23": "Tryndamere", "4": "Twisted Fate", "29": "Twitch", "77": "Udyr", "6": "Urgot", "110": "Varus", "67": "Vayne", 
                "45": "Veigar", "161": "Vel'Koz", "254": "Vi", "112": "Viktor", "8": "Vladimir", "106": "Volibear", "19": "Warwick", 
                "498": "Xayah", "101": "Xerath", "5": "Xin Zhao", "157": "Yasuo", "777": "Yone", "83": "Yorick", "350": "Yuumi", 
                "154": "Zac", "238": "Zed", "115": "Ziggs", "26": "Zilean", "142": "Zoe", "143": "Zyra"}

#champ name to lowercase - without space.
name_eng_simple = {}
for key, val  in id_name_list.items():
    if 'nunu' == val[0:4]: #누누와 윌럼프 예외처리
        name_eng_simple[key] = 'nunu'
    else:
        name_eng_simple[key] = val.lower().replace('\'', '').replace(' ', '').replace('_', '').replace('%20','').replace('.', '')
name_kor_simple = {}
for key, val in id_name_kor_list.items():
    if '누누'==val[0:2]:
        name_kor_simple[key] = '누누'
    else:
        name_kor_simple[key] = val.replace(' ', '').replace('_', '').replace('%20','').replace('.','')

def simplify(name): #단순화
    global id_name_list, id_name_kor_list, name_eng_simple, name_kor_simple
    name1 = ''
    if 'nunu'== name[0:4]: #누누와 윌럼프 예외처리
        return 'nunu'
    elif '누누'== name[0:2]: #누누와 윌럼프 예외처리 
        return '누누'
    elif name[0] in [chr(i) for i in list(range(65,91))+list(range(97,123))]: #알파벳...
        name1= name.lower().replace('\'', '').replace(' ', '').replace('_', '').replace('%20','').replace('.','')
        return name1 if name1 in name_eng_simple.values()  else name
    elif name[0] in [chr(i) for i in range(44032, 55204)]: #한글로 시작
        name1= name.replace(' ', '').replace('_', '').replace('%20','').replace('.','.')
        return name1 if name1 in name_kor_simple.values() else name
    else:
        return name
    
def match_kor_eng(name, simple=False): #챔피언 이름 확인
    global id_name_list, id_name_kor_list, name_eng_simple, name_kor_simple
    key='0'
    if 'nunu' == name[0:4]:  #누누는 예외처리.
        name = 'nunu'
    elif '누누'== name[0:2]: #누누 예외처리
        name = '누누'
    else:
        name = name.lower().replace('\'', '').replace(' ', '').replace('_', '').replace('+','').replace('%20','').replace('.','')
    if name in name_eng_simple.values(): #영어 이름이면...
        for i in id_name_list.keys():
            if name_eng_simple[i] == name:
                key = str(i) #키값 찾기.
                break
        return name_kor_simple[key] if simple else id_name_kor_list[key]
    elif name in name_kor_simple.values():
        for i in id_name_kor_list.keys():
            if name_kor_simple[i] == name:
                key = str(i)
                break
        return name_eng_simple[key] if simple else id_name_list[key]
    elif name in id_name_list.keys():
        return name_kor_simple[key] if simple else id_name_kor_list[name]

def crawler(name, champion=None):
    starttime = time.time()
    p_name = parse.quote_plus(name)
    html = requests.get(f'https://www.op.gg/summoner/champions/userName={p_name}').text
    soup2 = BeautifulSoup(html, 'lxml')
    source = soup2.find_all('div', {'class':'season-15'})[0]
    txt = source.get_attribute_list('data-tab-data-url')[0]
    try: 
        html3 = requests.get('https://op.gg'+txt).text
        soup0 = BeautifulSoup(html3, 'lxml')
        trs = soup0.find_all('tr')
    except: #url 없으면...
        trs = source.find_all('tr')
    user_dict = dict()
    for tr in trs:
        if len(tr.find_all('td'))>0:
            champ = simplify(tr.find_all('td')[2].text.replace('\n', ''))
            played = tr.find_all('td')[3]
            if len(played.find_all('div', {'class':'Text Left'}))>0: 
                win = played.find_all('div', {'class':'Text Left'})[0].text 
            else:
                win = '0W'
            if len(played.find_all('div', {'class':'Text Right'}))>0:
                lose = played.find_all('div', {'class':'Text Right'})[0].text
            else:
                lose = '0L'
            if len(played.find_all('span', {'class':'WinRatio'}))>0:
                winrate = played.find_all('span', {'class':'WinRatio'})[0].text
            else:
                winrate = '0%'
            user_dict[champ] = [win, lose, winrate]
    
    print(time.time()-starttime)
    if champion == None:
        return user_dict
    elif str(champion) in id_name_list.keys():
        return user_dict[name_eng_simple[str(champion)]]
    elif simplify(champion) in name_eng_simple.values():
        return user_dict[simplify(champion)]
    elif simplify(champion) in name_kor_simple.values():
        return user_dict[match_kor_eng(champion, simple=True)]
    else:
        return ''