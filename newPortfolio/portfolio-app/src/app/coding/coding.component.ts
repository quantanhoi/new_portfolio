import { Component, OnInit } from '@angular/core';
import { NewspaperService } from '../newspaper.service';

@Component({
  selector: 'app-coding',
  templateUrl: './coding.component.html',
  styleUrl: './coding.component.css'
})
export class CodingComponent implements OnInit {
  codingArticle: any[] = []; 
  constructor(private newspaperService: NewspaperService) {}
  ngOnInit(): void {
    this.newspaperService.getNewspapers().subscribe((data) => {
      this.codingArticle = data.filter((article) => article.topic == 'Code');
    });
  }
}
