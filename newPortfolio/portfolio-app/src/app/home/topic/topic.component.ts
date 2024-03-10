import { Component, OnInit , Output, EventEmitter} from '@angular/core';
import { TopicService } from '../../topic.service';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrl: './topic.component.css'
})


export class TopicComponent implements OnInit{
  topics: any[] = []; 
  constructor(private topicService: TopicService) { }
  ngOnInit(): void {
    this.topicService.getTopics().subscribe(data => {
      this.topics = data;
    });
  }
  @Output() topicSelected = new EventEmitter<any>();

  selectTopic(topic: any) {
    this.topicSelected.emit(topic);
  }
  
}
