/* eslint react/prop-types: 0 */
import * as React from 'react';

import { Socket } from '../Socket';

export function Button(props) {
    const currentUser = props.currentUser;
    const isLoggedIn = props.currentUser.isLoggedIn;
    console.log(isLoggedIn);
    
    function handleSubmit(event) {
        let newtexts = document.getElementById("text_input");
  
        Socket.emit('new text input',{
            'entry': newtexts.value+'',
            'email': currentUser.email
        });
        
    console.log('Sent the message ' + newtexts.value + ' to server!');
    newtexts.value = ''
    event.preventDefault();
    }
    
    return (
        <div id = "TextBox">
            { isLoggedIn?
            <form className = 'TextInput' onSubmit={handleSubmit}>
                <input id = 'text_input' placeholder="Enter a Text! "></input>
                <button>Send!</button>
            </form>
            :
            <form className = 'TextInput'>
                <input placeholder="Login to send messages " disabled></input>
                <button disabled>Send!</button>
            </form>
            }
        </div>
    );
}
