import { Component, Input ,OnInit } from '@angular/core';
import { FirstImageService } from '../../../first-image.service';

@Component({
  selector: 'app-first-image',
  templateUrl: './first-image.component.html',
  styleUrl: './first-image.component.css'
})

export class FirstImageComponent implements OnInit {
  
  @Input() newspaperUrl: string = '';
  imageUrl: string = '';

  constructor(private firstImageService: FirstImageService) { }

  ngOnInit(): void {
    this.getFirstImage(this.newspaperUrl);
  }

  getFirstImage(url: string): void {
    this.firstImageService.getFirstImage(url)
      .subscribe(response => {
        this.imageUrl = response.imageUrl;
      });
  }
}
