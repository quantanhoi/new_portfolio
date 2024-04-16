import { Component, OnInit } from '@angular/core';
import {PortfolioService} from '../portfolio.service';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrl: './portfolio.component.css'
})
export class PortfolioComponent {
  skills: any[] = [];
  projects: any[] = [];
  
  constructor(private portfolioService: PortfolioService) { }
  ngOnInit(): void {
    this.portfolioService.getSkills().subscribe(data => {
      this.skills = data});

    this.portfolioService.getEnhancedProjects().subscribe(data => {
      this.projects = data});
  }
  getProjectImage(project_img: string): string {
    return `assets/project_icons/${project_img}`;
  }
}
