import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { ToastrService } from 'ngx-toastr';

@Injectable()
export class HttpErrorInterceptor implements HttpInterceptor {
  constructor(
    private toastr: ToastrService
  ) { }

  intercept(req: HttpRequest<any>, next: HttpHandler) {
    return next.handle(req).pipe(
      catchError((err: any) => {
        let errorMesagge = '';
        let errorType = '';
        if (err instanceof ErrorEvent) {
          errorType = "Error del lado del cliente"
          errorMesagge = `${err.error}: ${err.message}`;
          this.toastr.error(errorMesagge, errorType, { closeButton: true });
        } else {
          errorType = "Error del lado del servidor"
          errorMesagge = `${err.status}: ${err.error.message}`;
          this.toastr.error(errorMesagge, errorType, { closeButton: true });
          if (err.status == 401) {
            this.redirectToLogin();
          }
        }
        return throwError(() => err);
      })
    );
  }

  redirectToLogin(): void {
    const newPath = `/auth/signin`;
    window.location.href = newPath
  }

}
