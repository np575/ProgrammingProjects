
import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newAddress = document.getElementById("address_input");
   
    // TODO- send the address on. a socket to the server
    Socket.emit('new address input',{
        'address': newAddress.value+'',});
    
    
    console.log('Sent the address ' + newAddress.value + ' to server!');
    newAddress.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <div className="bottom container">
            
            <h4> Please enter the text you want to write: </h4>    
            <input id="address_input" placeholder="Enter a Text! "></input>
            <div className="buttonbucket">
            <button>Submit</button>
            </div>
            </div>
        </form>
    );
}
