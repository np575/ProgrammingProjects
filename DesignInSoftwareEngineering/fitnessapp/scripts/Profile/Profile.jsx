import React, {useState,useEffect} from 'react';

import { ProfileCont } from './ProfileCont';

import { Socket } from '../Socket';

export function Profile(props) {
    const currentUser = props.currentUser;
    const isLoggingIn = props.isLoggingIn;
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    const quotes = props.quotes;
    
    return (
        <div id = 'Profile'>
            { currentUser.isLoggedIn?
                <ProfileCont currentUser = { currentUser } 
                                profileDetail = { profileDetail }
                                userWeight = { userWeight }
                                date = {props.date}
                                isLoggingIn = { isLoggingIn } 
                                quotes = { quotes }/>
                :
                <ProfileCont currentUser = { currentUser } 
                                profileDetail = { profileDetail }
                                userWeight = { userWeight }
                                date = {props.date}
                                isLoggingIn = { isLoggingIn }
                                quotes = { quotes }/>
            }
        <div id="footer">
              <img src={'/static/logo.png'} className = "logoImg" />
        </div>
        </div>
        );
}