    
import * as React from 'react';
import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';

export function ContentGoogle() {
   const [addresses, setAddresses] = React.useState([]);
   // const [usercount, setUsercount] = React.useState([]);
    
      //const [name, setName] = React.useState([]);
      
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('input received', (data) => {
                console.log("Received addresses from server: " + data['allAddresses']);
                setAddresses(data['allAddresses']);
            })
        });
    }

    
    getNewMessages();
   
    
    return (
    
        
    <div>
      <h1>Sample Chat app</h1>
      <h1> Please Authenicate yourself first to chat </h1>
     
     
      <GoogleButton />


     
      </div>
     
    );

}