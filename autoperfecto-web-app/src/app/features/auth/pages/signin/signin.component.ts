import { Component } from '@angular/core';
import { FooterComponent } from '../../../../shared/components/footer/footer.component';
import { HeaderComponent } from '../../../../shared/components/header/header.component';
import { SigninFormComponent } from '../../components/signin-form/signin-form.component';
import { SigninCardComponent } from '../../components/signin-card/signin-card.component';

@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [HeaderComponent, FooterComponent, SigninFormComponent, SigninCardComponent],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.scss'
})
export class SigninComponent {

}
