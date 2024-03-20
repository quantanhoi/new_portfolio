import requests
from assets.apiKey import api_key
# match Id example
match_id = '1-6fa90eb2-cacf-4008-b77c-98d9c9ce4e39'

# Set the URL for the request
match_detail_url = f'https://open.faceit.com/data/v4/matches/{match_id}'
# player_detail_url = 'https://open.faceit.com/data/v4/players/'
game_id = 'cs2'


#initialize dictionay
map_stats = {}

# Set the headers, including the Authorization header with the API key
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def get_match_details():
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
        for player in players:
            print(player['player_id'] + ' ' + player['nickname'])
            get_player_details(player['player_id'])
    else:
        print(f'Failed to retrieve match details. Status code: {response.status_code}')
    
    
def get_player_details(player_id):
    limit = 20
    player_detail_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/{game_id}/stats?offset=0&limit={limit}'
    response = requests.get(player_detail_url, headers=headers)
    player_detail = response.json()
    player_matches = player_detail['items']
    for player_match in player_matches:
        match_details = player_match['stats']
        map = match_details['Map']
        result = match_details['Result']
        # print("Map: " + map + " Result: " + result)
        update_map_stats(map, result)
    print(map_stats)
    map_win_ratio(map_stats)
    map_stats.clear()

def update_map_stats(map_name, result):
    # If the map is not already in the dictionary, add it with initial win/loss counts
    if map_name not in map_stats:
        map_stats[map_name] = {'wins': 0, 'losses': 0}
    
    # Increment the win or loss count based on the result
    if result == '1':  # Assuming '1' indicates a win
        map_stats[map_name]['wins'] += 1
    else:  # Assuming '0' indicates a loss
        map_stats[map_name]['losses'] += 1
def map_win_ratio(map_stats):
    for map_name in map_stats:
        wins = map_stats[map_name]['wins']
        losses = map_stats[map_name]['losses']
        total = wins + losses
        if total > 0:
            win_ratio = wins / total
            print(f'{map_name}: {win_ratio:.2f} ({wins}/{total})')
        else:
            print(f'{map_name}: No matches played')
get_match_details()

