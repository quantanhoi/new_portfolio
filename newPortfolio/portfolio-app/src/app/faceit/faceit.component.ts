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
  map_pool: Array<string> = ['de_ancient', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_anubis', 'de_vertigo'];
  //for loading spinner
  isLoading: boolean = false;
  //for collapsable player details
  // expandedPlayer: string | null = null;
  // togglePlayer(key: string): void {
  //   this.expandedPlayer = this.expandedPlayer === key ? null : key;
  // }

  constructor(private faceitService: PortfolioService) { }
  onSubmit() {
    this.isLoading = true;
    this.faceitService.getMatchDetails(this.matchId).subscribe(
      data => {
        this.matchDetails = data;
        this.isLoading = false;
        console.log('Faceit data:', data);
      },
      error => {
        console.error('Error fetching Faceit data:', error);
      }
    );
  }

  getMapImageUrl(mapName: string): string {
    if (!this.map_pool.includes(mapName)) {
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
