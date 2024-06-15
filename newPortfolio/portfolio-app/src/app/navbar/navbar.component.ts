import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { TopicService } from '../topic.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent implements OnInit {
  topics: any[] = [];
  @Output() topicSelected = new EventEmitter<any>();
  constructor(private topicService: TopicService, private router: Router) {}


  navigateTo(route: string) {
    this.router.navigate([route]);
  }

  ngOnInit(): void {
      this.topicService.getTopics().subscribe(data => {
        this.topics = data.filter(topic => topic.name !== 'Code');
      });
  }

  selectTopic(topic: any) {
    this.router.navigate(['/home', {topic: topic.name}]);
  }

}
