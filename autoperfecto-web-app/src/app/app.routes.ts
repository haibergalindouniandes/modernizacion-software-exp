import { Routes } from '@angular/router';
import { NotFoundComponent } from './shared/components/not-found/not-found.component';
import { AuthGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./features/auth/auth.routing').then(m => m.AUTH_ROUTES)
  },
  {
    path: 'home',
    loadChildren: () => import('./features/home/home.routing').then(m => m.HOME_ROUTES),
    canActivate: [AuthGuard]
  },
  {
    path: 'cars',
    loadChildren: () => import('./features/cars/cars.routing').then(m => m.CARS_ROUTES),
    canActivate: [AuthGuard]
  },
  {
    path: '**',
    component: NotFoundComponent,
    pathMatch: 'full'
  }
];
