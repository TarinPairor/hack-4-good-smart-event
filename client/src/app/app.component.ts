import { CommonModule } from '@angular/common';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { RouterOutlet } from '@angular/router';
import { Component, Provider } from '@angular/core'; // Import the missing 'Provider' type
import { HttpClientModule } from '@angular/common/http'; // Import the HttpClientModule
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  providers: [], // Remove provideHttpClient(withFetch()) from the providers array
  imports: [RouterOutlet, CommonModule, HttpClientModule, FormsModule], // Add HttpClientModule to the imports array
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'client';
  a = false;

  toggleA() {
    this.a = !this.a;
  }
}
