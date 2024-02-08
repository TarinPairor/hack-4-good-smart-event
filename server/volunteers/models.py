from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class AdminUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default='admin_username')
    email = models.EmailField(unique=True, default="admin@change.me")
    groups = models.ManyToManyField(Group, blank=True, related_name="adminuser_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="adminuser_permissions")
    password = models.CharField(max_length=128, default='admin_password')

    # Add these lines
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     related_name="adminuser_set",
    #     related_query_name="user",
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_name="adminuser_set",
    #     related_query_name="user",
    # )

class Participant(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, default="admin@change.me")
    groups = models.ManyToManyField(Group, blank=True, related_name="participant_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="participant_permissions")
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #array of login in times
    
    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True)
    is_present = models.BooleanField()

class Choice(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('choice', 'Multiple Choice'),
    )

    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=400, blank=True, null=True)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='text')
    choices = models.ManyToManyField(Choice, blank=True)

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    user = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.answer_text if self.answer_text else 'No answer'

class Survey(models.Model):
    name = models.CharField(max_length=200)
    admin = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    questions = models.ManyToManyField(Question)