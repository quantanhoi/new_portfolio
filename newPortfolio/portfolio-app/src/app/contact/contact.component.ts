import { Component, OnInit } from '@angular/core';
import { PortfolioService } from '../portfolio.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.css'
})
export class ContactComponent {
  contacts: any[] = [];
  constructor(private portfolioService: PortfolioService) { }
  ngOnInit(): void {
    this.portfolioService.getContacts().subscribe(data => {
      this.contacts = data;
    });
  }
}
