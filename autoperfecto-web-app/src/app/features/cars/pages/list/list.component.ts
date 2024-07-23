import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ListTableComponent } from '../../components/list-table/list-table.component';
import { HeaderComponent } from '../../../../shared/components/header/header.component';
import { FooterComponent } from '../../../../shared/components/footer/footer.component';
import { DetailCardComponent } from '../../components/detail-card/detail-card.component';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, ListComponent, HeaderComponent, FooterComponent, ListTableComponent, DetailCardComponent],
  templateUrl: './list.component.html',
  styleUrl: './list.component.scss'
})
export class ListComponent {

}
