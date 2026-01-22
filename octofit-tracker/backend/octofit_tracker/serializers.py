from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout, WorkoutSuggestion
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """Custom field to handle MongoDB ObjectId"""
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['_id', 'id', 'name', 'username', 'email', 'password', 'age', 'weight', 'height', 'fitness_level', 'team_id', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_id(self, obj):
        """Return the _id as id for frontend compatibility"""
        return str(obj._id)


class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    username = serializers.SerializerMethodField()
    total_activities = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'team_id', 'total_points', 'rank', 'username', 'total_activities', 'updated_at']
    
    def get_username(self, obj):
        """Get username from User model"""
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return f"User {obj.user_id}"
    
    def get_total_activities(self, obj):
        """Count total activities for this user"""
        return Activity.objects.filter(user_id=str(obj.user_id)).count()


class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'category', 'created_at']


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutSuggestion
        fields = ['_id', 'id', 'user_id', 'user', 'workout_type', 'duration', 'description', 'suggested_date', 'created_at']
    
    def get_id(self, obj):
        """Return the _id as id for frontend compatibility"""
        return str(obj._id)
    
    def get_user(self, obj):
        """Get username from User model"""
        try:
            user = User.objects.get(_id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return f"User {obj.user_id}"
