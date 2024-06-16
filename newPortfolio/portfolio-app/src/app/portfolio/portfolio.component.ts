import { Component, OnInit } from '@angular/core';
import {PortfolioService} from '../portfolio.service';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrl: './portfolio.component.css'
})
export class PortfolioComponent {
  skills: any[] = [
    { name: 'C/C++', imgSrc: 'assets/project_icons/C++.png' },
    { name: 'JavaScript', imgSrc: 'assets/project_icons/Javascript.png' },
    { name: 'Typescript', imgSrc: 'assets/project_icons/Typescript.png' },
    { name: 'Python', imgSrc: 'assets/project_icons/Python.png' },
    { name: 'Java', imgSrc: 'assets/project_icons/Java.png' },
    { name: 'R', imgSrc: 'assets/project_icons/R.png' },
    { name: 'HTML', imgSrc: 'assets/project_icons/HTML.png' },
    { name: 'CSS', imgSrc: 'assets/project_icons/CSS.png' },
    { name: 'Postgresql', imgSrc: 'assets/project_icons/Postgresql.png' },
    { name: 'MySQL', imgSrc: 'assets/project_icons/Mysql.png' },
    { name: 'MongoDB', imgSrc: 'assets/project_icons/MongoDB.png' },
    { name: 'Angular', imgSrc: 'assets/project_icons/Angular.png' },
    { name: 'React', imgSrc: 'assets/project_icons/React.png' },
    { name: 'Node.js', imgSrc: 'assets/project_icons/node.js.png' },
    { name: 'Flask', imgSrc: 'assets/project_icons/Flask.png' },
    { name: 'AWS', imgSrc: 'assets/project_icons/AWS.png' },
    { name: 'Docker', imgSrc: 'assets/project_icons/Docker.png' },
    { name: 'Git', imgSrc: 'assets/project_icons/Git.png' },
    { name: 'KNIME', imgSrc: 'assets/project_icons/KNIME.png' },
    { name: 'PowerBI', imgSrc: 'assets/project_icons/PowerBI.png' },
    { name: 'Trello', imgSrc: 'assets/project_icons/Trello.png' },
    
  ];
  projects: any[] = [];
  
  constructor(private portfolioService: PortfolioService) { }
  ngOnInit(): void {
    this.portfolioService.getEnhancedProjects().subscribe(data => {
      this.projects = data});
  }
  getProjectImage(project_img: string): string {
    return `assets/project_icons/${project_img}`;
  }
}
