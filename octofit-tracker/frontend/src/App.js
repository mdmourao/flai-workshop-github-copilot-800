import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-4">
      <div className="card mb-4">
        <div className="card-body text-center py-5">
          <img 
            src="/octofitapp-small.png" 
            alt="OctoFit Logo" 
            style={{ 
              height: '120px', 
              marginBottom: '1.5rem',
              filter: 'drop-shadow(0 10px 30px rgba(102, 126, 234, 0.4))'
            }} 
          />
          <h1>Welcome to OctoFit Tracker</h1>
          <p className="lead">Track your fitness activities, compete with teams, and achieve your goals!</p>
          <div className="mt-4">
            <Link to="/activities" className="btn btn-primary btn-lg me-2">
              Get Started
            </Link>
            <Link to="/leaderboard" className="btn btn-outline-light btn-lg">
              View Leaderboard
            </Link>
          </div>
        </div>
      </div>

      <div className="row g-4">
        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🏃‍♂️</div>
              <h3 className="card-title">Track Activities</h3>
              <p className="card-text">Log your workouts and monitor your progress with detailed analytics and insights.</p>
              <Link to="/activities" className="btn btn-primary mt-3">
                View Activities
              </Link>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>👥</div>
              <h3 className="card-title">Join Teams</h3>
              <p className="card-text">Collaborate with others, share achievements, and compete together for glory.</p>
              <Link to="/teams" className="btn btn-primary mt-3">
                View Teams
              </Link>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🏆</div>
              <h3 className="card-title">Compete</h3>
              <p className="card-text">Check the leaderboard, earn badges, and see how you rank against others.</p>
              <Link to="/leaderboard" className="btn btn-primary mt-3">
                View Leaderboard
              </Link>
            </div>
          </div>
        </div>
      </div>

      <div className="row g-4 mt-2">
        <div className="col-md-6">
          <div className="card h-100">
            <div className="card-body">
              <h3 className="card-title">💪 Workout Suggestions</h3>
              <p className="card-text">Get personalized workout recommendations based on your fitness level and goals.</p>
              <Link to="/workouts" className="btn btn-success">
                View Suggestions
              </Link>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card h-100">
            <div className="card-body">
              <h3 className="card-title">👤 User Profiles</h3>
              <p className="card-text">Explore user profiles, track achievements, and connect with the fitness community.</p>
              <Link to="/users" className="btn btn-info">
                View Users
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img 
                src="/octofitapp-small.png" 
                alt="OctoFit Logo" 
                className="navbar-logo"
              />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
