import React, { useState, useEffect } from 'react';

import { MacrosChart } from './MacrosChart';
import { WeightGraph } from './WeightGraph';
import { UpdateForm } from './UpdateForm';
import { Socket } from '../Socket';
import { UserForm } from '../UserForm';

export function ProfileCont(props){
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    const isLoggingIn = props.isLoggingIn;
    const quotes = props.quotes;
    
    function updateStatus() {
        console.log('isEdit: ' + isEdit);
        setStatus((prevStatus) => !isEdit);
    }
    Socket.on('not editing', (data) => {
        console.log(data);
        setStatus(false);
    });
    Socket.off('not editing', '');
    
    return (
        <div id = 'ProfileContent'>
            <div id = 'Left'>
                <div className = 'UserDetails'>
                    <h3> { currentUser.name } </h3><br/>
                    <h3> Goal: {profileDetail.goal_weight} </h3> <br/>
                    <p>
                        Height: { profileDetail.height } <br/>
                        Weight: { userWeight[ userWeight.length - 1 ] } <br/>
                        Age: { profileDetail.age } <br/>
                        Gender: { profileDetail.gender } <br/>
                        Activity Level: { profileDetail.activityLevel } <br/>
                        BMR: { profileDetail.bmr } <br/>
                    </p>
                    { isEdit? 
                        <UpdateForm currentUser = { currentUser }/>
                        :
                        currentUser.isLoggedIn?
                            <button id = 'UpdateButton' onClick = { updateStatus }>Add New Weight Entry</button>
                            :
                            <button id = 'UpdateButton' onClick = { updateStatus } disabled>Add New Weight Entry</button>
                    }
                </div>
                <MacrosChart profileDetail = { profileDetail } />
            </div>
            { currentUser.isLoggedIn?
                <div id = 'Middle'>
                    <h2><i> "{ quotes }" </i></h2>
                </div>
                
                :
                <div id = 'Middle'>
                    <h2 id = 'SampleProfile'>You are viewing a sample profile!<br/>Please Login to see your data!</h2>
                    { isLoggingIn?
                        <UserForm />
                        :
                         <div id = 'Blank'>blank</div>
                    }
                </div>
                }
            <div id = 'Right'>
                <WeightGraph userWeight = { props.userWeight } goal_weight= {profileDetail.goal_weight} date = {props.date} />
                <div className = 'RecommendedMeals'>
                    <h3>Recommended Meals based on your macros</h3>
                    <p>
                        Breakfast: { profileDetail.breakfastMeal } <br/>
                        Lunch: { profileDetail.lunchMeal } <br/>
                        Dinner: { profileDetail.dinnerMeal } <br/>
                        Total Calories: { profileDetail.calMeal } <br/>
                        Total Protein: { profileDetail.protMeal } <br/>
                        Total Carbs: { profileDetail.carbMeal } <br/>
                        Total Fat: { profileDetail.fatMeal } <br/>
                    </p>
                </div>
            </div>               
        </div>
    );
}