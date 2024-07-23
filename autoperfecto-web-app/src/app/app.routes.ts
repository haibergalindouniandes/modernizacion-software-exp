import { Routes } from '@angular/router';
import { NotFoundComponent } from './shared/components/not-found/not-found.component';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./features/auth/auth.routing').then(m => m.AUTH_ROUTES)
  },
  {
    path: 'home',
    loadChildren: () => import('./features/home/home.routing').then(m => m.HOME_ROUTES)
  },
  {
    path: 'cars',
    loadChildren: () => import('./features/cars/cars.routing').then(m => m.CARS_ROUTES)
  },
  {
    path: '**',
    component: NotFoundComponent,
    pathMatch: 'full'
  }
];
