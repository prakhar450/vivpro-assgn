import React, { useState } from 'react';

function SongCard({ song }) {
    const [expanded, setExpanded] = useState(false);

    const toggleExpand = () => {
        setExpanded(!expanded);
    };

    return (
        <div className="song-card" onClick={toggleExpand}>
            <h3>{song.song_title}</h3>
            {expanded && (
                <div className="song-details">
                    <p>Title: {song.song_title}</p>
                    {song.dynamic_attrs && Object.entries(song.dynamic_attrs).map(([key, value]) => (
                        <p key={key}>{`${key}: ${value}`}</p>
                    ))}
                </div>
            )}
        </div>
    );
}

export default SongCard;
