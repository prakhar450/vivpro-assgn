import React, { useState, useEffect } from 'react';
import SongCard from './SongCard';

function SongList() {
    const [songs, setSongs] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(0);

    useEffect(() => {
        // Fetch songs whenever the currentPage or searchTerm changes
        fetch(`/home?page=${currentPage}&search=${encodeURIComponent(searchTerm)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setSongs(data.songs);
                setTotalPages(data.total_pages);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }, [currentPage, searchTerm]);

    // Reset to the first page when the search term changes
    useEffect(() => {
        setCurrentPage(1);
    }, [searchTerm]);

    return (
        <div>
            <input
                type="text"
                placeholder="Search by title..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            {songs.map(song => (
                <SongCard key={song.song_id} song={song} />
            ))}
            <div>
                {Array.from({ length: totalPages }, (_, i) => i + 1).map(page => (
                    <button key={page} onClick={() => setCurrentPage(page)}>
                        {page}
                    </button>
                ))}
            </div>
        </div>
    );
}

export default SongList;
