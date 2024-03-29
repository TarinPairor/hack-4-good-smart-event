from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Participant, Event, Attendance, Survey, Question, Choice, AdminUser, Answer
import json
from django.utils import timezone
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from openai import OpenAI

client = OpenAI(api_key='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')


# Create your views here.


def home_page(request):
    """
    Renders the home page view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a welcome message.
    """
    return JsonResponse({"message": "Welcome to the home page"})  # Return JSON response


################################################################################################
# ADMIN USER AUTHENTICATION VIEWS
################################################################################################

@csrf_exempt
def admin_user_signup(request):
    """
    Handles the signup process for admin users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the signup process.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username is taken.'})
        else:
            user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=True)
            user.save()
            return JsonResponse({'message': 'Account created successfully.'})
    return JsonResponse({'message': 'Invalid request method.'})


@csrf_exempt
def admin_user_login(request):
    """
    Handles the login process for admin users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the login process.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return JsonResponse({'status': 'successfully logged in'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid username or password, or the user is not a superuser.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Username and password are required.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    

@csrf_exempt
def admin_user_logout(request):
    """
    Handles the logout process for admin users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the logout process.
    """
    logout(request)
    return JsonResponse({'message': 'Logged out successfully.'})


################################################################################################
# PARTICIPANT USER AUTHENTICATION VIEWS
################################################################################################

@csrf_exempt
def participant_user_signup(request):
    """
    Handles the signup process for participant users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the signup process.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if Participant.objects.filter(username=username).exists() or User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username is taken.'})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            participant = Participant.objects.create_user(username=username, password=password)
            participant.save()

            login(request, user)
            return JsonResponse({'message': 'Account created successfully.'})
    return JsonResponse({'message': 'Invalid request method.'})


@csrf_exempt
def participant_user_login(request):
    """
    Handles the login process for participant users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the login process.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'successfully logged in'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Username is required.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@csrf_exempt
def participant_user_logout(request):
    """
    Handles the logout process for participant users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the logout process.
    """
    logout(request)
    return JsonResponse({'message': 'Logged out successfully.'})


################################################################################################
# VALIDATE VIEW
################################################################################################

@csrf_exempt
def validate(request):
    """
    Validates the user's authentication status.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the user's authentication status.
    """
    return JsonResponse({'message': str(request.user)})
    if request.user.is_authenticated:
        user_data = {
            'username': request.user.username,
            'user_type': 'admin' if request.user.is_superuser else 'participant'
            # Add more user attributes as needed
        }
        return JsonResponse(user_data)
    elif str(request.user) == 'AnonymousUser':
        user_data = {
            'username': request.user,
            'user_type': 'anonymous'
        }
        return JsonResponse(user_data)
    else:
        return JsonResponse({'message': 'Not logged in.'})
    

################################################################################################
# GET PARTICIPANT USER DETAILS
################################################################################################

def get_participant_user_details(request):
    """
    Retrieves the details of a participant user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the details of the participant user.
    """
    if request.user.is_authenticated:
        user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'user_type': 'participant'
        }
        return JsonResponse(user_data)
    else:
        return JsonResponse({'message': 'Not logged in.'})
    

################################################################################################
# EVENT VIEWS
################################################################################################
    
def get_events(request):
    """
    Retrieves all events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the list of events.
    """
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'start_date': event.start_date,
            'end_date': event.end_date
        })
    return JsonResponse(event_list, safe=False)
    
@csrf_exempt
def create_event(request):
    """
    Creates a new event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the event creation process.
    """
    # if request.user.is_authenticated and ~request.user.is_superuser:
    if True:
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        start_date = timezone.now()

        if name and description and start_date:
            event = Event(name=name, description=description, start_date=start_date)
            event.save()
            return JsonResponse({'message': 'Event created successfully.'})
        else:
            return JsonResponse({'message': 'All fields are required.'})
    else:
        return JsonResponse({'message': 'Not logged in as an admin user.'})
    

@csrf_exempt
def end_event(request):
    """
    Ends an event.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The event ID.

    Returns:
        JsonResponse: A JSON response indicating the status of the event ending process.
    """
    event_id = request.GET.get('event_id', None)
    if event_id is not None:
        event_id = int(event_id)
        # if request.user.is_authenticated and ~request.user.is_superuser:
        if True:
            event = Event.objects.get(id=event_id)
            event.end_date = timezone.now()
            event.save()
            return JsonResponse({'message': 'Event ended successfully.'})
        else:
            return JsonResponse({'message': 'Not logged in as an admin user.'})
    else:
        return JsonResponse({'message': 'No event id provided.'})

@csrf_exempt
def search_event_by_id(request):
    """
    Retrieves an event by its ID.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The event ID.

    Returns:
        JsonResponse: A JSON response containing the details of the event.
    """
    event_id = request.GET.get('event_id', None)
    event = Event.objects.get(id=event_id)
    event_data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date
    }
    return JsonResponse(event_data)

@csrf_exempt
def get_current_events(request):
    """
    Retrieves all current events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the list of current events.
    """
    current_events = Event.objects.filter(end_date__isnull=True)
    event_list = []
    for event in current_events:
        event_list.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'start_date': event.start_date,
            'end_date': event.end_date
        })
    return JsonResponse(event_list, safe=False)

@csrf_exempt
def get_past_events(request):
    """
    Retrieves all past events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the list of past events.
    """
    past_events = Event.objects.filter(end_date__isnull=False)
    event_list = []
    for event in past_events:
        event_list.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'start_date': event.start_date,
            'end_date': event.end_date
        })
    return JsonResponse(event_list, safe=False)

@csrf_exempt
def get_events_by_admin(request):
    """
    Retrieves all events created by an admin user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the list of events created by the admin user.
    """
    if request.user.is_authenticated and request.user.is_superuser:
        events = Event.objects.filter(admin=request.user.username)
        event_list = []
        for event in events:
            event_list.append({
                'id': event.id,
                'name': event.name,
                'description': event.description,
                'start_date': event.start_date,
                'end_date': event.end_date
            })
        return JsonResponse(event_list, safe=False)
    else:
        return JsonResponse({'message': 'Not logged in as an admin user.'})
################################################################################################
# ATTENDANCE VIEWS
################################################################################################
@csrf_exempt
def get_attendances_with_event_id(request):
    """
    Retrieves all attendances for an event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the list of attendances for the event.
    """
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id=event_id)
    attendances = Attendance.objects.filter(event=event)
    attendance_list = []
    for attendance in attendances:
        attendance_list.append({
            # 'event': attendance.event,
            'participant': attendance.participant.username,
            'check_in_time': attendance.check_in_time,
            'check_out_time': attendance.check_out_time,
            'is_present': attendance.is_present
        })
    return JsonResponse(attendance_list, safe=False)


@csrf_exempt    
def check_in(request):
    """
    Checks in a participant user to an event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the check-in process.
    """
    if request.user.is_authenticated and not request.user.is_superuser:
        # get event_id from params
        event_id = request.GET.get('event_id', None)
        event = Event.objects.get(id=event_id)
        if event:
            participant = Participant.objects.get(username=request.user.username)
            attendance = Attendance(event=event, participant=participant, check_in_time=timezone.now(), is_present=True)
            attendance.save()
            return JsonResponse({'message': 'Checked in successfully.'})
        else:
            return JsonResponse({'message': 'Event ID is required.'})
    else:
        return JsonResponse({'message': 'Not logged in as a participant user.'})
    

def check_out(request):
    """
    Checks out a participant user from an event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the check-out process.
    """
    if request.user.is_authenticated and not request.user.is_superuser:
        # get event_id from params
        event_id = request.GET.get('event_id', None)
        event = Event.objects.get(id=event_id)
        if event:
            participant = Participant.objects.get(username=request.user.username)
            attendance = Attendance.objects.get(event=event, participant=participant)
            attendance.check_out_time = timezone.now()
            attendance.is_present = False
            attendance.save()
            return JsonResponse({'message': 'Checked out successfully.'})
        else:
            return JsonResponse({'message': 'Event ID is required.'})
    else:
        return JsonResponse({'message': 'Not logged in as a participant user.'})
    
@csrf_exempt    
def get_time_spent_at_event_from_participant(request):
    """
    Retrieves the time spent by a participant user at an event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the time spent by the participant user at the event.
    """
    event_id = request.GET.get('event_id', None)
    participant_username = request.GET.get('p', None)
    if event_id and participant_username:
        try:
            event = Event.objects.get(id=event_id)
            participant = Participant.objects.get(username=participant_username)
            attendance = Attendance.objects.get(event=event, participant=participant)
            time_spent = attendance.check_out_time - attendance.check_in_time
            if attendance.check_out_time is None:
                time_spent = timezone.now() - attendance.check_in_time
            time_spent_readable = str(datetime.timedelta(seconds=time_spent.total_seconds()))
            return JsonResponse({
                'participant': participant.username,
                'time_spent': time_spent_readable})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Event or participant does not exist.'})
    else:
        return JsonResponse({'message': 'Event ID and participant username are required.'})
    
@csrf_exempt
def get_average_time_spent_from_particants_with_event_id(request):
    """
    Retrieves the average time spent by all participants at an event.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the average time spent by all participants at the event.
    """
    event_id = request.GET.get('event_id', None)
    event = Event.objects.get(id=event_id)
    attendances = Attendance.objects.filter(event=event)
    time_spent_list = []
    for attendance in attendances:
        time_spent = attendance.check_out_time - attendance.check_in_time
        if attendance.check_out_time is None:
            time_spent = timezone.now() - attendance.check_in_time
        time_spent_list.append(time_spent.total_seconds())
    average_time_spent = sum(time_spent_list) / len(time_spent_list)
    average_time_spent_readable = str(datetime.timedelta(seconds=average_time_spent))
    return JsonResponse({'average_time_spent': average_time_spent_readable})
    
################################################################################################
# SURVEY VIEWS
################################################################################################
    
@csrf_exempt
def create_survey(request):
    if request.method == 'POST':
        # if request.user.is_superuser:
        if True:
            data = json.loads(request.body)

            name = data.get('name')
            description = data.get('description')
            event_id = request.GET.get('event_id', None)
            questions_data = data.get('questions', None)

            # Check if name is provided
            if not name:
                return JsonResponse({'message': 'Name is required.'})
            try:
                event = Event.objects.get(id=event_id)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Event does not exist.'})

            survey = Survey(name=name, description=description, admin=request.user.username, event=event)
            survey.save()

            if questions_data:
                for question_data in questions_data:
                    question_text = question_data.get('question')
                    question_type = question_data.get('question_type')
                    choices_text = question_data.get('choices', [])

                    question = Question(question=question_text, question_type=question_type)
                    question.save()

                    for choice_text in choices_text:
                        choice = Choice(text=choice_text)
                        choice.save()
                        question.choices.add(choice)

                    survey.questions.add(question)

            return JsonResponse({'message': 'Survey created successfully by.' + request.user.username})
        else:
            return JsonResponse({'message': 'Only admin users can create surveys.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})
    
@csrf_exempt
def get_survey(request):
    survey_id = request.GET.get('survey_id', None)
    survey = Survey.objects.get(id=survey_id)
    survey_data = {
        'id': survey.id,
        'name': survey.name,
        'description': survey.description,
        'admin': survey.admin,
        'event': survey.event,
        'questions': []
    }
    for question in survey.questions.all():
        question_data = {
            'id': question.id,
            'question': question.question,
            'question_type': question.question_type,
            'choices': []
        }
        for choice in question.choices.all():
            question_data['choices'].append({
                'id': choice.id,
                'text': choice.text
            })
        survey_data['questions'].append(question_data)
    return JsonResponse(survey_data)


@csrf_exempt
def get_surveys_under_event_id(request):
    event_id = request.GET.get('event_id', None)
    event = Event.objects.get(id=event_id)
    surveys = Survey.objects.filter(event=event)
    survey_list = []
    for survey in surveys:
        survey_list.append({
            'id': survey.id,
            'name': survey.name,
            'description': survey.description,
            'admin': survey.admin,
            # 'event': survey.event
        })
    return JsonResponse(survey_list, safe=False)



@csrf_exempt
def get_questions_and_answers_from_survey_id(request):
    survey_id = request.GET.get('survey_id', None)
    survey = Survey.objects.get(id=survey_id)
    questions = survey.questions.all()
    question_list = []
    for question in questions:
        question_list.append({
            'question': question.question,
            'answer': question.answer
        })
    return JsonResponse(question_list, safe=False)


@csrf_exempt
def answer_survey_question_with_question_id(request):
    if request.method == 'POST':
        # if request.user.is_authenticated and not request.user.is_superuser:
        if True:
            question_id = request.GET.get('question_id')
            data = json.loads(request.body)
            answer_text = data.get('answer')

            # Get the question
            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                return JsonResponse({'error': 'Question does not exist'}, status=404)

            # Check the question type
            if question.question_type == 'choice':
                if answer_text not in question.choices.values_list('text', flat=True):
                    return JsonResponse({'message': 'Invalid choice.'}, status=400)

            # Append the user's answer to the question's answer field
            answer_string = f":{request.user.username}=:{answer_text}"
            if question.answer:
                question.answer += "\n" + answer_string
            else:
                question.answer = answer_string
            question.save()

            # Create or update the answer in the Answer table
            Answer.objects.update_or_create(
                user=request.user.username,
                question=question,
                answer_text=answer_text
            )

            return JsonResponse({'message': 'Answer saved successfully'}, status=200)

        else:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def get_question_ids_from_survey_id(request):
    survey_id = request.GET.get('survey_id')
    try:
        survey = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return JsonResponse({'message': 'Survey does not exist.'})
    questions = survey.questions.all()
    question_ids = [question.id for question in questions]
    return JsonResponse(question_ids, safe=False)


@csrf_exempt
def get_survey_question_with_question_id(request):
    question_id = request.GET.get('question_id')
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question does not exist.'})
    choices = question.choices.all()
    return JsonResponse({'question_id': question.id, 'question': question.question, 'answer': question.answer, 'question_type': question.question_type, 'choices': [choice.text for choice in choices]})


@csrf_exempt
def get_all_answered_survey_questions_with_event_id(request):
    if request.method == 'GET':
        event_id = request.GET.get('event_id')
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event does not exist'}, status=404)

        surveys = Survey.objects.filter(event=event)
        question_list = []
        for survey in surveys:
            questions = survey.questions.all().filter(answer__isnull=False)
            for question in questions:
                question_list.append({
                    'question': question.question,
                    'answer': question.answer
                })

        return JsonResponse(question_list, safe=False)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    # if request.user.is_superuser:
    #     questions = Question.objects.filter(answer__isnull=False)
    #     question_list = []
    #     for question in questions:
    #         question_list.append({
    #             'question': question.question,
    #             'answer': question.answer
    #         })
    #     return JsonResponse(question_list, safe=False)
    # else:
    #     return JsonResponse({'message': 'Only admin users can view answered survey questions.'})


@csrf_exempt
def chatbot_response(request):
    if request.method == 'GET':
        event_id = request.GET.get('event_id')

        # The first half of get_all_answered_survey_questions_with_event_id
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Event does not exist'}, status=404)

        surveys = Survey.objects.filter(event=event)
        question_list = []
        for survey in surveys:
            questions = survey.questions.all().filter(answer__isnull=False)
            for question in questions:
                question_list.append({
                    'question': question.question,
                    'answer': question.answer
                })

        # Format the question_list for the chatbot
        question_list_string = "\n".join([f"Question: {item['question']}\nAnswer: {item['answer']}" for item in question_list])

        # Pass the question_list to the chatbot
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": f"What is the concluded feedback of our event from this data?\n{question_list_string}"}
          ])

        return JsonResponse({'message': response.choices[0].message.content})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)