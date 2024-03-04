// App.js
import React, { useState } from 'react';
import SearchComponent from './SearchComponent';
import axios from 'axios';

function App() {
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (query) => {
    setIsLoading(true);
    try {
      // Make API call to fetch search results from the backend
      const response = await axios.get(`http://127.0.0.1:8000/mentor/search/?query=${query}`);
      setSearchResults(response.data.results);
    } catch (error) {
      console.error('Error fetching search results:', error);
      setSearchResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h1>Learning Platform</h1>
      <SearchComponent handleSearch={handleSearch} />
      {/* Display search results */}
      <div>
        <h2>Search Results</h2>
        {isLoading && <p>Loading...</p>}
        {!isLoading && searchResults.length === 0 && <p>No results found.</p>}
        {!isLoading && searchResults.length > 0 && (
          <ul>
            {searchResults.map((result, index) => (
              <li key={index}>{result.title}</li>
            ))}
          </ul>
        )}
      </div>
      {/* Other components and content can be added here */}
    </div>
  );
}

export default App;
