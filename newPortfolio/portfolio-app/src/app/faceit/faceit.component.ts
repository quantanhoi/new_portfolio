import { Component } from '@angular/core';
import { PortfolioService } from '../portfolio.service';
import { MatchDetails } from '../models/match-details.model';
@Component({
  selector: 'app-faceit',
  templateUrl: './faceit.component.html',
  styleUrl: './faceit.component.css'
})
export class FaceitComponent {
  matchId = '';
  matchDetails: MatchDetails | null = null;
  constructor(private faceitService: PortfolioService) { }
  onSubmit() {
    this.faceitService.getMatchDetails(this.matchId).subscribe(
      data => {
        this.matchDetails = data;
      },
      error => {
        console.error('Error fetching Faceit data:', error);
      }
    );
  }

  getMapImageUrl(mapName: string): string {
    const map_pool: Array<string> = ['de_ancient', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_anubis', 'de_vertigo'];
    if (!map_pool.includes(mapName)) {
      return 'assets/map_logo/csgo_map.png';
    }
    return `assets/map_logo/${mapName}.png`;
  }

  getWinRateColor(winRate: string): string {
    const rate = parseFloat(winRate);
    if (rate > 50) {
      return 'lightgreen'; 
    } else {
      return 'tomato'; 
    }
  }
  
  

}
