import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TopicService {
  private apiUrl: string = 'http://16.171.182.163:5000/api/topics';


  constructor(private http: HttpClient) { }

  getTopics(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
