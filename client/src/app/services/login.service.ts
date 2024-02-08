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
    console.log('body:', body);
    console.log('reached here in services');
    return this.http.post(url, body, options);
  }
}
