import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SurveyServices } from '../../services/survey.services';
import { AttendanceService } from '../../services/attendance.services';
import { Attendance } from '../../models/attendance.models';
import { Survey } from '../../models/survey.model';
import { CommonModule } from '@angular/common';
import { DatePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
  providers: [DatePipe],
})
export class DashboardComponent {
  eventId: string = '';
  averageTimeSpent: string = '';
  aiResponse: string = '';
  attendances: Attendance[] = [];
  createSurveyData: any = null;
  surveys: Survey[] = [];

  data = JSON.stringify({
    name: 'Sample Survey',
    description: 'This is a sample survey',
    questions: [
      {
        question: 'How did you find the event?',
        question_type: 'text',
      },
      {
        question: 'Rate the event from 1 to 5.',
        question_type: 'choice',
        choices: ['1', '2', '3', '4', '5'],
      },
    ],
  });

  constructor(
    private route: ActivatedRoute,
    private datePipe: DatePipe,
    private surveyServices: SurveyServices,
    private attendanceService: AttendanceService
  ) {}

  ngOnInit() {
    this.eventId = this.route.snapshot.paramMap.get('event_id')!;
  }

  getAverageTimeSpentFromParticipantsWithEventId(eventId: string) {
    this.surveyServices
      .getAverageTimeSpentFromParticipantsWithEventId(eventId)
      .subscribe((response) => {
        console.log('Response:', response);
        // Handle the response here {"average_time_spent": "0:00:04.954464"}
        this.averageTimeSpent = response.average_time_spent;
      });
  }

  chabotResponseWithQuestionId(eventId: string) {
    this.surveyServices
      .chabotResponseWithQuestionId(eventId)
      .subscribe((response) => {
        this.aiResponse = response.message;
      });
  }
  //mention how its secure
  getParticipantsWithEventId(eventId: string) {
    this.attendanceService.getAttendancesWithEventId(eventId).subscribe(
      (response) => {
        this.attendances = response.map((attendance: Attendance) => {
          let checkInTime = attendance.check_in_time;
          let checkOutTime = attendance.check_out_time;

          // Check if the times can be parsed by the Date constructor
          if (checkInTime !== null && isNaN(new Date(checkInTime).getTime())) {
            console.error('Invalid check-in time:', checkInTime);
          } else {
            checkInTime = this.datePipe.transform(checkInTime, 'short') || '';
          }

          if (
            checkOutTime !== null &&
            isNaN(new Date(checkOutTime).getTime())
          ) {
            console.error('Invalid check-out time:', checkOutTime);
          } else {
            checkOutTime =
              checkOutTime !== null
                ? this.datePipe.transform(checkOutTime, 'short')
                : '';
          }

          return {
            ...attendance,
            check_in_time: checkInTime,
            check_out_time: checkOutTime,
          };
        });
      },
      (error) => {
        console.error('Error getting participants:', error);
      }
    );
  }

  // change later
  onSubmitCreateSurvey() {
    try {
      const createSurveyData = JSON.parse(this.createSurveyData);
      this.surveyServices
        .createSurvey(this.eventId, createSurveyData)
        .subscribe((response) => {
          console.log('Survey created:', response);
          this.createSurveyData = '';
          location.reload();
        });
    } catch (error) {
      console.error('Invalid JSON:', error);
    }
  }

  onClickGetSurveysUnderEventId(eventId: string) {
    this.surveyServices
      .getSurveysUnderEventId(eventId)
      .subscribe((surveys: any[]) => {
        this.surveys = surveys;
        console.log('Surveys:', this.surveys);
      });
    console.log('Surveys:', this.surveys);
  }
}
