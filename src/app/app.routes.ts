import { Routes } from '@angular/router';
import { About } from './pages/about/about';
import { Skills } from './pages/skills/skills';
import { Projects } from './pages/projects/projects';
import { Contact } from './pages/contact/contact';
import { Presentation } from './pages/presentation/presentation';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./app').then((m) => m.App),
    children: [
      { path: '', component: Presentation },
      { path: 'about', component: About },
      { path: 'skills', component: Skills },
      { path: 'projects', component: Projects },
      { path: 'contact', component: Contact },
    ],
  },
  { path: '**', redirectTo: '' },
];
