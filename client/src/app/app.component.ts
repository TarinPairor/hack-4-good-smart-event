import { CommonModule } from '@angular/common';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { RouterOutlet } from '@angular/router';
import { Component, Provider } from '@angular/core'; // Import the missing 'Provider' type
import { HttpClientModule } from '@angular/common/http'; // Import the HttpClientModule
import { FormsModule } from '@angular/forms';
import { NavbarComponent } from './components/navbar/navbar.component';
import { LoginService } from './services/login.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  providers: [], // Add HttpClientModule to the imports array
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [
    RouterOutlet,
    CommonModule,
    HttpClientModule,
    FormsModule,
    NavbarComponent,
  ],
})
export class AppComponent {
  title = 'client';
  a = false;

  constructor() {}
}
