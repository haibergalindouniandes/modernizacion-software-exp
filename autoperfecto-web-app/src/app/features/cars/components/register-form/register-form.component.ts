import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ToastrService } from 'ngx-toastr';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { RegisterService } from '../../../../core/services/cars/register.service';
import { Car } from '../../../../core/models/cars/car';

@Component({
  selector: 'app-register-form',
  standalone: true,
  imports: [CommonModule, RegisterFormComponent, ReactiveFormsModule, FormsModule],
  templateUrl: './register-form.component.html',
  styleUrl: './register-form.component.scss'
})
export class RegisterFormComponent {

  serviceRegistrationForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    public toastr: ToastrService,
    private service: RegisterService,
  ) { }

  ngOnInit() {
    this.serviceRegistrationForm = this.fb.group({
      marca: ['', [Validators.required, Validators.minLength(6)]],
      placa: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(7)]],
      modelo: ['', [Validators.required, Validators.minLength(4)]],
      kilometraje: [0, [Validators.required, Validators.min(0)]],
      color: ['', [Validators.required, Validators.minLength(4)]],
      cilindraje: ['', [Validators.required, Validators.minLength(2)]],
      tipo_combustible: ['', [Validators.required, Validators.minLength(6)]],
      vendido: ['', Validators.required],
      valor_venta: [0, [Validators.required, Validators.min(0)]],
      kilometraje_venta: [0, [Validators.required, Validators.min(0)]]
    });
  }

  registerService() {
    if (this.serviceRegistrationForm.valid) {
      let data = this.serviceRegistrationForm.value;
      let registerService = new Car(
        data.marca,
        data.placa,
        data.modelo,
        data.kilometraje,
        data.color,
        data.cilindraje,
        data.tipo_combustible,
        data.vendido === 'Si',
        data.valor_venta,
        data.kilometraje_venta
      );
      this.service.registerService(registerService)
        .subscribe(registerSucess => {
          this.toastr.success('Confirmation', 'Se registro automovil exitosamente!', { closeButton: true });
          this.cancel();
        })
    }
  }

  cancel() {
    this.serviceRegistrationForm.reset({
      kilometraje: 0,
      valor_venta: 0,
      kilometraje_venta: 0
    });
  }

}
