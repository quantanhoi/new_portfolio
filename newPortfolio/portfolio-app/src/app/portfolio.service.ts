import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, forkJoin, of } from 'rxjs';
import { catchError, map, mergeMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PortfolioService {
  private apiUrl: string = 'http://127.0.0.1:5000/api/';
  private project: string = 'http://127.0.0.1:5000/api/projects';
  private githubApiUrl: string = 'https://api.github.com/repos/';

  constructor(private http: HttpClient) { }
  getSkills(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}skills`);
  }

  getProjects(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}projects`);
  }
  getGitHubProjectDetails(repoPath: string): Observable<any> {
    return this.http.get(`${this.githubApiUrl}${repoPath}`).pipe(
      catchError(error => {
        console.error('Error fetching GitHub data:', error);
        return of(null); // Return null or default object if GitHub API fails
      })
    );
  }

  getEnhancedProjects(): Observable<any[]> {
    return this.getProjects().pipe(
      mergeMap(projects => forkJoin(
        projects.map(project => {
          const url = new URL(project.url);
          const repoPath = url.pathname.substring(1); // Remove the leading slash
          return this.getGitHubProjectDetails(repoPath).pipe(
            map(githubData => ({
              ...project,
              description: githubData ? githubData.description : 'Description not available.'
            }))
          );
        })
      ))
    );
  }
}
