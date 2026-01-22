from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
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
            {'name': 'Iron Man', 'email': 'tony.stark@marvel.com', 'password': 'arc_reactor123'},
            {'name': 'Captain America', 'email': 'steve.rogers@marvel.com', 'password': 'vibranium_shield'},
            {'name': 'Thor', 'email': 'thor.odinson@marvel.com', 'password': 'mjolnir_worthy'},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@marvel.com', 'password': 'red_room_spy'},
            {'name': 'Hulk', 'email': 'bruce.banner@marvel.com', 'password': 'gamma_smash'},
            {'name': 'Spider-Man', 'email': 'peter.parker@marvel.com', 'password': 'web_slinger'},
        ]
        
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dc.com', 'password': 'kryptonite_fear'},
            {'name': 'Batman', 'email': 'bruce.wayne@dc.com', 'password': 'dark_knight'},
            {'name': 'Wonder Woman', 'email': 'diana.prince@dc.com', 'password': 'lasso_truth'},
            {'name': 'The Flash', 'email': 'barry.allen@dc.com', 'password': 'speed_force'},
            {'name': 'Aquaman', 'email': 'arthur.curry@dc.com', 'password': 'ocean_king'},
            {'name': 'Green Lantern', 'email': 'hal.jordan@dc.com', 'password': 'willpower_ring'},
        ]
        
        marvel_user_objects = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_marvel._id)
            )
            marvel_user_objects.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name} (Team Marvel)'))
        
        dc_user_objects = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
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
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population complete!'))
        self.stdout.write(self.style.SUCCESS(f'Total Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Leaderboard Entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('='*50))
