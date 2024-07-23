import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import { Observable } from 'rxjs';
import { Car } from '../../models/cars/car';

@Injectable({
  providedIn: 'root'
})
export class ListService {

  private apiUrl: string = environment.baseUrl + 'listar_automoviles';
  private apiKey: string = environment.apiKey;
  private headers = new HttpHeaders({ 'Api-Key': this.apiKey });

  constructor(private http: HttpClient) { }

  getCars(): Observable<Car[]> {
    return this.http.get<Car[]>(`${this.apiUrl}`, { headers: this.headers });
  }

}
