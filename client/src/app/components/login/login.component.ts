import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loginType: string;
  loginService: LoginService;
  healthCheckData: Object;
  adminUsername: string;
  adminPassword: string;

  constructor(private httpClient: HttpClient) {
    this.loginType = 'login';
    this.loginService = new LoginService(httpClient);
    this.healthCheckData = '';
    this.adminUsername = '';
    this.adminPassword = '';
  }

  ngOnInit() {
    this.healthCheck();
  }

  toggleLoginForm(type: string) {
    this.loginType = type;
    console.log('loginType is now:', this.loginType);
  }

  healthCheck() {
    this.loginService.healthCheck().subscribe((data: any) => {
      this.healthCheckData = data.message;
      console.log('Data:', this.healthCheckData);
    });
  }

  onSubmit(adminUsername: string, adminPassword: string) {
    console.log('Admin Username:', adminUsername);
    console.log('Admin Password:', adminPassword);
    this.loginService
      .adminUserLogin(adminUsername, adminPassword)
      .subscribe((response: any) => {
        // Handle the response here
        console.log('response');
        console.log(response);
      });
  }
}
