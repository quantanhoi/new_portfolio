import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NewspaperComponent } from './home/newspaper/newspaper.component';
import { HttpClientModule} from '@angular/common/http';
import { TopicComponent } from './home/topic/topic.component';
import { FirstImageComponent } from './home/newspaper/first-image/first-image.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NewspaperComponent,
    TopicComponent,
    FirstImageComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
