import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(private http: HttpClient) {}

  healthCheck() {
    const url = 'http://127.0.0.1:8000/volunteers/';
    return this.http.get(url);
  }

  adminUserLogin(username: string, password: string) {
    const url = 'http://127.0.0.1:8000/volunteers/admin_user_login/';
    const body = { username, password };
    const options = { withCredentials: true };

    return this.http.post(url, body, options);
  }

  adminUserLogout() {
    const url = 'http://127.0.0.1:8000/volunteers/admin_user_logout/';
    return this.http.post(url, null, { withCredentials: true });
  }

  participantUserLogin(username: string, password: string) {
    const url = 'http://127.0.0.1:8000/volunteers/participant_user_login/';
    const body = { username, password };
    const options = { withCredentials: true };
    return this.http.post(url, body, options);
  }

  // validate() {
  //   const url = 'http://127.0.0.1:8000/volunteers/validate/';
  //   const csrfToken = this.cookieService.get('csrftoken');
  //   console.log('CSRF Token:', csrfToken); // Print the CSRF token
  //   return this.http.get(url, { withCredentials: true }).pipe(
  //     catchError((error) => {
  //       console.error('Error:', error);
  //       return throwError(error);
  //     })
  //   );
  // }
}
