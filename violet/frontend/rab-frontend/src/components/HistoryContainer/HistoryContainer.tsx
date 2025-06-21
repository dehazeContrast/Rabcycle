import React, { useState } from 'react'
import HistoryCard from '../HistoryCard/HistoryCard.tsx'
import waterImage from '../../assets/water.jpg';


const historyData = [
    {
        image: waterImage,
        info: 'June 20, 2025',
    },
    {
        image:waterImage,
        info: 'June 19, 2025',
    },
];

const HistoryContainer = () => {
    return (
        <div className="history-container">
            {historyData.map((entry, index) => (
            <HistoryCard key={index} image={entry.image} info={entry.info}/>
            ))}
        </div>
    );
};

export default HistoryContainer;