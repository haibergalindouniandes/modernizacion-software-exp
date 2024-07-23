import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ToastrService } from 'ngx-toastr';
import { environment } from '../../../../../environments/environment';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Signin } from '../../../../core/models/auth/signin';

@Component({
  selector: 'app-signin-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './signin-form.component.html',
  styleUrl: './signin-form.component.scss'
})
export class SigninFormComponent {

  signInForm!: FormGroup;

  private admonUser: string = environment.admonUser;
  private admonPassWord: string = environment.admonPassWord;
  email: string = '';
  password: string = '';

  constructor(
    private fb: FormBuilder,
    private toastr: ToastrService,
    private router: Router
  ) { }

  signIn(signIn: Signin) {
    sessionStorage.clear();
    let userLogin = new Signin(signIn.email, signIn.password);
    if(userLogin.email == this.admonUser && userLogin.password == this.admonPassWord){
      sessionStorage.setItem('username', this.admonUser);
      this.toastr.success('Confirmación', '¡¡¡ Bienvenido ' + sessionStorage.getItem('username') + ' !!!', { closeButton: true });
      this.router.navigate(['/home'])
    }else{
      this.toastr.error('El usuario o contraseña invalido', 'Error', { closeButton: true });
    }
  }

  ngOnInit() {
    this.signInForm = this.fb.group({
      email: ['', [Validators.required, Validators.email,Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]],
      password: ['', [Validators.required, Validators.minLength(8),Validators.pattern("^(?!.* )(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$")]]
    });
  }
}
