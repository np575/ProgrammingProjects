import React, { useState } from "react";
import { Socket } from './Socket';
import ReactDOM from 'react-dom';

export function UserForm(){
    const [newUsr,setUsr]=useState('');
    Socket.on('new form',(data)=>{
       setUsr(data); 
    });
    Socket.off('new form',' ');
    function handleSubmit(event) {
        let response = '';
        let count = 0;
        
        if (document.getElementById("birthday").value == "" ){
            response += 'Birthday, ';
            count++;
        }
        if (document.getElementById("height_feet").value == ""){
            if(count == 0) {
                response += 'Feet, ';
            }else {
                response += 'feet, ';
            }
            count++;
        }
        if (document.getElementById("height_inches").value == "" ){
            if(count == 0) {
                response += 'Inches, ';
            }else {
                response += 'inches, ';
            }
            count++;
        }
        if (document.getElementById("weight").value == ""  ){
            if(count == 0) {
                response += 'Weight, ';
            }else {
                response += 'weight, ';
            }
            count++;
        }
        if (document.getElementById("gender").value == "0"){
            if(count == 0) {
                response += 'Gender, ';
            }else {
                response += 'gender, ';
            }
            count++;
        }   
        if (document.getElementById("GoalWeight").value == "" ){
            if(count == 0) {
                response += 'Goal Weight, ';
            }else {
                response += 'goal weight, ';
            }
            count++;
        } 
        if (document.getElementById("ActivityLevel").value == "0"){
            if(count == 0) {
                response += 'Activity level, ';
            }else {
                response += 'activity level ';
            }
            count++;
        }
        if (count > 0) {
            response += 'must have a value either inputted or selected!';
            alert(response);
        }
       else{
        let birthday = document.getElementById("birthday").value;
        console.log('Birthday: ' + birthday);
        let height_feet = parseInt(document.getElementById("height_feet").value);
        let height_inch =parseInt(document.getElementById("height_inches").value);
        let weight = parseFloat(document.getElementById("weight").value);
        let gender = document.getElementById("gender").value;
        let goal_weight = parseFloat(document.getElementById("GoalWeight").value);
        let activityLevel = document.getElementById("ActivityLevel").value;
        
        let height = (height_feet * 12 ) + height_inch;
       
        Socket.emit('new user input',{
          'birthday': birthday,
          'height': height,
          'weight': weight,
          'gender': gender,
          'goal_weight': goal_weight,
          'activityLevel': activityLevel,
          'name': newUsr.name,
          'email': newUsr.email,
          'imgUrl': newUsr.imgUrl,
        });
       }
        event.preventDefault();
    }
    return(
      <div id = 'UserForm'>
        <h4>Welcome { newUsr.name }!<br/>Please fill out the form below to get started</h4>
        <div className = 'Form'>
            <form onSubmit={handleSubmit}>
                Birthday: <input type="date"  id="birthday" name="birthday"/><br/>
                Height: <input type="number" id="height_feet" placeholder="feet"  name="height"/>{ ' \' ' } 
                        <input placeholder="inches" id="height_inches"/>{ ' \"' }<br/>
                Weight: <input type="float" id="weight"  placeholder="lbs" /> lbs<br/>
                Gender: <select id="gender">
                            <option value="0">{'<-Please select your gender->'}</option>
                            <option value="Man">Male</option>
                            <option value="Woman">Female</option>
                        </select><br/>
               Goal Weight: <input type="float" id= "GoalWeight" placeholder="lbs"/> lbs<br/>
               Activity Level: <select id="ActivityLevel">
                        <option value="0">{'<-Please select an activity level->'}</option>
                        <option value="1"> Sedentary: little to no exercise a week</option>
                        <option value="2"> Not Very Active: 1 - 3 times a week</option>
                        <option value="4"> Somewhat Active: 3 - 4 times a week</option>
                        <option value="3"> Active: 4 - 5 times a week</option>
                        <option value="5"> Very Active: 6 times a week</option>
                    </select><br/>
                <button type="submit" value="Submit">Submit</button>
            </form>
        </div>
      </div>
        );
    }