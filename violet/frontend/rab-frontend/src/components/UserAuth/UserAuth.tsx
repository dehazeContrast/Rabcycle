import React from 'react'
import './UserAuth.css';
import password_icon from '../../assets/lock_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png'
import mail_icon from '../../assets/mail_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png'
import user_icon from '../../assets/person_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png'

const UserAuth = () => {
    return (
        <div className='container'>
            <div className="header">
                <div className="text">Sign Up</div>
                <div className="underline"></div>
            </div>
            <div className="inputs">
                <div className = "input">
                    <img src={user_icon} alt="" />
                    <input type="text" />
                </div>
                <div className = "input">
                    <img src={mail_icon} alt="" />
                    <input type="email" />
                </div>
                <div className = "input">
                    <img src={password_icon} alt="" />
                    <input type="password" />
                </div>
            </div>
        </div>
    );
};

export default UserAuth;