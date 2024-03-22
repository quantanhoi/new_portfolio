import requests
from assets.apiKey import api_key
# match Id example
match_id = '1-048d57d0-57b8-4c3f-9cbc-d57b9e138926'

# Set the URL for the request

# player_detail_url = 'https://open.faceit.com/data/v4/players/'
game_id = 'cs2'


#initialize dictionay
map_stats = {}
team1_map_stats = {}
team2_map_stats = {}

# Set the headers, including the Authorization header with the API key
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def get_match_details(match_id):
    match_detail_url = f'https://open.faceit.com/data/v4/matches/{match_id}'
    # Make the GET request
    response = requests.get(match_detail_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        match_details = response.json()
        team = match_details['teams']
        faction1 = team['faction1']
        faction2 = team['faction2']
        players = faction1['roster'] + faction2['roster']

        
        #faction1
        print("Team 1")
        for player in faction1['roster']:
            print(player['nickname'])
            get_player_details(player['player_id'], team1_map_stats)

        #faction2
        print("Team 2")
        for player in faction2['roster']:  
            print(player['nickname'])
            get_player_details(player['player_id'], team2_map_stats)
            

        
        #print map win ratio both team
        print("Team 1 Map Win Ratio:")
        map_win_ratio(team1_map_stats)
        print("Team 2 Map Win Ratio:")
        map_win_ratio(team2_map_stats)
        
        #clear teaam map stats
        team1_map_stats.clear()
        team2_map_stats.clear()
        
    else:
        print(f'Failed to retrieve match details. Status code: {response.status_code}')
    
    
def get_player_details(player_id, team_map_stats):
    limit = 30
    player_detail_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/{game_id}/stats?offset=0&limit={limit}'
    response = requests.get(player_detail_url, headers=headers)
    player_detail = response.json()
    player_matches = player_detail['items']
    for player_match in player_matches:
        match_details = player_match['stats']
        map = match_details['Map']
        result = match_details['Result']
        # print("Map: " + map + " Result: " + result)
        update_map_stats(map, result, team_map_stats)
    #print(map_stats)
    map_win_ratio(map_stats)
    #clear player map stats
    map_stats.clear()

def update_map_stats(map_name, result, team_map_stats):
    # If the map is not already in the dictionary, add it with initial win/loss counts
    if map_name not in map_stats:
        map_stats[map_name] = {'wins': 0, 'losses': 0}
    
    if map_name not in team_map_stats:
        team_map_stats[map_name] = {'wins': 0, 'losses': 0}
    
    # Increment the win or loss count based on the result
    if result == '1':  # win = 1, loss = 0
        map_stats[map_name]['wins'] += 1
        team_map_stats[map_name]['wins'] += 1
    else:  
        map_stats[map_name]['losses'] += 1
        team_map_stats[map_name]['losses'] += 1
        
def map_win_ratio(map_stats):
    for map_name in map_stats:
        wins = map_stats[map_name]['wins']
        losses = map_stats[map_name]['losses']
        total = wins + losses
        if total > 0:
            win_ratio = wins / total
            print(f'{map_name}: {win_ratio:.2%} ({wins}/{total})')
        else:
            print(f'{map_name}: No matches played')
            
#
# 
# get_match_details()

