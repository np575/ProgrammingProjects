  
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [usercount, setUsercount] = React.useState([]);
    const [name, setName] = React.useState([]);
    const [profile, setProfile] = React.useState([]);
    const [userlink, setUserlink] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('input received', (data) => {
                console.log("Received addresses from server: " + data['allAddresses']);
                setAddresses(data['allAddresses']);
            })
        });
    }
    
    
    function getusercount() {
        React.useEffect(() => {
            Socket.on('connected', (data) => {
                console.log("Received addresses from server for connect: " +data['test'] );
                setUsercount(data['test']); 
            })
        });
    }
    
    
    
     function getuserlink() {
        React.useEffect(() => {
            Socket.on('new address', (data) => {
                console.log("Received addresses from server for connect: " + data['keylink'] );
                setUserlink(data['keylink']); 
            })
        });
    }
    
    
     function getusername() {
        React.useEffect(() => {
            Socket.on('username', (data) => {
                console.log("Received username from server: " + data['user_name']);
                setName(data['user_name']);
                
            })
        });
    }
    
    function getusercountdisconnect() {
        React.useEffect(() => {
            Socket.on('disconnected', (data) => {
                console.log("Received addresses from server for disconnect: " + data['test']);
                setUsercount(data['test']);
            })
        });
    }
    
      function getuserimage() {
        React.useEffect(() => {
            Socket.on('new google image', (data) => {
                console.log("Received addresses from server for connect: " + data['image'] );
                setProfile(data['image']); 
            })
        });
    }
    
    
    getusercount();
    getNewMessages();
    getusercount();
    getusercountdisconnect();
    getusername();
    getuserimage();
    getuserlink();
    
    return (
         <div>
      <h1>Sample Chat app </h1>
      <h1>Active User Count: {usercount}</h1>
      <h1> Bot is Present Please type-> !! help for more information</h1>
      
      <ol>
      {
          addresses.map((address, index) =>  
          <h3 key={index}><img src={profile} width="30" height="30"/>{address}</h3>)
      }
      
       {
           userlink.map((keylink, index) =>
            <h3 key={index}>clickable link: <a href={keylink} target="_blank">{keylink}</a> </h3> )
          //both image or url is clickable   
      }
      </ol>
      <Button />
      </div>
    );
}
