import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard API Response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard Data:', leaderboardData);
        
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="card">
          <div className="card-body text-center py-5">
            <div className="spinner-border text-primary mb-3" role="status">
              <span className="visually-hidden">Loading...</span>
            </div>
            <p className="mb-0">Loading leaderboard...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p className="mb-0">{error}</p>
        </div>
      </div>
    );
  }

  const getMedalEmoji = (rank) => {
    switch (rank) {
      case 1: return '🥇';
      case 2: return '🥈';
      case 3: return '🥉';
      default: return '';
    }
  };

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header d-flex justify-content-between align-items-center">
          <h2 className="mb-0">🏆 Leaderboard</h2>
          <span className="badge bg-primary">{leaderboard.length} Competitors</span>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>User</th>
                  <th>Total Points</th>
                  <th>Total Activities</th>
                </tr>
              </thead>
              <tbody>
                {leaderboard.length > 0 ? (
                  leaderboard.map((entry, index) => (
                    <tr key={entry.id || index} className={index < 3 ? 'table-primary' : ''}>
                      <td>
                        <span className={`badge ${
                          index === 0 ? 'bg-warning' :
                          index === 1 ? 'bg-secondary' :
                          index === 2 ? 'bg-danger' :
                          'bg-dark'
                        }`}>
                          {getMedalEmoji(index + 1)} {index + 1}
                        </span>
                      </td>
                      <td><strong>{entry.user || entry.username}</strong></td>
                      <td><span className="badge bg-success">{entry.total_points || entry.points || 0} pts</span></td>
                      <td><span className="badge bg-info">{entry.total_activities || entry.activities || 0}</span></td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="4" className="text-center py-4">
                      <p className="text-muted mb-0">No leaderboard data found</p>
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
