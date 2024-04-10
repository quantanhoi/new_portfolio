interface MapDetail {
    win_rate: string;
    total_map_played: number;
}


interface mapStatistics {
    [mapName: string]: MapDetail;
}
interface playerStatistics {
    [playerName: string]: playerDetail;
}
interface playerDetail {
    [mapName: string]: MapDetail;
}


interface TeamDetail {
    map_statistics: mapStatistics;
    player_statistics: playerStatistics;
}

export interface MatchDetails {
    [teamName: string]: TeamDetail;
}
