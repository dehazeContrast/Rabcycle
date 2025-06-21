import React, { useState } from 'react'
import './HistoryCard.css';

type HistoryCardProps = {
    image: string;
    info: string;
}

const HistoryCard: React.FC<HistoryCardProps> = ({ image, info }) => {

    return (
        <div className="card">
            {/* get from reactState's image and text */}
            <img src={image} width="100px" height="100px" className="image"/>
            <p className="info">{info}</p>
        </div>
    );
};

export default HistoryCard;