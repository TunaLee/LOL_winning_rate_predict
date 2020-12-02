from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd

from backend.apps.inputdata.api.test import crawler

def predict(data):
    df = pd.read_csv('backend/apps/inputdata/api/Join_data.csv').iloc[:,1:]
    X=df.iloc[:,1:-1]
    y=df.iloc[:,-1]
    svm=SVC(probability=True)
    svm.fit(X,y)
    svm.predict([data])
    return svm.predict_proba([data])[0][1]

def deserializer(data):
    champ = pd.read_csv('backend/apps/inputdata/api/Champ_kor.csv')
    teamid = int(data['team_id'])
    our_team = []
    counter_team = []
    our_team.append(data['our_top_champ'])
    our_team.append(data['our_jungle_champ'])
    our_team.append(data['our_middle_champ'])
    our_team.append(data['our_carry_champ'])
    our_team.append(data['our_support_champ'])
    counter_team.append(data['counter_top_champ'])
    counter_team.append(data['counter_jungle_champ'])
    counter_team.append(data['counter_middle_champ'])
    counter_team.append(data['counter_carry_champ'])
    counter_team.append(data['counter_support_champ'])

    our_wr = 0
    counter_wr = 0
    our_team_WR=[]
    counter_team_WR=[]
    for k in range(5):
        for i in range(len(champ)):
            if teamid == 100:
                if our_team[k] == champ.loc[:, 'number'][i]:
                    our_wr += champ.loc[:, 'blue_WR'][i]
                    our_team_WR.append(champ.loc[:, 'blue_WR'][i])
                if counter_team[k] == champ.loc[:, 'number'][i]:
                    counter_wr += champ.loc[:, 'red_WR'][i]
                    counter_team_WR.append(champ.loc[:, 'red_WR'][i])
            else :
                if our_team[k] == champ.loc[:, 'number'][i]:
                    our_wr += champ.loc[:, 'red_WR'][i]
                    our_team_WR.append(champ.loc[:, 'red_WR'][i])
                if counter_team[k] == champ.loc[:, 'number'][i]:
                    counter_wr += champ.loc[:, 'blue_WR'][i]
                    counter_team_WR.append(champ.loc[:, 'blue_WR'][i])
    if teamid == 200:
        champ_WR_dif = counter_wr - our_wr
    else:
        champ_WR_dif = our_wr - counter_wr
    try:
        our_top_win, our_top_loss, our_top_WR = crawler(data['our_top_summoner'], str(data['our_top_champ']))
    except:
        our_top_win, our_top_loss, our_top_WR = ['0W','0L',f'{our_team_WR[0]*100}%']
    try:
        our_jungle_win, our_jungle_loss, our_jungle_WR = crawler(data['our_jungle_summoner'], str(data['our_jungle_champ']))
    except:
        our_jungle_win, our_jungle_loss, our_jungle_WR = ['0W','0L', f'{our_team_WR[1]*100}%']
    try:
        our_middle_win, our_middle_loss, our_middle_WR = crawler(data['our_middle_summoner'], str(data['our_middle_champ']))
    except:
        our_middle_win, our_middle_loss, our_middle_WR = ['0W','0L',f'{our_team_WR[2]*100}%']
    try:
        our_carry_win, our_carry_loss, our_carry_WR = crawler(data['our_carry_summoner'], str(data['our_carry_champ']))
    except:
        our_carry_win, our_carry_loss, our_carry_WR = ['0W','0L', f'{our_team_WR[3]*100}%']
    try:
        our_support_win, our_support_loss, our_support_WR = crawler(data['our_support_summoner'], str(data['our_support_champ']))
    except:
        our_support_win, our_support_loss, our_support_WR = ['0W','0L',f'{our_team_WR[4]*100}%']
    match_cnt = int(our_top_win[:-1])+int(our_top_loss[:-1])+int(our_jungle_win[:-1])+int(our_jungle_loss[:-1])+int(our_middle_win[:-1])+int(our_middle_loss[:-1])+int(our_carry_win[:-1])+int(our_carry_loss[:-1])+int(our_support_win[:-1])+int(our_support_loss[:-1])
    user_champ_WR = (int(float(our_top_WR[:-1])) + int(float(our_jungle_WR[:-1])) + int(float(our_middle_WR[:-1])) + int(float(our_carry_WR[:-1])) + int(float(our_support_WR[:-1])))/5


    with open('backend/apps/inputdata/api/LOL_Champ_Tier.json', 'rb') as f:
        tier_data = json.load(f)

    top_tier_df = pd.DataFrame(tier_data[0])
    jungle_tier_df = pd.DataFrame(tier_data[1])
    mid_tier_df = pd.DataFrame(tier_data[2])
    carry_tier_df = pd.DataFrame(tier_data[3])
    support_tier_df = pd.DataFrame(tier_data[4])
    top_tier = 6
    jungle_tier = 6
    mid_tier = 6
    carry_tier = 6
    support_tier = 6
    c_top_tier = 6
    c_jungle_tier = 6
    c_mid_tier = 6
    c_carry_tier = 6
    c_support_tier = 6
    for j in range(len(top_tier_df)):
        if our_team[0] == top_tier_df.loc[:, 'champid'][j]:
            top_tier = top_tier_df.loc[:, 'tier'][j]
        if counter_team[0] == top_tier_df.loc[:, 'champid'][j]:
            c_top_tier = top_tier_df.loc[:, 'tier'][j]

    for j in range(len(jungle_tier_df)):
        if our_team[1] == jungle_tier_df.loc[:, 'champid'][j]:
            jungle_tier = jungle_tier_df.loc[:, 'tier'][j]
        if counter_team[1] == jungle_tier_df.loc[:, 'champid'][j]:
            c_jungle_tier = jungle_tier_df.loc[:, 'tier'][j]

    for j in range(len(mid_tier_df)):
        if our_team[2] == mid_tier_df.loc[:, 'champid'][j]:
            mid_tier = mid_tier_df.loc[:, 'tier'][j]
        if counter_team[2] == mid_tier_df.loc[:, 'champid'][j]:
            c_mid_tier = mid_tier_df.loc[:, 'tier'][j]

    for j in range(len(carry_tier_df)):
        if our_team[3] == carry_tier_df.loc[:, 'champid'][j]:
            carry_tier = carry_tier_df.loc[:, 'tier'][j]
        if counter_team[3] == carry_tier_df.loc[:, 'champid'][j]:
            c_carry_tier = carry_tier_df.loc[:, 'tier'][j]

    for j in range(len(support_tier_df)):
        if our_team[4] == support_tier_df.loc[:, 'champid'][j]:
            support_tier = support_tier_df.loc[:, 'tier'][j]
        if counter_team[4] == support_tier_df.loc[:, 'champid'][j]:
            c_support_tier = support_tier_df.loc[:, 'tier'][j]

    Slayer = ['Nocturne', 'Nidalee', 'Rengar', 'LeBlanc', 'Master Yi', 'Shaco', 'Akali', 'Ekko', 'Yone',
              'Evelynn', 'Zed', 'Kassadin', "Kha'Zix", 'Katarina', 'Qiyana', 'Talon', 'Fizz']
    Tank = ['Galio', 'Nautilus', 'Nunu & Willump', 'Rammus', 'Leona', 'Maokai', 'Malphite', 'Blitzcrank',
            'Poppy', 'Sion', 'Sejuani', 'Shen', 'Singed', 'Amumu', 'Alistar', 'Ornn', 'Jarvan IV', 'Zac',
            "Cho'Gath"]
    Fighter = ['Garen', 'Gangplank', 'Gragas', 'Gnar', 'Nasus', 'Darius', 'Diana', 'Rumble', 'Renekton',
               "Rek'Sai", 'Lee Sin', 'Riven', 'Lillia', 'Mordekaiser', 'Dr. Mundo', 'Vi', 'Volibear', 'Sett',
               'Shyvana', 'Skarner', 'Xin Zhao', 'Aatrox', 'Yasuo', 'Wukong', 'Olaf', 'Yorick', 'Udyr', 'Urgot',
               'Warwick', 'Irelia', 'Illaoi', 'Jax', 'Jayce', 'Camille', 'Kayn', 'Kayle', 'Kled', 'Trundle',
               'Tryndamere', 'Pantheon', 'Fiora', 'Hecarim']
    Mage = ['Neeko', 'Ryze', 'Lux', 'Lissandra', 'Malzahar', 'Morgana', 'Veigar', "Vel'Koz", 'Brand',
            'Vladimir', 'Viktor', 'Sylas', 'Seraphine', 'Swain', 'Syndra', 'Ahri', 'Aurelion Sol', 'Azir',
            'Annie', 'Anivia', 'Elise', 'Orianna', 'Zyra', 'Xerath', 'Zoe', 'Ziggs', 'Karma', 'Karthus',
            'Cassiopeia', 'Kennen', 'Taliyah', 'Twisted Fate', 'Fiddlesticks', 'Heimerdinger']
    Marksman = ['Graves', 'Draven', 'Lucian', 'Miss Fortune', 'Varus', 'Vayne', 'Samira', 'Senna', 'Sivir',
                'Aphelios', 'Ashe', 'Ezreal', 'Xayah', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Caitlyn',
                "Kog'Maw", 'Corki', 'Quinn', 'Kindred', 'Tristana', 'Twitch', 'Teemo']
    Controller = ['Nami', 'Rakan', 'Lulu', 'Bard', 'Braum', 'Sona', 'Soraka', 'Thresh', 'Ivern', 'Yuumi',
                  'Janna', 'Zilean', 'Taric', 'Tahm Kench', 'Pyke']

    with open('backend/apps/inputdata/api/champion_id_and_name_list.json', 'rb') as f:
        champlist = json.load(f)

    for i in range(len(Slayer)):
        for j in range(152):
            if Slayer[i] == list(champlist.values())[j]:
                Slayer[i] = list(champlist.keys())[j]
                break
    for i in range(len(Tank)):
        for j in range(152):
            if Tank[i] == list(champlist.values())[j]:
                Tank[i] = list(champlist.keys())[j]
                break
    for i in range(len(Fighter)):
        for j in range(152):
            if Fighter[i] == list(champlist.values())[j]:
                Fighter[i] = list(champlist.keys())[j]
                break
    for i in range(len(Mage)):
        for j in range(152):
            if Mage[i] == list(champlist.values())[j]:
                Mage[i] = list(champlist.keys())[j]
                break
    for i in range(len(Marksman)):
        for j in range(152):
            if Marksman[i] == list(champlist.values())[j]:
                Marksman[i] = list(champlist.keys())[j]
                break
    for i in range(len(Controller)):
        for j in range(152):
            if Controller[i] == list(champlist.values())[j]:
                Controller[i] = list(champlist.keys())[j]
                break
    Slayer = list(map(int, Slayer))
    Tank = list(map(int, Tank))
    Mage = list(map(int, Mage))
    Fighter = list(map(int, Fighter))
    Marksman = list(map(int, Marksman))
    Controller = list(map(int, Controller))
    slayer=0
    tank=0
    mage=0
    fighter=0
    marksman=0
    controller=0
    c_slayer = 0
    c_tank = 0
    c_mage = 0
    c_fighter = 0
    c_marksman = 0
    c_controller = 0
    for j in range(5):
        if our_team[j] in Slayer:
            slayer+= 1
        elif our_team[j] in Tank:
            tank += 1
        elif our_team[j] in Fighter:
            fighter += 1
        elif our_team[j] in Mage:
            mage += 1
        elif our_team[j] in Marksman:
            marksman += 1
        elif our_team[j] in Controller:
            controller += 1

        if counter_team[j] in Slayer:
            c_slayer += 1
        elif counter_team[j] in Tank:
            c_tank += 1
        elif counter_team[j] in Fighter:
            c_fighter += 1
        elif counter_team[j] in Mage:
            c_mage += 1
        elif counter_team[j] in Marksman:
            c_marksman += 1
        elif counter_team[j] in Controller:
            c_controller += 1


    return [teamid,champ_WR_dif,user_champ_WR,top_tier,jungle_tier,mid_tier,carry_tier,support_tier,c_top_tier,c_jungle_tier, c_mid_tier, c_carry_tier, c_support_tier, slayer,tank,fighter,mage,marksman,controller,c_slayer, c_tank, c_fighter, c_mage, c_marksman, c_controller, match_cnt]

# print(predict([100,0.1,52.0,2.0,1.0,2.0,2.0,1.0,3.0,3.0,3.0,3.0,3.0,1.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,0.0,2.0,1.0,1.0,200]))
