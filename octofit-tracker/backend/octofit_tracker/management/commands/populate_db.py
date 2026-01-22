from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout, WorkoutSuggestion
from bson import ObjectId
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared!'))
        
        # Create Teams
        self.stdout.write(self.style.WARNING('Creating teams...'))
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='The World\'s Greatest Super Heroes'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name} and {team_dc.name}'))
        
        # Create Users (Superheroes)
        self.stdout.write(self.style.WARNING('Creating superhero users...'))
        marvel_heroes = [
            {'name': 'Iron Man', 'username': 'ironman', 'email': 'tony.stark@marvel.com', 'password': 'arc_reactor123', 'age': 45, 'weight': 84, 'height': 185, 'fitness_level': 'Advanced'},
            {'name': 'Captain America', 'username': 'captainamerica', 'email': 'steve.rogers@marvel.com', 'password': 'vibranium_shield', 'age': 105, 'weight': 95, 'height': 188, 'fitness_level': 'Advanced'},
            {'name': 'Thor', 'username': 'thor', 'email': 'thor.odinson@marvel.com', 'password': 'mjolnir_worthy', 'age': 1500, 'weight': 108, 'height': 198, 'fitness_level': 'Advanced'},
            {'name': 'Black Widow', 'username': 'blackwidow', 'email': 'natasha.romanoff@marvel.com', 'password': 'red_room_spy', 'age': 36, 'weight': 59, 'height': 170, 'fitness_level': 'Advanced'},
            {'name': 'Hulk', 'username': 'hulk', 'email': 'bruce.banner@marvel.com', 'password': 'gamma_smash', 'age': 49, 'weight': 135, 'height': 244, 'fitness_level': 'Advanced'},
            {'name': 'Spider-Man', 'username': 'spiderman', 'email': 'peter.parker@marvel.com', 'password': 'web_slinger', 'age': 23, 'weight': 76, 'height': 178, 'fitness_level': 'Intermediate'},
        ]
        
        dc_heroes = [
            {'name': 'Superman', 'username': 'superman', 'email': 'clark.kent@dc.com', 'password': 'kryptonite_fear', 'age': 35, 'weight': 107, 'height': 191, 'fitness_level': 'Advanced'},
            {'name': 'Batman', 'username': 'batman', 'email': 'bruce.wayne@dc.com', 'password': 'dark_knight', 'age': 42, 'weight': 95, 'height': 188, 'fitness_level': 'Advanced'},
            {'name': 'Wonder Woman', 'username': 'wonderwoman', 'email': 'diana.prince@dc.com', 'password': 'lasso_truth', 'age': 3000, 'weight': 75, 'height': 183, 'fitness_level': 'Advanced'},
            {'name': 'The Flash', 'username': 'flash', 'email': 'barry.allen@dc.com', 'password': 'speed_force', 'age': 29, 'weight': 81, 'height': 183, 'fitness_level': 'Intermediate'},
            {'name': 'Aquaman', 'username': 'aquaman', 'email': 'arthur.curry@dc.com', 'password': 'ocean_king', 'age': 38, 'weight': 146, 'height': 185, 'fitness_level': 'Advanced'},
            {'name': 'Green Lantern', 'username': 'greenlantern', 'email': 'hal.jordan@dc.com', 'password': 'willpower_ring', 'age': 33, 'weight': 86, 'height': 188, 'fitness_level': 'Intermediate'},
        ]
        
        marvel_user_objects = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                username=hero['username'],
                email=hero['email'],
                password=hero['password'],
                age=hero['age'],
                weight=hero['weight'],
                height=hero['height'],
                fitness_level=hero['fitness_level'],
                team_id=str(team_marvel._id)
            )
            marvel_user_objects.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name} (Team Marvel)'))
        
        dc_user_objects = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                username=hero['username'],
                email=hero['email'],
                password=hero['password'],
                age=hero['age'],
                weight=hero['weight'],
                height=hero['height'],
                fitness_level=hero['fitness_level'],
                team_id=str(team_dc._id)
            )
            dc_user_objects.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name} (Team DC)'))
        
        all_users = marvel_user_objects + dc_user_objects
        
        # Create Activities
        self.stdout.write(self.style.WARNING('Creating activities...'))
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'Cardio']
        
        for user in all_users:
            num_activities = random.randint(5, 15)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                distance = round(random.uniform(2, 25), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = random.randint(200, 800)
                days_ago = random.randint(0, 30)
                activity_date = timezone.now() - timedelta(days=days_ago)
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=activity_date
                )
            self.stdout.write(self.style.SUCCESS(f'Created {num_activities} activities for {user.name}'))
        
        # Create Leaderboard entries
        self.stdout.write(self.style.WARNING('Creating leaderboard entries...'))
        leaderboard_entries = []
        for user in all_users:
            total_points = random.randint(500, 5000)
            leaderboard_entry = Leaderboard.objects.create(
                user_id=str(user._id),
                team_id=user.team_id,
                total_points=total_points
            )
            leaderboard_entries.append(leaderboard_entry)
        
        # Sort and assign ranks
        leaderboard_entries.sort(key=lambda x: x.total_points, reverse=True)
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
            # Find user by converting string ID to ObjectId
            user = User.objects.get(_id=ObjectId(entry.user_id))
            self.stdout.write(self.style.SUCCESS(f'Rank {rank}: {user.name} - {entry.total_points} points'))
        
        # Create Workouts
        self.stdout.write(self.style.WARNING('Creating workout suggestions...'))
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity workout designed to push your limits like Captain America',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 700,
                'category': 'Strength & Cardio'
            },
            {
                'name': 'Web-Slinger Circuit',
                'description': 'Agility and flexibility training inspired by Spider-Man',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_estimate': 500,
                'category': 'Cardio & Flexibility'
            },
            {
                'name': 'Amazonian Warrior Routine',
                'description': 'Combat training inspired by Wonder Woman',
                'difficulty': 'Advanced',
                'duration': 55,
                'calories_estimate': 650,
                'category': 'Combat & Strength'
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Lightning-fast cardio workout inspired by The Flash',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories_estimate': 450,
                'category': 'Cardio'
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Full-body water workout inspired by Aquaman',
                'difficulty': 'Beginner',
                'duration': 40,
                'calories_estimate': 400,
                'category': 'Swimming'
            },
            {
                'name': 'Asgardian Strength Training',
                'description': 'Heavy lifting workout worthy of Thor',
                'difficulty': 'Advanced',
                'duration': 50,
                'calories_estimate': 600,
                'category': 'Strength'
            },
            {
                'name': 'Dark Knight Martial Arts',
                'description': 'Mixed martial arts training inspired by Batman',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 700,
                'category': 'Combat'
            },
            {
                'name': 'Gamma Smash HIIT',
                'description': 'High-intensity interval training with Hulk-level power',
                'difficulty': 'Intermediate',
                'duration': 35,
                'calories_estimate': 500,
                'category': 'HIIT'
            },
            {
                'name': 'Kryptonian Core Workout',
                'description': 'Core strengthening exercises inspired by Superman',
                'difficulty': 'Beginner',
                'duration': 25,
                'calories_estimate': 300,
                'category': 'Core'
            },
            {
                'name': 'Black Widow Yoga Flow',
                'description': 'Flexibility and mindfulness training for spy-level agility',
                'difficulty': 'Beginner',
                'duration': 45,
                'calories_estimate': 250,
                'category': 'Yoga'
            },
        ]
        
        for workout_data in workouts:
            workout = Workout.objects.create(**workout_data)
            self.stdout.write(self.style.SUCCESS(f'Created workout: {workout.name}'))
        # Create Workout Suggestions for each user
        self.stdout.write(self.style.WARNING('Creating workout suggestions for users...'))
        workout_types = ['Strength', 'Cardio', 'Flexibility', 'HIIT', 'Yoga', 'Swimming', 'Combat']
        workout_descriptions = [
            'High-intensity workout designed to push your limits like Captain America',
            'Agility and flexibility training inspired by Spider-Man',
            'Combat training inspired by Wonder Woman',
            'Lightning-fast cardio workout inspired by The Flash',
            'Full-body water workout inspired by Aquaman',
            'Heavy lifting workout worthy of Thor',
            'Mixed martial arts training inspired by Batman',
            'High-intensity interval training with Hulk-level power',
            'Core strengthening exercises inspired by Superman',
            'Flexibility and mindfulness training for spy-level agility',
        ]
        
        for user in all_users:
            # Create 1-3 workout suggestions per user
            num_suggestions = random.randint(1, 3)
            for i in range(num_suggestions):
                workout_type = random.choice(workout_types)
                duration = random.choice([30, 35, 40, 45, 50, 55, 60])
                description = random.choice(workout_descriptions)
                days_ahead = random.randint(0, 7)
                suggested_date = timezone.now() + timedelta(days=days_ahead)
                
                WorkoutSuggestion.objects.create(
                    user_id=str(user._id),
                    workout_type=workout_type,
                    duration=duration,
                    description=description,
                    suggested_date=suggested_date
                )
            self.stdout.write(self.style.SUCCESS(f'Created {num_suggestions} workout suggestions for {user.name}'))
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population complete!'))
        self.stdout.write(self.style.SUCCESS(f'Total Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Leaderboard Entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Workout Suggestions: {WorkoutSuggestion.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('='*50))
