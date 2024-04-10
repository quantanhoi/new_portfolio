from flask import Blueprint, jsonify, request
import requests
from assets.apiKey import api_key
import json
from time import process_time

game_id = 'cs2'
# Set the headers, including the Authorization header with the API key
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}


faceit_blueprint = Blueprint('faceit', __name__)
@faceit_blueprint.route('/api/faceit', methods=['POST'])
def getBestMapList():
    processTimeStart = process_time()
    #initialize dictionary for team 1 and team 2, team1_map_stats contains map statistic for whole team
    #team1_player_stats contains each player statistics in a team
    team1_map_stats = {}
    team1_player_stats = {}
    team2_map_stats = {}
    team2_player_stats = {}
    data = request.json
    match_id = data.get('match_id')
    match_detail_url = f'https://open.faceit.com/data/v4/matches/{match_id}'
    response = requests.get(match_detail_url, headers=headers)
    if response.status_code == 200:
        match_details = response.json()
        team = match_details['teams']
        faction1 = team['faction1']
        faction1_name = faction1['name']
        faction2 = team['faction2']
        faction2_name = faction2['name']
        for player in faction1['roster']:
            team1_player_stats[player['nickname']] = get_player_details(player['player_id'], team1_map_stats)
            
        for player in faction2['roster']:  
            team2_player_stats[player['nickname']] = get_player_details(player['player_id'], team2_map_stats)
        final_response = {
        f'{faction1_name}': {"map_statistics": calculate_team_map_win_rate(team1_player_stats), "player_statistics": team1_player_stats},
        f'{faction2_name}': {"map_statistics": calculate_team_map_win_rate(team2_player_stats), "player_statistics": team2_player_stats}
        }
        team1_map_stats.clear()
        team2_map_stats.clear()
        processTimeStop = process_time()
        print("Elapsed time during the whole program in seconds:", processTimeStop-processTimeStart)  
        return jsonify(final_response), 200
    return jsonify({"error": "Match not found"}), 404



def get_player_details(player_id, team_map_stats):
    """Get the player's match history and update the map stats dictionary

    Args:
        player_id (_type_): _description_
        team_map_stats (_type_): dictionary containing map stats for whole team
    Returns:
        _type_: dictionary containing map win rate and total map played
    """
    
    
    #here I should also add a statistic for the total number of matches played by the player
    player_map_stats = {}
    
    limit = 30 # Number of matches to get
    player_detail_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/{game_id}/stats?offset=0&limit={limit}'
    response = requests.get(player_detail_url, headers=headers)
    player_detail = response.json()
    player_matches = player_detail['items']
    for player_match in player_matches:
        match_details = player_match['stats']
        map = match_details['Map']
        result = match_details['Result']
        update_map_stats(map, result, team_map_stats)
        update_map_stats(map, result, player_map_stats)
    calculatedPlayerStats = map_win_ratio_calc(player_map_stats)
    return calculatedPlayerStats



def update_map_stats(map_name, result, map_stats):
    """update the map stats dictionary with the result of the match

    Args:
        map_name (_type_): name/id of the map
        result (_type_): 0/1 for loss/win
        team_map_stats (_type_): dictionary containing map stats for whole team
    """

    # If the map is not already in the dictionary, add it with initial win/loss counts
    if map_name not in map_stats:
        map_stats[map_name] = {'wins': 0, 'losses': 0}
    # Increment the win or loss count based on the result
    if result == '1':  # win = 1, loss = 0
        map_stats[map_name]['wins'] += 1
    else:  
        map_stats[map_name]['losses'] += 1
        
            
def map_win_ratio_calc(map_stats):
    """Calculate the win rate for each map in the map_stats dictionary

    Args:
        map_stats (_type_): dictionary containing map stats for whole team

    Returns:
        _type_: dictionary containing map win rate and total map played
    """
    map_win = {}
    for map_name in map_stats:
        if map_name not in map_win:
            map_win[map_name] = {'win_rate': 0, 'total_map_played': 0}
        wins = map_stats[map_name]['wins']
        losses = map_stats[map_name]['losses']
        total = wins + losses
        if total > 0:
            map_win[map_name]['win_rate'] = float("{:.2f}".format(wins / total * 100))
            map_win[map_name]['total_map_played'] = total
    return map_win


def calculate_team_map_win_rate(teamN_player_stats):
    """calculate the average win rate per map for a team

    Args:
        teamN_player_stats (_type_): _description_

    Returns:
        _type_: _description_
    """
    map_win_rates = {}
    player_count_per_map = {}
    total_map_played = {}
    
    for player, maps in teamN_player_stats.items():
        for map_name, stats in maps.items():
            if map_name not in map_win_rates:
                map_win_rates[map_name] = 0
                player_count_per_map[map_name] = 0
                total_map_played[map_name] = 0
            
            win_rate_percentage = float(stats["win_rate"])
            map_win_rates[map_name] += win_rate_percentage
            total_map_played[map_name] += stats["total_map_played"]
            player_count_per_map[map_name] += 1
    
    # Calculate average win rate per map
    for map_name in map_win_rates:
        map_win_rates[map_name] = {"win_rate": round(map_win_rates[map_name] / player_count_per_map[map_name], 2), "total_map_played":total_map_played[map_name]}
    
    return map_win_rates