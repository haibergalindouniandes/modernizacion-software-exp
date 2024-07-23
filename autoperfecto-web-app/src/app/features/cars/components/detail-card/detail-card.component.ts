import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Car } from '../../../../core/models/cars/car';
import { ShraredListDetailService } from '../../../../core/services/cars/shrared-list-detail.service';

@Component({
  selector: 'app-detail-card',
  standalone: true,
  imports: [CommonModule, DetailCardComponent],
  templateUrl: './detail-card.component.html',
  styleUrl: './detail-card.component.scss'
})
export class DetailCardComponent {

  selectedCar: Car | undefined;

  constructor(
    private listDetailSharedService: ShraredListDetailService
  ) { }

  ngOnInit() {
    this.listDetailSharedService.getDataService().subscribe(data => {
      this.selectedCar = data;
    });

  }

}
