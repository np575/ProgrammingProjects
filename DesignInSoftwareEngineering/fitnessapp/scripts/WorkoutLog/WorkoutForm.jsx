/* eslint react/prop-types: 0 */
import React from 'react';

import { Socket } from '../Socket';

export function WorkoutForm(props) {
    const currentUser = props.currentUser;
    
    function handleSubmit(event) {
        let level = parseInt(document.getElementById("DifficultyLevel").value);
        let split = document.getElementById("split").value;
        let email = currentUser.email
        if (split == "" ){
            alert('Please type in a valid split');
        }
        if (document.getElementById("DifficultyLevel").value == "0"){
            alert('Please choose valid Difficulty Level');
        }
        if(email == '')
        {
            alert('Please login first, After that fill out this form.');
        }
        else{
            Socket.emit('workout entry',{
              'level': level,
              'split': split,
              'email': currentUser.email,
              'name': currentUser.name,
              'sid': currentUser.sid
            });
        }
        event.preventDefault();
    }

    return (
        <div id = 'WorkoutForm' className = 'Form'>
            <h3>Workout Entry</h3><br/>
            <form onSubmit={ handleSubmit }>
                Difficulty Level: <select id="DifficultyLevel">
                        <option value="0">{'<-Please select your workout experience->'}</option>
                        <option value="1"> 1 - Beginner</option>
                        <option value="2"> 2 - Intermediate</option>
                        <option value="3"> 3 - Advanced</option>
                    </select><br/><br/>
                Choose Workout Splits: <select id="split">
                        <option value="">{'<-Please Choose A Workout Split->'}</option>
                        <option value="Bro Split"> Bro Split (4 days/week)</option>
                        <option value="Full Body"> Full Body (2 - 3 days/week)</option>
                        <option value="Push/Pull/Legs"> Push/Pull/Legs (3 or 6 days/week)</option>
                        <option value="Upper/Lower"> Upper/Lower (2, 4, or 6 days/week)</option>
                    </select><br/><br/>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}