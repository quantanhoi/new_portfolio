import { Component, OnInit, OnChanges, SimpleChanges, Input, AfterViewInit } from '@angular/core';
import { NewspaperService } from '../../newspaper.service';
import Swiper from 'swiper';

@Component({
  selector: 'app-newspaper',
  templateUrl: './newspaper.component.html',
  styleUrls: ['./newspaper.component.css'],
})
export class NewspaperComponent implements OnInit, OnChanges {
  //declare the attributes that will be used in the html files
  newspapers: any[] = [];
  @Input() topic: string = '';

  constructor(private newspaperService: NewspaperService) {}


  //call load newspaper on initialization
  ngOnInit(): void {
    this.loadNewspapers();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['topic'] && !changes['topic'].isFirstChange()) {
      this.filterNewspapers(this.topic);
    }
  }

  //calling service to load newspaper with api url
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
