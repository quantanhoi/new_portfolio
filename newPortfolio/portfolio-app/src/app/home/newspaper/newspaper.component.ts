import { Component, OnInit, OnChanges, SimpleChanges, Input, AfterViewInit } from '@angular/core';
import { NewspaperService } from '../../newspaper.service';
import Swiper from 'swiper';

@Component({
  selector: 'app-newspaper',
  templateUrl: './newspaper.component.html',
  styleUrls: ['./newspaper.component.css'],
})
export class NewspaperComponent implements OnInit, OnChanges, AfterViewInit {
  newspapers: any[] = [];
  @Input() topic: string = '';

  constructor(private newspaperService: NewspaperService) {}

  ngOnInit(): void {
    this.loadNewspapers();
  }

  ngAfterViewInit(): void {
    const swiper = new Swiper('.swiper-container', {
      loop: true,
      navigation: true,
      autoHeight: true,
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        640: {
          slidesPerView: 2,
          spaceBetween: 20
        }
      }
    });
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['topic'] && !changes['topic'].isFirstChange()) {
      this.filterNewspapers(this.topic);
    }
  }

  loadNewspapers(): void {
    this.newspaperService.getNewspapers().subscribe((data) => {
      this.newspapers = data.filter((article) => article.topic !== 'Code');
      if (this.topic) {
        this.filterNewspapers(this.topic);
      }
    });
  }

  filterNewspapers(topic: string): void {
    this.newspaperService.getNewspapers().subscribe((data) => {
      this.newspapers = data.filter((article) => article.topic === topic);
    });
  }
}
