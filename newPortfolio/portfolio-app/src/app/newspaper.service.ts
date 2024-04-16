import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewspaperService {
  private apiUrl: string = 'https://trungthieu1999.social:5000/api/newspapers';

  constructor(private http: HttpClient) { }

  getNewspapers(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
