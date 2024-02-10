import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css',
})
export class NavbarComponent {
  constructor(private loginService: LoginService, private router: Router) {}

  onClickLogout() {
    this.loginService.adminUserLogout().subscribe((response: any) => {
      console.log('response:', response);
    });
    //redirect to login page
    this.router.navigate(['/']);
  }
}
