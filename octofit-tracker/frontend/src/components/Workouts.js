import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts API Response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts Data:', workoutsData);
        
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p>Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Workout Suggestions</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>User</th>
              <th>Workout Type</th>
              <th>Duration (min)</th>
              <th>Description</th>
              <th>Suggested Date</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length > 0 ? (
              workouts.map((workout) => (
                <tr key={workout.id}>
                  <td>{workout.id}</td>
                  <td>{workout.user}</td>
                  <td>{workout.workout_type}</td>
                  <td>{workout.duration}</td>
                  <td>{workout.description || 'N/A'}</td>
                  <td>{new Date(workout.suggested_date).toLocaleDateString()}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center">No workouts found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
