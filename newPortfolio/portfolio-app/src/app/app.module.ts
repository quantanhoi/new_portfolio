import { NgModule, isDevMode } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

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

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NewspaperComponent,
    TopicComponent,
    FirstImageComponent,
    PortfolioComponent,
    ContactComponent,
    CodingComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: !isDevMode(),
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
