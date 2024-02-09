import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AdminEventsService {
  constructor(private http: HttpClient) {}

  healthCheck() {
    const url = 'http://127.0.0.1:8000/volunteers/';
    return this.http.get(url);
  }

  getEvents(): Observable<Event[]> {
    const url = 'http://127.0.0.1:8000/volunteers/get_events/';
    return this.http.get<Event[]>(url);
  }
}
