import { Routes } from '@angular/router';
import { SigninComponent } from './pages/signin/signin.component';


export const AUTH_ROUTES: Routes = [
  { path: '', component: SigninComponent },
  { path: 'signin', component: SigninComponent },

];
