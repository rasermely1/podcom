import React, { useState } from 'react';
import axios from 'axios';

const QueryComponent = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);
  const [llm, setLlm] = useState('gpt-4-vision-preview');

  const handleQuery = async () => {
    try {
      const response = await axios.post('http://localhost:5000/query', {
        query: query,
        llm: llm
      });
      setResults(response.data.results);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Query the LLM</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query"
      />
      <select value={llm} onChange={(e) => setLlm(e.target.value)}>
        <option value="gpt-4-vision-preview">GPT-4 Vision Preview</option>
        <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
        <option value="claude-2">Claude-2</option>
        <option value="mistral-7b">Mistral-7B</option>
        <option value="falcon-40b">Falcon-40B</option>
      </select>
      <button onClick={handleQuery}>Submit</button>
      {results && <div><h2>Results:</h2><pre>{results}</pre></div>}
    </div>
  );
};

export default QueryComponent;
