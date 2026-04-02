import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [movies, setMovies] = useState([])
  // New "Whiteboard" for the form inputs
  const [formData, setFormData] = useState({ title: '', director: '', year: '' })

  useEffect(() => {
    fetchMovies()
  }, [])

  const fetchMovies = async () => {
    const response = await axios.get('http://127.0.0.1:8000/movies')
    setMovies(response.data)
  }

  // This function sends the data to your POST route
  const handleAddMovie = async (e) => {
    e.preventDefault() // Stops the page from refreshing
    try {
      await axios.post('http://127.0.0.1:8000/movies', formData)
      setFormData({ title: '', director: '', year: '' }) // Clear the form
      fetchMovies() // Refresh the list to see the new movie!
    } catch (error) {
      alert("Error adding movie!")
    }
  }

  const handleDelete = async (id) => {
  try {
    // We send the ID to the URL we built in FastAPI: /movies/{id}
    await axios.delete(`http://127.0.0.1:8000/movies/${id}`)
    
    // Refresh the list so the movie "vanishes" from the screen
    fetchMovies()
  } catch (error) {
    alert("Could not delete the movie!")
  }
}

const handleUpdate = async (id) => {
  const newTitle = prompt("Enter the new movie title:");
  if (!newTitle) return; // If they hit cancel, do nothing

  try {
    // We send the ID in the URL, and the NEW data in the body
    await axios.put(`http://127.0.0.1:8000/movies/${id}`, {
      title: newTitle,
      director: "Updated", // You can expand this to ask for director too!
      year: 2024
    });
    fetchMovies(); // Refresh the list
  } catch (error) {
    alert("Update failed!");
  }
};

  return (
    <div style={{ padding: '20px' }}>
      <h1>🎬 Movie Collection</h1>

      {/* --- ADD MOVIE FORM --- */}
      <form onSubmit={handleAddMovie} style={{ marginBottom: '20px' }}>
        <input 
          placeholder="Title" 
          value={formData.title} 
          onChange={(e) => setFormData({...formData, title: e.target.value})} 
        />
        <input 
          placeholder="Director" 
          value={formData.director} 
          onChange={(e) => setFormData({...formData, director: e.target.value})} 
        />
        <input 
          type="number" 
          placeholder="Year" 
          value={formData.year} 
          onChange={(e) => setFormData({...formData, year: e.target.value})} 
        />
        <button type="submit">Add Movie</button>
      </form>

      {/* --- MOVIE LIST --- */}
<ul>
  {movies.map((movie) => (
    <li key={movie.id} style={{ marginBottom: '10px' }}>
      <strong>{movie.title}</strong> ({movie.year}) - {movie.director} 
      
      {/* Delete Button */}
      <button 
        onClick={() => handleDelete(movie.id)} 
        style={{ marginLeft: '10px', color: 'red' }}
      >
        Delete
      </button>

      {/* FLYTTA HIT EDIT-KNAPPEN (Innanför <li>) */}
      <button 
        onClick={() => handleUpdate(movie.id)} 
        style={{ marginLeft: '10px', color: 'blue' }}
      >
        Edit Title
      </button>
    </li>
  ))} 
  {/* Map-funktionen tar slut här uppe nu! */}
</ul>
    </div>
  )
}

export default App