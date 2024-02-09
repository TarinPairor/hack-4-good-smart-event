import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AttendanceService {
  constructor(private http: HttpClient) {}

  checkIn(eventId: string): Observable<any> {
    let params = new HttpParams().set('event_id', eventId);
    return this.http.get('http://127.0.0.1:8000/volunteers/check_in/', {
      params: params,
    });
  }

  //add?p=Part
  checkOut(eventId: string): Observable<any> {
    let params = new HttpParams().set('event_id', eventId);
    return this.http.get('http://127.0.0.1:8000/volunteers/check-out', {
      params: params,
    });
  }
  //   checkOut(eventId: string): Observable<any> {
  //     return this.http.post('http://127.0.0.1:8000/volunteers/check-out', {
  //       event_id: eventId,
  //     });
  //   }

  getTimeSpentAtEventFromParticipant(
    eventId: string,
    participantUsername: string
  ): Observable<any> {
    return this.http.get(
      'http://127.0.0.1:8000/volunteers/get_time_spent_at_event_from_participant',
      { params: { event_id: eventId, p: participantUsername } }
    );
  }
}
