import React, { useState } from 'react'
import HistoryCard from '../HistoryCard/HistoryCard.tsx'
import  './HistoryContainer.css'
import waterImage from '../../assets/water.jpg';


//Temp hard-coded data to pull from
const historyData = [
    {
        image: waterImage,
        info: 'June 20, 2025',
    },
    {
        image:waterImage,
        info: 'June 19, 2025',
    },
        {
        image:waterImage,
        info: 'June 18, 2025',
    },
        {
        image:waterImage,
        info: 'June 17, 2025',
    },
        {
        image:waterImage,
        info: 'June 16, 2025',
    },
        {
        image:waterImage,
        info: 'June 15, 2025',
    },
        {
        image:waterImage,
        info: 'June 14, 2025',
    },
        {
        image:waterImage,
        info: 'June 13, 2025',
    },
];

const HistoryContainer = () => {
    return (
        <div className="history-container">
            <title>History</title>
            {historyData.map((entry, index) => (
            <HistoryCard key={index} image={entry.image} info={entry.info}/>
            ))}
        </div>
    );
};

export default HistoryContainer;