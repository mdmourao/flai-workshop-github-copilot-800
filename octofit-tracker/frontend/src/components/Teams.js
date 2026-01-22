import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams API Response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams Data:', teamsData);
        
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading teams...</p></div>;
  if (error) return <div className="container mt-4"><p>Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Team Name</th>
              <th>Description</th>
              <th>Created Date</th>
            </tr>
          </thead>
          <tbody>
            {teams.length > 0 ? (
              teams.map((team) => (
                <tr key={team.id}>
                  <td>{team.id}</td>
                  <td>{team.name}</td>
                  <td>{team.description || 'N/A'}</td>
                  <td>{new Date(team.created_at).toLocaleDateString()}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center">No teams found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
