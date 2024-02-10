import { Component, NgModule, OnInit } from '@angular/core';

import { AdminEventsService } from '../../services/events.services';
import { Injectable } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DatePipe } from '@angular/common';
import { Event } from '../../models/event.models';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-admin-events',
  standalone: true,
  templateUrl: './admin-events.component.html',
  styleUrls: ['./admin-events.component.css'],
  imports: [CommonModule, FormsModule],
  providers: [DatePipe],
})
export class AdminEventsComponent implements OnInit {
  events: Event[] = [];
  eventName: string = '';
  eventDescription: string = '';

  constructor(
    private adminEventsService: AdminEventsService,
    private datePipe: DatePipe,
    private router: Router
  ) {}

  ngOnInit() {
    //this.generateEvents();
  }

  generateEvents() {
    this.adminEventsService.getEvents().subscribe((events: Object) => {
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

  onSubmitCreateEvent() {
    this.adminEventsService
      .createEvent(this.eventName, this.eventDescription)
      .subscribe((response: any) => {
        if (response.message != 'Event created successfully.') {
          console.error('Error:', response.message);
        } else {
          console.log('Event created:', response.message);
          this.generateEvents();
        }
      });
  }

  onClickEndEvent(eventId: number) {
    this.adminEventsService.endEvent(eventId.toString()).subscribe(
      () => {
        console.log('Event ended successfully.');
        this.router.navigate(['admin-events']);
        // Add any additional logic here
      },
      (error) => {
        console.error('Error ending event:', error);
        // Add any error handling logic here
      }
    );
  }

  navigateToEvent(eventId: number) {
    this.router.navigate(['admin-events', eventId]);
  }
}
