import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import { Content } from './Content';
// or
//import { GoogleLogin } from 'react-google-login';
 
 
// const responseGoogle = (response) => {
//   console.log(response);
// }
 


 function handleSubmit(response) {
  
    
  let name = response.profileObj.name;
  let profile = response.profileObj.imageUrl;
  
  
   Socket.emit('new google user', {
       'name': name , 'picture' : profile   //name and profile
    });
   
   
   
   
   
    
   console.log('Sent the name ' + name + ' to server!');
   console.log('Sent the image ' + profile + ' to server!');
   
   ReactDOM.render(<Content />, document.getElementById('content'));
   
   
}

 export function GoogleButton() {
  
  
  return( <GoogleLogin
    clientId="235867645579-gs14jqdef78eh8fads7d6ul1qv5gmf1r.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={handleSubmit}
    onFailure={handleSubmit}
    cookiePolicy={'single_host_origin'}
    className="gbutton"
    
  />);
}





