import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { ContactComponent } from './contact/contact.component';
import { CodingComponent } from './coding/coding.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'skills', component: PortfolioComponent },
  { path: 'contacts', component:  ContactComponent},
  { path: 'codings', component: CodingComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
