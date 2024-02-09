import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

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
  participantUsername: string;
  userType: string;
  errorMsg: string;

  constructor(private httpClient: HttpClient, private router: Router) {
    this.loginType = 'login';
    this.loginService = new LoginService(httpClient);
    this.healthCheckData = '';
    this.adminUsername = '';
    this.adminPassword = '';
    this.participantUsername = '';
    this.userType = '';
    this.errorMsg = '';
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

  onSubmitAdmin(adminUsername: string, adminPassword: string) {
    console.log('Admin Username:', adminUsername);
    this.loginService
      .adminUserLogin(adminUsername, adminPassword)
      .subscribe((response: any) => {
        if (response.status != 'successfully logged in') {
          this.errorMsg = response.message;
        } else {
          // Handle the response here
          console.log(response);
          this.adminUsername = adminUsername;
          this.userType = 'admin';
          this.router.navigate(['/admin-events']);
        }
      });
  }

  onSubmitParticipant(
    participantUsername: string,
    participantPassword: string
  ) {
    console.log('Participant Username:', participantUsername);
    this.loginService
      .participantUserLogin(participantUsername, 'participant')
      .subscribe((response: any) => {
        if (response.status != 'successfully logged in') {
          this.errorMsg = response.message;
        } else {
          // Handle the response here
          console.log(response);
          this.participantUsername = participantUsername;
          this.userType = 'participant';
          this.router.navigate(['/participant-events']);
        }
      });
  }

  onClickLogout() {
    this.loginService.adminUserLogout().subscribe((response: any) => {
      console.log('response:', response);
    });
    //redirect to login page
    this.router.navigate(['/']);
  }

  // validate() {
  //   this.loginService.validate().subscribe((response: any) => {
  //     console.log('Response:', response);
  //     const { username, user_type } = response;
  //     this.loginType = user_type === 'admin' ? 'admin' : 'participant';
  //     console.log('Username:', username);
  //     console.log('User Type:', user_type);
  //     // if user_type is admin, set adminUsername to username
  //     if (user_type === 'admin') {
  //       this.adminUsername = username;
  //     } else {
  //       this.participantUsername = username;
  //     }
  //     this.userType = user_type;
  //   });
  // }
}
