import { Component, inject } from '@angular/core';
import { project } from '../../models/project';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'app-projects',
  imports: [],
  templateUrl: './projects.html',
  styleUrl: './projects.scss',
})
export class Projects {
  project: project[] = [];
  private projectService = inject(ProjectService);

  ngOnInit() {
    this.getProjects();
  }

  private getProjects(): void {
    this.projectService.getProjectList().subscribe({
      next: (data) => {
        this.project = data;
      },
      error: (error) => {
        console.error('Error when obtaining the projects: ', error);
      },
    });
  }
}
