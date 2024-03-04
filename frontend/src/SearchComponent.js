import React, { useState } from 'react';
import axios from 'axios';

const SearchComponent = ({ handleSearch }) => {
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Make a GET request to the backend with the search query
      const response = await axios.get(`search/?query=${query}`);
      // Update the search results state with the response data
      setSearchResults(response.data.results);
      // Pass the search results to the parent component
      handleSearch(searchResults);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  return (
    <div style={styles.container}>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search for content..."
          value={query}
          onChange={handleChange}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>
          Search
        </button>
      </form>
    </div>
  );
};

const styles = {
  container: {
    marginBottom: '20px',
  },
  input: {
    padding: '10px',
    marginRight: '10px',
    width: '300px',
    borderRadius: '5px',
    border: '1px solid #ccc',
    fontSize: '16px',
    outline: 'none',
  },
  button: {
    padding: '10px 20px',
    backgroundColor: '#007bff',
    color: '#fff',
    borderRadius: '5px',
    border: 'none',
    fontSize: '16px',
    cursor: 'pointer',
  },
};

export default SearchComponent;
