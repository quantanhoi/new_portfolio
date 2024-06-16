import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class FirstImageService {
  private apiUrl: string = 'https://trungthieu1999.social:5000/api/get-first-image';

  constructor(private http: HttpClient) { }

  getFirstImage(url: string): Observable<{imageUrl: string}> {
    return this.http.post<{imageUrl: string}>(this.apiUrl, { url }).pipe(
      catchError(() => of({ imageUrl: '/assets/newspaper-placeholder.png' }))
    );
  }
}
