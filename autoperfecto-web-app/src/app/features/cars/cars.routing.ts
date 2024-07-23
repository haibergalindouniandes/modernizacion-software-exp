import { Routes } from '@angular/router';
import { ListComponent } from './pages/list/list.component';
import { RegisterComponent } from './pages/register/register.component';


export const CARS_ROUTES: Routes = [
  {
    path: 'list-detail-cars', component: ListComponent
  },
  {
    path: 'register', component: RegisterComponent
  },
];
