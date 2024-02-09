import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AttendanceService } from '../../services/attendance.services';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-event-participation',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-participation.component.html',
  styleUrl: './event-participation.component.css',
})
export class EventParticipationComponent {
  eventId: string = '';
  showOptions: boolean = false;
  toggle: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private attendanceService: AttendanceService
  ) {}

  ngOnInit() {
    this.eventId = this.route.snapshot.paramMap.get('event_id')!;
  }

  onClickCheckIn(eventId: string) {
    this.attendanceService.checkIn(eventId).subscribe(
      () => {
        this.toggle = !this.toggle;
        this.showOptions = true;
        console.log('Checked in successfully');
      },
      (error) => {
        console.error('Error during check in:', error);
      }
    );
  }

  onClickCheckOut(eventId: string) {
    this.attendanceService.checkOut(eventId).subscribe(
      () => {
        this.toggle = !this.toggle;
        this.showOptions = false;
        console.log('Checked out successfully');
      },
      (error) => {
        console.error('Error during check out:', error);
      }
    );
  }
}
