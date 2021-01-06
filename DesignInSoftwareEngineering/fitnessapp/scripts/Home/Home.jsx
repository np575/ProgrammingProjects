import React, { useState } from "react";

import { Socket } from '../Socket';

import { HomeCont } from './HomeCont';

export function Home(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;
  
  return (
    <div id = 'Home'>
        <HomeCont currentUser = { currentUser } 
                  isLoggingIn = { isLoggingIn }
                  message = { props.message }/>
        <div id="footer">
             <img src={'/static/logo.png'} className = "logoImg" />
        </div>
    </div>
    );
}
    
