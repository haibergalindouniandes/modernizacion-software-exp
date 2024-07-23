import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Car } from '../../../../core/models/cars/car';
import { ListService } from '../../../../core/services/cars/list.service';
import { switchMap } from 'rxjs';
import { ShraredListDetailService } from '../../../../core/services/cars/shrared-list-detail.service';

@Component({
  selector: 'app-list-table',
  standalone: true,
  imports: [CommonModule, ListTableComponent],
  templateUrl: './list-table.component.html',
  styleUrl: './list-table.component.scss'
})
export class ListTableComponent {

  carsList: Array<Car> = [];
  selectedCar: Car | undefined;

  constructor(
    public toastr: ToastrService,
    private carsListService: ListService,
    private listDetailSharedService: ShraredListDetailService
  ) { }

  ngOnInit() {
    this.getCars();
  }

  getCars() {
    this.carsList = [];
    this.carsListService.getCars()
      .pipe(
        switchMap(listCarsSuccess => {
          this.carsList = listCarsSuccess;
          return [];
        })
      )
      .subscribe(() => { });
  }

  onSelectedCar(car: Car): void {
    this.selectedCar = car;
    this.sendDataSharedService(this.selectedCar);
  }

  sendDataSharedService(car: Car) {
    this.listDetailSharedService.setDataService(car);
  }

}
