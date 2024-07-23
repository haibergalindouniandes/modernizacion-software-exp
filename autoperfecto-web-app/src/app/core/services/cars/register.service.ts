import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import { Observable } from 'rxjs';
import { Car } from '../../models/cars/car';
import { Response } from '../../models/response/response';


@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  private apiUrl: string = environment.baseUrl + 'crear_automovil';
  private apiKey: string = environment.apiKey;
  private headers = new HttpHeaders({ 'Api-Key': this.apiKey });

  constructor(private http: HttpClient) { }

  registerService(register: Car): Observable<Response> {
    return this.http.post<Response>(this.apiUrl, register, { headers: this.headers });
  }
}
