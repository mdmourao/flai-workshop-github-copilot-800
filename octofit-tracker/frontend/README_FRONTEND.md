# OctoFit Tracker Frontend

React-based frontend for the OctoFit Tracker fitness application.

## Features

- User management and profiles
- Activity tracking and logging
- Team management
- Competitive leaderboard
- Personalized workout suggestions

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file from the example:
```bash
cp .env.example .env
```

3. Update the `.env` file with your Codespace name (this is usually set automatically in GitHub Codespaces):
```
REACT_APP_CODESPACE_NAME=your-codespace-name
```

## Running the Application

Start the development server:
```bash
npm start
```

The application will open at [http://localhost:3000](http://localhost:3000)

## Available Routes

- `/` - Home page
- `/users` - User management
- `/activities` - Activity tracking
- `/teams` - Team management
- `/leaderboard` - Competitive leaderboard
- `/workouts` - Workout suggestions

## API Integration

The frontend connects to the Django REST API backend running on port 8000. All API endpoints follow the pattern:
```
https://${REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/{endpoint}/
```

## Components

- **Users**: Display and manage user profiles
- **Activities**: Track and log fitness activities
- **Teams**: Create and manage teams
- **Leaderboard**: View competitive rankings
- **Workouts**: Get personalized workout suggestions

## Technologies

- React 19.2.3
- React Router DOM 7.12.0
- Bootstrap 5.3.8
- Fetch API for HTTP requests

## Development

The app includes console logging for debugging API calls. Open browser DevTools to view:
- API endpoint URLs
- Response data
- Error messages
