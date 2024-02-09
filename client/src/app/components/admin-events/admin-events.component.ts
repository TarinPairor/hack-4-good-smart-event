import { Component, OnInit } from '@angular/core';

import { AdminEventsService } from '../../services/events.services';
import { Injectable } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DatePipe } from '@angular/common';
import { Event } from '../../models/event.models';

@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-admin-events',
  standalone: true,
  templateUrl: './admin-events.component.html',
  styleUrls: ['./admin-events.component.css'],
  imports: [CommonModule],
  providers: [DatePipe],
})
export class AdminEventsComponent implements OnInit {
  events: Event[] = [];

  constructor(
    private adminEventsService: AdminEventsService,
    private datePipe: DatePipe
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
}
