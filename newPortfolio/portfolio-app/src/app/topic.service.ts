import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TopicService {
  private apiUrl: string = 'https://trungthieu1999.social:5000/api/topics';


  constructor(private http: HttpClient) { }

  getTopics(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
