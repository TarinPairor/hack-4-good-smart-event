from volunteers.views import *
from django.urls import path

app_name = "volunteers"

urlpatterns = [
    path("", home_page, name="home_page"),
    # ADMIN USER URLS
    path('admin_user_login/', admin_user_login, name='admin_user_login'),
    path('admin_user_signup/', admin_user_signup, name='admin_user_signup'),
    path('admin_user_logout/', admin_user_logout, name='admin_user_logout'),
    # PARTICIPANT USER URLS
    path('participant_user_signup/', participant_user_signup, name='participant_user_signup'),
    path('participant_user_login/', participant_user_login, name='participant_user_login'),
    path('participant_user_logout/', participant_user_logout, name='participant_user_logout'),
    path("get_participant_user_details/", get_participant_user_details, name="get_participant_user_details"),
    # VALIDATE URLS
    path('validate/', validate, name='validate'),
    # EVENT URLS
    path('get_events/', get_events, name='event'),
    path('create_event/', create_event, name='create_event'),
    path('end_event/', end_event, name='end_event'),
    path('search_event_by_id/', search_event_by_id, name='search_event_by_id'),
    path('check_in/', check_in, name='check_in'),
    path('check_out/', check_out, name='check_out'),
    path('get_attendances_with_event_id/', get_attendances_with_event_id, name='get_attendances_with_event_id'),
    path('get_time_spent_at_event_from_participant/', get_time_spent_at_event_from_participant, name='get_time_spent_at_event_from_participant'),
    path('get_average_time_spent_from_particants_with_event_id/', get_average_time_spent_from_particants_with_event_id, name='get_average_time_spent_from_particants_with_event_id'),
    path('get_past_events/', get_past_events, name='get_past_events'),
    path('get_current_events/', get_current_events, name='get_current_events'),
    # SURVEY URLS
    path('create_survey/', create_survey, name='create_survey'),
    path('get_surveys_under_event_id/', get_surveys_under_event_id, name='get_surveys_under_event_id'),
    path('answer_survey_question_with_question_id/', answer_survey_question_with_question_id, name='answer_survey_question_with_question_id'),
    path('get_survey_question_with_question_id/', get_survey_question_with_question_id, name='get_survey_question_with_question_id'),
    path('get_question_ids_from_survey_id/', get_question_ids_from_survey_id, name='get_question_ids_from_survey_id'),
    path('get_all_answered_survey_questions_with_event_id/', get_all_answered_survey_questions_with_event_id, name='get_all_answered_survey_questions_with_event_id'),
    path('get_questions_and_answers_from_survey_id/', get_questions_and_answers_from_survey_id, name='get_questions_and_answers_from_survey_id'),
    #AI URLS
    path('chatbot_response/', chatbot_response, name='chatbot_response')
    
]
