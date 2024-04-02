import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { ContactComponent } from './contact/contact.component';
import { CodingComponent } from './coding/coding.component';
import { FaceitComponent } from './faceit/faceit.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'skills', component: PortfolioComponent },
  { path: 'contacts', component:  ContactComponent},
  { path: 'codings', component: CodingComponent},
  { path: 'faceit', component: FaceitComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
