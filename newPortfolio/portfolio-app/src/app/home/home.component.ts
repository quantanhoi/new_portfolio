import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  selectedTopic: string = '';
  onTopicSelected(topic: string) {
    this.selectedTopic = topic;
  }
}
