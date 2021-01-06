import React, { useState } from "react";

import { UserForm } from "../UserForm";
import { Chat } from '../Chat/Chat';

export function HomeCont(props) {
  const currentUser = props.currentUser;
  const isLoggingIn = props.isLoggingIn;

  return (
    <div id = 'HomeContent'>
      { isLoggingIn?
        <UserForm />
        :
        <div className = 'Home'>
          { currentUser.isLoggedIn?
            <h3>Welcome { currentUser.name }</h3>              
            :
            <h3>Welcome! Please login to use Gut Buster</h3>
          }
          <div>
            <ul>
              <li>Gut Buster is a great fitness tool that satisfies all of your workout and dieting needs.</li><br/><br/>
              <li>Once signed in you can view your profile, and interact with other active users through our chat feature.</li><br/><br/>
              <li>Once logged in you will be shown a secure form thats requires information such as birthday, height, weight, goal weight, and activity level.</li><br/><br/>
              <li>Visit  your Profile where our cutting edge software provides statistical information such as such as pie-charts for your macros, 
              a line graph for your goal weight, and the recommended meals based on your macros.</li> <br/><br/>
              <li>Visit the Workout platform to generate a custom workout plan for the week.</li><br/><br/>
              <li>Naviagte to the Food Search Page to browse various meals. Each meal shows its 
              calorie count, preperation time, and a link to the recepie.</li><br/>
          </ul>
          </div>
        </div>
      }
      <Chat currentUser = { currentUser } message = { props.message }/>
    </div>
    );
}
