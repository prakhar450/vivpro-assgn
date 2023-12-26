import logo from './logo.svg';
import './App.css';
import React from 'react';
import SongList from './components/SongList';

function App() {
  return (
    <div className="App">
      <h1>My Playlist</h1>
      <SongList />
    </div>
  );
}

export default App;
