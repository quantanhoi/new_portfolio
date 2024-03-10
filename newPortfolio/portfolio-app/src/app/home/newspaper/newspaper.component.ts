import { Component, OnInit, SimpleChanges, Input } from '@angular/core';
import { NewspaperService } from '../../newspaper.service';

@Component({
  selector: 'app-newspaper',
  templateUrl: './newspaper.component.html',
  styleUrls: ['./newspaper.component.css'],
})
export class NewspaperComponent implements OnInit {
  newspapers: any[] = [];

  constructor(private newspaperService: NewspaperService) {}

  ngOnInit(): void {
    this.newspaperService.getNewspapers().subscribe((data) => {
      this.newspapers = data.filter((article) => article.topic !== 'Code');
    });
  }
  @Input() topic: string = '';

  ngOnChanges(changes: SimpleChanges) {
    if (changes['topic']) {
      this.filterNewspapers(this.topic);
    }
  }

  filterNewspapers(topic: any) {
    this.newspaperService.getNewspapers().subscribe((data) => {
      console.log(topic)
      this.newspapers = data.filter((article) => article.topic == topic.name);
    });
  }
}
