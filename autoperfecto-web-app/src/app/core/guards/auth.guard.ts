import { CanActivate, Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private toastr: ToastrService, private router: Router) {}

  canActivate(): boolean {
    if (sessionStorage.getItem('username') !== null) {
      return true;
    } else {
      this.toastr.error('Para acceder a este recurso debe iniciar sesión', 'No autorizado', { closeButton: true });
      this.router.navigate(['/']);
      return false;
    }
  }
}
