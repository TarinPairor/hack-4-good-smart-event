import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SurveyServices {
  constructor(private http: HttpClient) {}

  healthCheck() {
    const url = 'http://127.0.0.1:8000/volunteers/';
    return this.http.get(url);
  }

  createSurvey(eventId: string, surveyData: any) {
    const url = `http://127.0.0.1:8000/volunteers/create_survey/?event_id=${eventId}`;
    return this.http.post(url, surveyData);
  }

  getQuestionsFromSurveyId(surveyId: string): Observable<any> {
    const url =
      'http://127.0.0.1:8000/volunteers/get_question_ids_from_survey_id/';
    return this.http.get(url, { params: { survey_id: surveyId } });
  }

  getSurveyQuestionWithQuestionId(questionId: string): Observable<any> {
    const url =
      'http://127.0.0.1:8000/volunteers/get_survey_question_with_question_id/';
    return this.http.get(url, { params: { question_id: questionId } });
  }

  getSurveysUnderEventId(eventId: string): Observable<any> {
    const url = 'http://127.0.0.1:8000/volunteers/get_surveys_under_event_id/';
    return this.http.get(url, { params: { event_id: eventId } });
  }

  answerSurveyQuestionWithQuestionId(
    questionId: string,
    answer: string
  ): Observable<any> {
    const url = `http://127.0.0.1:8000/volunteers/answer_survey_question_with_question_id/?question_id=${questionId}`;
    // posts something like {answer: <input>}
    return this.http.post(url, { answer: answer });
  }

  getAverageTimeSpentFromParticipantsWithEventId(
    eventId: string
  ): Observable<any> {
    const url = `http://127.0.0.1:8000/volunteers/get_average_time_spent_from_particants_with_event_id/?event_id=${eventId}`;
    return this.http.get(url);
  }

  chabotResponseWithQuestionId(eventId: string): Observable<any> {
    const url = `http://127.0.0.1:8000/volunteers/chatbot_response/?event_id=${eventId}`;
    return this.http.get(url);
  }
}
