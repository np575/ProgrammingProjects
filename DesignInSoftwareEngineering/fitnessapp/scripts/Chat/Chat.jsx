/* eslint react/prop-types: 0 */
import React, { useEffect } from "react";
import { animateScroll } from 'react-scroll';

import { Button } from './Button';


export function Chat(props) {
  const currentUser = props.currentUser;
  const message = props.message;

  function scroll() {
    animateScroll.scrollToBottom({
      containerId: 'Message_List',
    });
  }
  useEffect(() => { scroll(); }, []);
  return (
    <div id = 'ChatBox'>
        <h3>Live Chat</h3>
        <ul id = 'Message_List'>
          { message.map((message, index) => {
            if( message.email === currentUser.email ){
              return (
                <li id = 'MessageSelf' key={index}>
                  <span id = 'SelfText'>
                    {message.text}
                  </span><br/>
                  <span id = "MessageTime">{ message.time }</span>
              </li>
              );
            }
            return (
              <li id = 'MessageOthers' key={index}>
                { message.email !== message.prev_email?
                  <div id = 'MessageHead'><img id = 'Profile_Pic' src={message.image}/>
                    <strong>{message.name}</strong>
                  </div>
                  :
                  <div id = 'FakeHead'></div>
                }
                <div id = 'OthersCont'>
                  <span id = 'OthersText'>
                    {message.text}
                  </span><br/>
                  <span id = "MessageTime">{ message.time }</span>
                </div>
                </li>
              ); 
          })}
        </ul>
        <Button currentUser = { currentUser } />
    </div>
    );
}