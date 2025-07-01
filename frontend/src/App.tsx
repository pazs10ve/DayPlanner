import { useState } from 'react';
import axios from 'axios';
import './App.css';
import Header from './components/Header';

interface PlannerData {
  city: string;
  weather: string;
  dining_suggestion: string;
  dining_plan: any;
  parsed_dining_plan?: Array<Record<string, string>>;
}

function App() {
  const [city, setCity] = useState('');
  const [plannerData, setPlannerData] = useState<PlannerData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const getPlanner = async () => {
    if (!city) {
      setError('Please enter a city name.');
      return;
    }
    setLoading(true);
    setError(null);
    setPlannerData(null);
    try {
      const response = await axios.get(`https://dayplanner-backend-j6y7.onrender.com/planner/${city}`);
      const data = response.data;
      const { dining_plan } = data;

      if (typeof dining_plan === 'string' && dining_plan.includes('|')) {
        const lines = dining_plan.split('\n').filter(line => line.trim() !== '');
        if (lines.length > 2) {
          const headers = lines[0].split('|').map(h => h.trim()).filter(h => h);
          const rows = lines.slice(2).map(line => {
            const values = line.split('|').map(v => v.trim()).filter(v => v);
            const rowObject: Record<string, string> = {};
            headers.forEach((header, index) => {
              rowObject[header] = values[index];
            });
            return rowObject;
          });
          data.parsed_dining_plan = rows;
        }
      }
      setPlannerData(data);
    } catch (err) {
      setError('Failed to fetch data. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <Header />
      <main>
        <div className="input-section">
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter city name"
          />
          <button onClick={getPlanner} disabled={loading}>
            {loading ? 'Loading...' : 'Get Plan'}
          </button>
        </div>
        {error && <p className="error">{error}</p>}
        {plannerData && (
          <div className="results-section">
            <h2>Plan for {plannerData.city}</h2>
            <p><strong>Weather:</strong> {plannerData.weather}</p>
            <p><strong>Suggestion:</strong> {plannerData.dining_suggestion}</p>
            <div>
              <h3>Dining Plan:</h3>
              {plannerData.parsed_dining_plan && plannerData.parsed_dining_plan.length > 0 ? (
                (() => {
                  const headers = Object.keys(plannerData.parsed_dining_plan[0]);
                  return (
                    <table className="dining-plan-table">
                      <thead>
                        <tr>
                          {headers.map(header => <th key={header}>{header}</th>)}
                        </tr>
                      </thead>
                      <tbody>
                        {plannerData.parsed_dining_plan.map((row, index) => (
                          <tr key={index}>
                            {headers.map(key => (
                              <td key={key} data-label={key}>{row[key]}</td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  );
                })()
              ) : (
                <p>{plannerData.dining_plan}</p>
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
