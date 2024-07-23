import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { Car } from '../../models/cars/car';

@Injectable({
  providedIn: 'root'
})
export class ShraredListDetailService {

  private dataCarService = new Subject<Car>();

  constructor() { }

  getDataService(): Observable<Car> {
    return this.dataCarService.asObservable();
  }

  setDataService(dataService: Car) {
    this.dataCarService.next(dataService);
  }
}
