import React from 'react';
import logo from './logo.svg';

import "./Profile.css"

function Profile() {
    return (
        <div className="Profile">
            <img src={logo} className="App-logo" alt="logo" />
            <div className='Name' >Femi Ogunkola
                <div class='date'> Joined 2022</div>
            </div>
            <div>
                <Statistics />
            </div>
            <div>
                <Statistics />
            </div>
            <div>
                <Statistics />
            </div>
            <div>
                <Statistics />
            </div>
        </div>
    )
}

function Statistics() {
    return (
        <div className='card'>
            <div className='card-field'>
                Owned
            </div>
            <div className='card-value'>
                5
            </div>
        </div>
    )
}

export default Profile