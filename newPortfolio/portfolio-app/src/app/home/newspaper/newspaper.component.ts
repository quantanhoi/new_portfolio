import { Component, OnInit } from '@angular/core';
import { NewspaperService } from '../../newspaper.service';

@Component({
  selector: 'app-newspaper',
  templateUrl: './newspaper.component.html',
  styleUrls: ['./newspaper.component.css']
})
export class NewspaperComponent implements OnInit {
  newspapers: any[] = [];

  constructor(private newspaperService: NewspaperService) { }

  ngOnInit(): void {
    this.newspaperService.getNewspapers().subscribe(data => {
      this.newspapers = data.filter(article => article.topic !== "Code");
    });
  }
}
