// App.js
import React, { useState } from 'react';
import SearchComponent from './SearchComponent';
import axios from 'axios';

function App() {
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async (query) => {
    try {
      // Make API call to fetch search results from the backend
      const response = await axios.get(`search/?query=${query}`);
      setSearchResults(response.data.results);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  return (
    <div>
      <h1>Learning Platform</h1>
      <SearchComponent handleSearch={handleSearch} />
      {/* Display search results */}
      <div>
        <h3>Search Results:</h3>
        <ul>
          {searchResults.map((result, index) => (
            <li key={index}>{result.title}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
