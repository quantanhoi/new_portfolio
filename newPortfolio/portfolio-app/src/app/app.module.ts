import { NgModule, isDevMode, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from'@angular/material/menu';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NewspaperComponent } from './home/newspaper/newspaper.component';
import { HttpClientModule} from '@angular/common/http';
import { TopicComponent } from './home/topic/topic.component';
import { FirstImageComponent } from './home/newspaper/first-image/first-image.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { ContactComponent } from './contact/contact.component';
import { CodingComponent } from './coding/coding.component';
import { FaceitComponent } from './faceit/faceit.component';
import { NavbarComponent } from './navbar/navbar.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NewspaperComponent,
    TopicComponent,
    FirstImageComponent,
    PortfolioComponent,
    ContactComponent,
    CodingComponent,
    FaceitComponent,
    NavbarComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: !isDevMode(),
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    }),
    BrowserAnimationsModule,
    MatButtonModule,
    MatMenuModule,
    
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
