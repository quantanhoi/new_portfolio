interface MapDetail {
    win_rate: string;
    total_map_played: number;
}

interface TeamDetail {
    [mapName: string]: MapDetail;
}

export interface MatchDetails {
    [teamName: string]: TeamDetail;
}
