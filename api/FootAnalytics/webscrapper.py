from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import unidecode
import json
os.environ['KMP_DUPLICATE_LIB_OK']='True'

fbrefadderURL = 'http://fbref.com'


columns = ['goals', 'assists', 'non-penalty_goals', 'penalty_kicks_made', 'penalty_kicks_attempted', 'yellow_cards', 'red_cards', 'xg', 'npxg', 
'xa', 'npxg+xa', 'goals', 'shots_total', 'shots_on_target', 'shots_on_target_%', 'goals/shot', 'goals/shot_on_target', 
'average_shot_distance', 'shots_from_free_kicks', 'penalty_kicks_made', 'penalty_kicks_attempted', 'xg', 'npxg', 'npxg/sh', 'goals_-_xg',
'non-penalty_goals_-_npxg', 'passes_completed', 'passes_attempted', 'pass_completion_%', 'total_passing_distance', 'progressive_passing_distance', 
'passes_completed_(short)', 'passes_attempted_(short)', 'pass_completion_%_(short)', 'passes_completed_(medium)', 'passes_attempted_(medium)', 
'pass_completion_%_(medium)', 'passes_completed_(long)', 'passes_attempted_(long)', 'pass_completion_%_(long)', 'assists', 'xa', 'key_passes', 
'passes_into_final_third', 'passes_into_penalty_area', 'crosses_into_penalty_area', 'progressive_passes', 'passes_attempted', 'live-ball_passes', 
'dead-ball_passes', 'passes_from_free_kicks', 'through_balls', 'passes_under_pressure', 'switches', 'crosses', 'corner_kicks', 'inswinging_corner_kicks',
'outswinging_corner_kicks', 'straight_corner_kicks', 'ground_passes', 'low_passes', 'high_passes', 'passes_attempted_(left)', 'passes_attempted_(right)', 
'passes_attempted_(head)', 'throw-ins_taken', 'passes_attempted_(other)', 'passes_completed', 'passes_offside', 'passes_out_of_bounds', 'passes_intercepted', 
'passes_blocked', 'shot-creating_actions', 'sca_(passlive)', 'sca_(passdead)', 'sca_(drib)', 'sca_(sh)', 'sca_(fld)', 'sca_(def)', 'goal-creating_actions', 
'gca_(passlive)', 'gca_(passdead)', 'gca_(drib)', 'gca_(sh)', 'gca_(fld)', 'gca_(def)', 'tackles', 'tackles_won', 'tackles_(def_3rd)', 'tackles_(mid_3rd)', 
'tackles_(att_3rd)', 'dribblers_tackled', 'dribbles_contested', '%_of_dribblers_tackled', 'dribbled_past', 'pressures', 'successful_pressures', 'successful_pressure_%', 
'pressures_(def_3rd)', 'pressures_(mid_3rd)', 'pressures_(att_3rd)', 'blocks', 'shots_blocked', 'shots_saved', 'passes_blocked', 'interceptions', 'tkl+int', 'clearances', 
'errors', 'touches', 'touches_(def_pen)', 'touches_(def_3rd)', 'touches_(mid_3rd)', 'touches_(att_3rd)', 'touches_(att_pen)', 'touches_(live-ball)', 'dribbles_completed', 
'dribbles_attempted', 'successful_dribble_%', 'players_dribbled_past', 'nutmegs', 'carries', 'total_carrying_distance', 'progressive_carrying_distance', 'progressive_carries', 
'carries_into_final_third', 'carries_into_penalty_area', 'miscontrols', 'dispossessed', 'pass_targets', 'passes_received', 'passes_received_%', 'progressive_passes_rec', 
'yellow_cards', 'red_cards', 'second_yellow_card', 'fouls_committed', 'fouls_drawn', 'offsides', 'crosses', 'interceptions', 'tackles_won', 'penalty_kicks_won', 
'penalty_kicks_conceded', 'own_goals', 'ball_recoveries', 'aerials_won', 'aerials_lost', '%_of_aerials_won']

Cannot_or_will_not_find = {'goals_per90': {'value': None, 'percentile': None}, 'assists_per90': {'value': None, 'percentile': None},
 'non-penalty_goals_per90': {'value': None, 'percentile': None}, 'penalty_kicks_made_per90': {'value': None, 'percentile': None}, 
 'penalty_kicks_attempted_per90': {'value': None, 'percentile': None}, 'yellow_cards_per90': {'value': None, 'percentile': None}, 
 'red_cards_per90': {'value': None, 'percentile': None}, 'xg_per90': {'value': None, 'percentile': None}, 
 'npxg_per90': {'value': None, 'percentile': None}, 'xa_per90': {'value': None, 'percentile': None}, 
 'npxg+xa_per90': {'value': None, 'percentile': None}, 'shots_total_per90': {'value': None, 'percentile': None}, 
 'shots_on_target_per90': {'value': None, 'percentile': None}, 'shots_on_target_%_per90': {'value': None, 'percentile': None}, 
 'goals/shot_per90': {'value': None, 'percentile': None}, 'goals/shot_on_target_per90': {'value': None, 'percentile': None}, 
 'average_shot_distance_per90': {'value': None, 'percentile': None}, 'shots_from_free_kicks_per90': {'value': None, 'percentile': None}, 
 'npxg/sh_per90': {'value': None, 'percentile': None}, 'goals_-_xg_per90': {'value': None, 'percentile': None}, 
 'non-penalty_goals_-_npxg_per90': {'value': None, 'percentile': None}, 'passes_completed_per90': {'value': None, 'percentile': None}, 
 'passes_attempted_per90': {'value': None, 'percentile': None}, 'pass_completion_%_per90': {'value': None, 'percentile': None}, 
 'total_passing_distance_per90': {'value': None, 'percentile': None}, 
 'progressive_passing_distance_per90': {'value': None, 'percentile': None}, 
 'passes_completed_(short)_per90': {'value': None, 'percentile': None}, 'passes_attempted_(short)_per90': {'value': None, 'percentile': None}, 
 'pass_completion_%_(short)_per90': {'value': None, 'percentile': None}, 'passes_completed_(medium)_per90': {'value': None, 'percentile': None}, 
 'passes_attempted_(medium)_per90': {'value': None, 'percentile': None}, 'pass_completion_%_(medium)_per90': {'value': None, 'percentile': None}, 
 'passes_completed_(long)_per90': {'value': None, 'percentile': None}, 'passes_attempted_(long)_per90': {'value': None, 'percentile': None}, 
 'pass_completion_%_(long)_per90': {'value': None, 'percentile': None}, 'key_passes_per90': {'value': None, 'percentile': None}, 
 'passes_into_final_third_per90': {'value': None, 'percentile': None}, 'passes_into_penalty_area_per90': {'value': None, 'percentile': None}, 
 'crosses_into_penalty_area_per90': {'value': None, 'percentile': None}, 'progressive_passes_per90': {'value': None, 'percentile': None}, 
 'live-ball_passes_per90': {'value': None, 'percentile': None}, 'dead-ball_passes_per90': {'value': None, 'percentile': None}, 
 'passes_from_free_kicks_per90': {'value': None, 'percentile': None}, 'through_balls_per90': {'value': None, 'percentile': None}, 
 'passes_under_pressure_per90': {'value': None, 'percentile': None}, 'switches_per90': {'value': None, 'percentile': None}, 
 'crosses_per90': {'value': None, 'percentile': None}, 'corner_kicks_per90': {'value': None, 'percentile': None}, 
 'inswinging_corner_kicks_per90': {'value': None, 'percentile': None}, 'outswinging_corner_kicks_per90': {'value': None, 
 'percentile': None}, 'straight_corner_kicks_per90': {'value': None, 'percentile': None}, 
 'ground_passes_per90': {'value': None, 'percentile': None}, 'low_passes_per90': {'value': None, 'percentile': None}, 
 'high_passes_per90': {'value': None, 'percentile': None}, 'passes_attempted_(left)_per90': {'value': None, 'percentile': None}, 
 'passes_attempted_(right)_per90': {'value': None, 'percentile': None}, 'passes_attempted_(head)_per90': {'value': None, 'percentile': None}, 
 'throw-ins_taken_per90': {'value': None, 'percentile': None}, 'passes_attempted_(other)_per90': {'value': None, 'percentile': None}, 
 'passes_offside_per90': {'value': None, 'percentile': None}, 'passes_out_of_bounds_per90': {'value': None, 'percentile': None}, 
 'passes_intercepted_per90': {'value': None, 'percentile': None}, 'passes_blocked_per90': {'value': None, 'percentile': None}, 
 'shot-creating_actions_per90': {'value': None, 'percentile': None}, 'sca_(passlive)_per90': {'value': None, 'percentile': None}, 
 'sca_(passdead)_per90': {'value': None, 'percentile': None}, 'sca_(drib)_per90': {'value': None, 'percentile': None}, 
 'sca_(sh)_per90': {'value': None, 'percentile': None}, 'sca_(fld)_per90': {'value': None, 'percentile': None}, 
 'sca_(def)_per90': {'value': None, 'percentile': None}, 'goal-creating_actions_per90': {'value': None, 'percentile': None}, 
 'gca_(passlive)_per90': {'value': None, 'percentile': None}, 'gca_(passdead)_per90': {'value': None, 'percentile': None}, 
 'gca_(drib)_per90': {'value': None, 'percentile': None}, 'gca_(sh)_per90': {'value': None, 'percentile': None}, 
 'gca_(fld)_per90': {'value': None, 'percentile': None}, 'gca_(def)_per90': {'value': None, 'percentile': None}, 
 'tackles_per90': {'value': None, 'percentile': None}, 'tackles_won_per90': {'value': None, 'percentile': None}, 
 'tackles_(def_3rd)_per90': {'value': None, 'percentile': None}, 'tackles_(mid_3rd)_per90': {'value': None, 'percentile': None}, 
 'tackles_(att_3rd)_per90': {'value': None, 'percentile': None}, 'dribblers_tackled_per90': {'value': None, 'percentile': None}, 
 'dribbles_contested_per90': {'value': None, 'percentile': None}, '%_of_dribblers_tackled_per90': {'value': None, 'percentile': None}, 
 'dribbled_past_per90': {'value': None, 'percentile': None}, 'pressures_per90': {'value': None, 'percentile': None}, 
 'successful_pressures_per90': {'value': None, 'percentile': None}, 'successful_pressure_%_per90': {'value': None, 'percentile': None}, 
 'pressures_(def_3rd)_per90': {'value': None, 'percentile': None}, 'pressures_(mid_3rd)_per90': {'value': None, 'percentile': None}, 
 'pressures_(att_3rd)_per90': {'value': None, 'percentile': None}, 'blocks_per90': {'value': None, 'percentile': None}, 
 'shots_blocked_per90': {'value': None, 'percentile': None}, 'shots_saved_per90': {'value': None, 'percentile': None}, 
 'interceptions_per90': {'value': None, 'percentile': None}, 'tkl+int_per90': {'value': None, 'percentile': None}, 
 'clearances_per90': {'value': None, 'percentile': None}, 'errors_per90': {'value': None, 'percentile': None}, 
 'touches_per90': {'value': None, 'percentile': None}, 'touches_(def_pen)_per90': {'value': None, 'percentile': None}, 
 'touches_(def_3rd)_per90': {'value': None, 'percentile': None}, 'touches_(mid_3rd)_per90': {'value': None, 'percentile': None}, 
 'touches_(att_3rd)_per90': {'value': None, 'percentile': None}, 'touches_(att_pen)_per90': {'value': None, 'percentile': None}, 
 'touches_(live-ball)_per90': {'value': None, 'percentile': None}, 'dribbles_completed_per90': {'value': None, 'percentile': None}, 
 'dribbles_attempted_per90': {'value': None, 'percentile': None}, 'successful_dribble_%_per90': {'value': None, 'percentile': None}, 
 'players_dribbled_past_per90': {'value': None, 'percentile': None}, 'nutmegs_per90': {'value': None, 'percentile': None}, 
 'carries_per90': {'value': None, 'percentile': None}, 'total_carrying_distance_per90': {'value': None, 'percentile': None}, 
 'progressive_carrying_distance_per90': {'value': None, 'percentile': None}, 'progressive_carries_per90': {'value': None, 'percentile': None}, 
 'carries_into_final_third_per90': {'value': None, 'percentile': None}, 'carries_into_penalty_area_per90': {'value': None, 'percentile': None}, 
 'miscontrols_per90': {'value': None, 'percentile': None}, 'dispossessed_per90': {'value': None, 'percentile': None}, 
 'pass_targets_per90': {'value': None, 'percentile': None}, 'passes_received_per90': {'value': None, 'percentile': None}, 
 'passes_received_%_per90': {'value': None, 'percentile': None}, 'progressive_passes_rec_per90': {'value': None, 'percentile': None}, 
 'second_yellow_card_per90': {'value': None, 'percentile': None}, 'fouls_committed_per90': {'value': None, 'percentile': None}, 
 'fouls_drawn_per90': {'value': None, 'percentile': None}, 'offsides_per90': {'value': None, 'percentile': None}, 
 'penalty_kicks_won_per90': {'value': None, 'percentile': None}, 'penalty_kicks_conceded_per90': {'value': None, 'percentile': None}, 
 'own_goals_per90': {'value': None, 'percentile': None}, 'ball_recoveries_per90': {'value': None, 'percentile': None}, 
 'aerials_won_per90': {'value': None, 'percentile': None}, 'aerials_lost_per90': {'value': None, 'percentile': None}, 
 '%_of_aerials_won_per90': {'value': None, 'percentile': None}}


'''
def try_and_except():
    try:

    except:

    return data
'''

def ScrapBig5Page(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})
    data = dict({})
    for tr in table.tbody.find_all("tr"):
        if tr.get("class") != "thead":
            for td in tr.find_all("td"):
                col = td.get("data-stat").strip()
                if col not in data:
                    data[col] = []
        
                if col == "squad":
                    data.get(col).append([td.a.contents[0],
                                          td.img.get("src"), 
                                          str(fbrefadderURL + td.a.get("href"))])
                elif col == "country":
                    data.get(col).append(td.span.contents[0])
                elif (col == "top_team_scorers" or col == "top_keeper"):
                    data.get(col).append(td.a.contents[0])
                elif (col == "last_5"):
                    lst = []
                    for div in td.div.find_all("div"):
                        lst.append(div.a.contents[0])
                    data.get(col).append(lst)
                else:
                    data.get(col).append(td.contents[0])
   
    # Convert to DataFrame
    df = pd.DataFrame(data)      

    # Group Data by Country
    groupedCountries = df.groupby(df.country)

    # Assign Each Country with specific Data
    italy,france,germany,spain,england = groupedCountries.get_group('it'), groupedCountries.get_group('fr'), groupedCountries.get_group('de'), groupedCountries.get_group('es'), groupedCountries.get_group('eng') 
    
    return italy,france,germany,spain,england,df


def ScrapTeamPage(url, players, country):
    # Url - Team Url, 
    # players - True if you want total for all players 
    # players - False if you want simply opponent and squad total
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})

    # Firs Iteration to keep the merging 2 dictionaries code simpler
    first_iter = True

    # Columns that will be numbers
    numbers = ["games", "games_starts", "minutes", "minutes_90s", "pens_made", "pens_att", "goals", "assits", "pens"
        "cards_yellow", "cards_red", "goals_assists_per90", "goals_pens_per90", "goals_assists_pens_per90",
        "xg", "npxg", "xa", "npxg_xa", "xg_xa_per90", "npxg_per90", "npxg_xa_per90"]

    # Columns to ignore before they will be connected through other iteration
    ignore = ['goals_per90', 'assists_per90', 'xg_per90', 'xa_per90', 'npxg_per90']

    # Name of the team and team URL github link / convert to raw.githubuser.com.....
    team_name = (url.split('-Stats')[0]).split('/')[-1]
    github_url =  "https://github.com/jenishpatel2147/FootballGraphs/blob/main/logos/" + country + "/" + team_name + ".png"

    print(team_name)

    # If Scrapping Players
    if players: 
        # Find all Players/Rows
        looper = table.tbody.find_all("tr")
        data = dict({"playerLink": [],
                    "playerName": [],
                    "team": team_name,
                    "logo_url": github_url})
    else:
        looper = table.tfoot.find_all("tr")
        data = dict({"team_type": []})

    counter = 0
        
    # All Players of a team
    for tr in looper:

        counter += 1
        #print("Player: " + str(counter))

        # If Scrapping Players
        if players:
            try:
                link = tr.a.get("href")
            except:
                link = "None"
            try:
                playerName = tr.th.a.contents[0]
            except:
                playerName = "None"

            # Get Name from URL because it doesn't contain accents
            link_name = (link.split('/')[-1])
            name = link_name.replace('-',' ')

            data.get("playerLink").append(link)
            data.get("playerName").append(name)
        
            # Generating URL to send to scarp information about the player
            scout = "scout/365_euro/"
            #print(link)
            firstpart = link.split(link_name)[0]
            #print(firstpart)
            main_url = 'https://fbref.com' + firstpart + scout + link_name + '-Scouting-Report'
            print(main_url)
            try:
                obj = ScrapAllStatsPlayerPage(main_url)
            except:
                print("URL not processed - url printed above")
                obj = Cannot_or_will_not_find
            
            #print(len(obj))
            tmp = Cannot_or_will_not_find.copy()
            # Adding New Data to current data
            for val in obj:
                tmp.pop(val)
                if first_iter:
                    data[val] = [obj.get(val)]
                else:
                    data[val].append(obj[val])

            # Empty Dict Evaluate to False
            if bool(tmp):
                for val in tmp:
                    if first_iter:
                        data[val] = [obj.get(val)]
                    else:
                        data[val].append(tmp[val])
            first_iter = False
        else:
            data.get("team_type").append(str(tr.th.contents[0]))

        # All Values for a player
        for td in tr.find_all("td"):
            
            # Current Column
            col = td.get("data-stat").strip()

            # Collecting this data through the Player's individual page
            if col in ignore:
                continue

            # If first_iter add Column to data
            if col not in data:
                data[col] = []

            # If Scrapping Players
            if players:
                if col == "nationality":
                    try:
                        nationality = td.span.contents[1].strip()
                    except:
                        nationality = "Could Not Find Nationality"
                    data.get(col).append(nationality)
                elif col == "matches":
                    data.get(col).append("")
                elif len(td.contents) > 0:
                    if (col in numbers):
                        data.get(col).append(float(td.contents[0].replace(',','')))
                    else:
                        data.get(col).append(str(td.contents[0]))
                        
                else:
                    if td.contents == []:
                        data.get(col).append(0)
                    else:
                        data.get(col).append(str(td.contents[0]))
            else:
                if len(td.contents) > 0:
                    data.get(col).append(str(td.contents[0]))
                else:
                    data.get(col).append("")
    df = pd.DataFrame(data)
    return df   


def GetLinksForScoutingReports(url, playername):
    obj = {}
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("div", attrs={"class": "section_content"})
    
    # Can also be used to calculate data for previous seasons
    looper = table.find("a", string=["2017-2018 Premier League", "Last 365 Days Men's Big 5 Leagues and European Competition"])
    print(looper.get("href"))


def ScrapAllStatsPlayerPage(url):
    obj = {}
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    table = soup.find("table", attrs={"class": "stats_table"})
    looper = table.tbody.find_all("tr")

    # Loop's over all the tr's
    for loop in looper:        

        # Gets Name of the Column in Lower Case and removing spaces
        name = loop.find('th')
        name = (name.text).replace(' ', '_').lower()

        # We will be ignoring Goalkeepers for now
        if name == "advanced_goalkeeping":
            return Cannot_or_will_not_find
        
        # Edges Cases --> Conver to more Robust handling
        if (name != "" and name != "shooting" and name != "statistic"
           and name != "passing" and name != "pass_types" and 
           name != "goal_and_shot_creation" and name != "defense" 
           and name != "possession" and name != "miscellaneous_stats" and name != "advanced_goalkeeping"):
            trs = (loop.find_all('td'))

            # Get Value
            value = trs[0].text

            # Get Percentile
            percentile = trs[1].find('div').text

            # Error Handing to Float Conversion
            try:
                value = float(value)
            except:
                value = value
    
            # Append to Dict
            obj[name + "_per90"] = { "value" : value, 'percentile': float(percentile)}

    return obj

def extractdata():
    big5url = "https://fbref.com/en/comps/Big5/Big-5-European-Leagues-Stats"

    italy,france,germany,spain,england,ALL = ScrapBig5Page(big5url)

    countries = [italy, france, spain, england, germany]
    fileNames = ["italy", "france", "spain", "england", "germany"]

    for i in range(4, len(countries)):
        print("Starting - " + str(fileNames[i]))
        players = pd.DataFrame()
        iters = 0 
        league = countries[i]
        name = fileNames[i]
        
        for index,row in league.iterrows():
            teamURL = row['squad'][2]
            temp = ScrapTeamPage(teamURL, True, name)
            players = pd.concat([temp,players], axis=0)
            iters +=1
            if iters % 5 == 0:
                print("Finished "+ str(iters) + " teams")

        d = [ 
            dict([
                (colname, row[i])
                for i,colname in enumerate(players.columns)
            ])
            for row in players.values
        ]

        jsonData = json.dumps(d, indent=4)

        fileName = './' + name + '_allplayers.json'
        with open(fileName, 'w') as outputFile:
            print(jsonData, file=outputFile)
        
        print("Finished - " + str(fileNames[i]))