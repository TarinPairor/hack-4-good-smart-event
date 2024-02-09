import { Component, OnInit } from '@angular/core';
import { AdminEventsService } from '../../services/events.services';
import { Injectable } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DatePipe } from '@angular/common';
import { Event } from '../../models/event.models';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-participant-events',
  standalone: true,
  templateUrl: './participant-events.component.html',
  styleUrls: ['./participant-events.component.css'],
  imports: [CommonModule],
  providers: [DatePipe],
})
export class ParticipantEventsComponent implements OnInit {
  events: Event[] = [];

  constructor(
    private participantEventsService: AdminEventsService,
    private datePipe: DatePipe,
    private router: Router
  ) {}

  ngOnInit() {
    //this.generateEvents();
  }

  generateEvents() {
    this.participantEventsService
      .getCurrentEvents()
      .subscribe((events: Object) => {
        this.events = events as Event[];
        this.events.forEach((event) => {
          const transformedStartDate = this.datePipe.transform(
            event.start_date,
            'short'
          );
          const transformedEndDate = this.datePipe.transform(
            event.end_date,
            'short'
          );

          if (transformedStartDate) {
            event.start_date = transformedStartDate;
          }

          if (transformedEndDate) {
            event.end_date = transformedEndDate;
          }
        });
      });
  }

  navigateToEvent(eventId: number) {
    this.router.navigate(['participant-events', eventId]);
  }
}
