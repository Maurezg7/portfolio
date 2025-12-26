import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { Observable, of } from "rxjs";
import { project } from "../models/project";

@Injectable({
  providedIn: 'root',
})
export class ProjectService{
  private http = inject(HttpClient);

  private projectsUrl = '/data/projects.json';
  private cachedProjects: project[] | null = null;

  getProjectList(): Observable<project[]> {
    if (this.cachedProjects) {
      return of(this.cachedProjects);
    }

    return this.http.get<project[]>(this.projectsUrl);
  }

  // getProjectById(id: number): Observable<project | undefined> {
  //   return new Observable(observer => {
  //     this.getProjectList().subscribe(projects => {
  //       const project = projects.find(p => p.id === id);
  //       observer.next(project);
  //       observer.complete();
  //     });
  //   });
  // }
}
