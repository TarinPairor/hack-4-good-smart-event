import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AttendanceService } from '../../services/attendance.services';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { SurveyServices } from '../../services/survey.services';
import { Survey } from '../../models/survey.model';
import { Question } from '../../models/question.models';
import { FormsModule } from '@angular/forms';
import { switchMap, map } from 'rxjs/operators';
import { from } from 'rxjs';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-event-participation',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './event-participation.component.html',
  styleUrl: './event-participation.component.css',
})
export class EventParticipationComponent {
  eventId: string = '';
  questions: any[] = [];
  surveys: Survey[] = [];
  toggle: boolean = true;

  constructor(
    private route: ActivatedRoute,
    private attendanceService: AttendanceService,
    private surveyService: SurveyServices,
    private router: Router
  ) {}

  ngOnInit() {
    this.eventId = this.route.snapshot.paramMap.get('event_id')!;
  }

  onClickCheckIn(eventId: string) {
    this.toggle = !this.toggle;
    this.attendanceService.checkIn(eventId).subscribe(
      () => {
        console.log('Checked in successfully');
      },
      (error) => {
        console.error('Error during check in:', error);
      }
    );
  }

  onClickCheckOut(eventId: string) {
    this.router.navigate(['/']);
    this.attendanceService.checkOut(eventId).subscribe(
      () => {
        console.log('Checked out successfully');
      },
      (error) => {
        console.error('Error during check out:', error);
      }
    );
  }

  onClickGetSurveysUnderEventId(eventId: string) {
    this.surveyService
      .getSurveysUnderEventId(eventId)
      .subscribe((surveys: any[]) => {
        this.surveys = surveys;
        console.log('Surveys:', this.surveys);
      });
    console.log('Surveys:', this.surveys);
  }

  onClickGetQuestionsAndIds(surveyId: string) {
    this.surveyService
      .getQuestionsFromSurveyId(surveyId)
      .subscribe((ids: string[]) => {
        ids.forEach((id: string) => {
          this.surveyService
            .getSurveyQuestionWithQuestionId(id)
            .subscribe((question: Question[]) => {
              this.questions.push(question);
              console.log('Questions:', this.questions);
            });
        });
      });
  }

  currentAnswers: { [questionId: number]: string } = {};

  onSubmitQuestions() {
    from(this.questions)
      .pipe(
        switchMap((question) => {
          console.log('Answer:', this.currentAnswers[question.question_id]); // Log the answer
          return this.surveyService.answerSurveyQuestionWithQuestionId(
            question.question_id,
            this.currentAnswers[question.question_id]
          );
        }),
        tap(() => {
          // Clear currentAnswers
          this.currentAnswers = {};
        })
      )
      .subscribe(
        () => {
          console.log('Question answered successfully');
          location.reload(); // Reload the page
        },
        (error) => console.error('Error during answering question:', error)
      );
  }
}
