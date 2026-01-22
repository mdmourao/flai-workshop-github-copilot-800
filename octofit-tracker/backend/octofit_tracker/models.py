from djongo import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  # in kg
    height = models.FloatField(null=True, blank=True)  # in cm
    fitness_level = models.CharField(max_length=50, null=True, blank=True)  # Beginner, Intermediate, Advanced
    team_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in kilometers
    calories = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"User {self.user_id} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name


class WorkoutSuggestion(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    description = models.TextField()
    suggested_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workout_suggestions'

    def __str__(self):
        return f"{self.workout_type} - {self.duration} mins for user {self.user_id}"
