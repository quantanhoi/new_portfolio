from flask import Blueprint, jsonify, request
import requests
from assets.apiKey import api_key
import json

game_id = 'cs2'
# Set the headers, including the Authorization header with the API key
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

#initialize dictionay
map_stats = {}
team1_map_stats = {}
team2_map_stats = {}


faceit_blueprint = Blueprint('faceit', __name__)
@faceit_blueprint.route('/api/faceit', methods=['POST'])
def getBestMapList():
    data = request.json
    match_id = data.get('match_id')
    match_detail_url = f'https://open.faceit.com/data/v4/matches/{match_id}'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(match_detail_url, headers=headers)
    if response.status_code == 200:
        match_details = response.json()
        team = match_details['teams']
        faction1 = team['faction1']
        faction2 = team['faction2']
        
        for player in faction1['roster']:
            get_player_details(player['player_id'], team1_map_stats)
        for player in faction2['roster']:  
            get_player_details(player['player_id'], team2_map_stats)
        final_response = {
        "team1": map_win_ratio_calc(team1_map_stats),
        "team2": map_win_ratio_calc(team2_map_stats)
        }
        team1_map_stats.clear()
        team2_map_stats.clear()
        return jsonify(final_response), 200
    return jsonify({"error": "Match not found"}), 404

    
    
def get_player_details(player_id, team_map_stats):
    limit = 20
    player_detail_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/{game_id}/stats?offset=0&limit={limit}'
    response = requests.get(player_detail_url, headers=headers)
    player_detail = response.json()
    player_matches = player_detail['items']
    for player_match in player_matches:
        match_details = player_match['stats']
        map = match_details['Map']
        result = match_details['Result']
        update_map_stats(map, result, team_map_stats)
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
        
            
def map_win_ratio_calc(map_stats):
    map_win = {}
    for map_name in map_stats:
        if map_name not in map_win:
            map_win[map_name] = {'win_rate': 0, 'total_map_played': 0}
        wins = map_stats[map_name]['wins']
        losses = map_stats[map_name]['losses']
        total = wins + losses
        if total > 0:
            map_win[map_name]['win_rate'] = "{:.2f}%".format(wins / total * 100)
            map_win[map_name]['total_map_played'] = total
    return map_win