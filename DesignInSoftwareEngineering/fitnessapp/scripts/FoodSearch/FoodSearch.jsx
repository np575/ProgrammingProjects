/* eslint react/prop-types: 0 */
import React, { useState, useEffect } from 'react';
import { UserForm } from '../UserForm';
import { Socket } from '../Socket';
import SearchField from "react-search-field";

export function FoodSearch(props) {
    const isLoggingIn = props.isLoggingIn;
    const isLoggedIn = props.currentUser.isLoggedIn;
    const currentUser = props.currentUser;
    
    function onClickAlert(){
        alert("Please Login");
    }
    
    function handleSubmit(response) {
        console.log(response);
        let name = response;
        let user = currentUser.email;
        Socket.emit('new food search', {
          'food_search': name,
          'user': user
        });
       console.log('Sent the food ' + name + user + ' to server!');
       setOnClick(true);
    }
    
    const [onClick, setOnClick] = useState(false);
    
    const [food, setFoods] = useState([]);
    const [ingredient, setIngredient] = useState([]);
    const [prep, setPrep] = useState([]);
    const [image, setImage] = useState([]);
    const [calorie, setCalorie] = useState([]);
    
    
    const [food1, setFoods1] = useState([]);
    const [ingredient1, setIngredient1] = useState([]);
    const [prep1, setPrep1] = useState([]);
    const [image1, setImage1] = useState([]);
    const [calorie1, setCalorie1] = useState([]);
    
    const [food2, setFoods2] = useState([]);
    const [ingredient2, setIngredient2] = useState([]);
    const [prep2, setPrep2] = useState([]);
    const [image2, setImage2] = useState([]);
    const [calorie2, setCalorie2] = useState([]);
    
    const [food3, setFoods3] = useState([]);
    const [ingredient3, setIngredient3] = useState([]);
    const [prep3, setPrep3] = useState([]);
    const [image3, setImage3] = useState([]);
    const [calorie3, setCalorie3] = useState([]);
    
    const [food4, setFoods4] = useState([]);
    const [ingredient4, setIngredient4] = useState([]);
    const [prep4, setPrep4] = useState([]);
    const [image4, setImage4] = useState([]);
    const [calorie4, setCalorie4] = useState([]);
   
    const [food5, setFoods5] = useState([]);
    const [ingredient5, setIngredient5] = useState([]);
    const [prep5, setPrep5] = useState([]);
    const [image5, setImage5] = useState([]);   
    const [calorie5, setCalorie5] = useState([]);

    function GetFoodResponse() {
        useEffect(() => {
            Socket.on('food response', (data) => {
                setFoods(data[0][0]);
                setPrep(data[0][1] + " minutes prep time");
                setIngredient(data[0][2]);
                setImage(data[0][3]);
                setCalorie(data[0][4] + " calories");

                setFoods1(data[1][0]);
                setPrep1(data[1][1] + " minutes prep time");
                setIngredient1(data[1][2]);
                setImage1(data[1][3]);
                setCalorie1(data[1][4] + " calories");
                
                setFoods2(data[2][0]);
                setPrep2(data[2][1] + " minutes prep time");
                setIngredient2(data[2][2]);
                setImage2(data[2][3]);
                setCalorie2(data[2][4] + " calories");
                
                setFoods3(data[3][0]);
                setPrep3(data[3][1] + " minutes prep time");
                setIngredient3(data[3][2]);
                setImage3(data[3][3]);
                setCalorie3(data[3][4] + " calories");
                
                setFoods4(data[4][0]);
                setPrep4(data[4][1] + " minutes prep time");
                setIngredient4(data[4][2]);
                setImage4(data[4][3]);
                setCalorie4(data[4][4] + " calories");
                
                setFoods5(data[5][0]);
                setPrep5(data[5][1] + " minutes prep time");
                setIngredient5(data[5][2]);
                setImage5(data[5][3]);
                setCalorie5(data[5][4] + " calories");
                
            });
            Socket.off('food response', '');
        }, []);
    }
   
   GetFoodResponse();
   
   
        
    return (
         <div id = 'FoodSearch'>
            <div className="img1">
             <img src={'../static/eat-right.png'} alt="Logo"
                style={{float: 'right',
                        position: 'relative',
                        width: 550
                        }}
            />
            </div>
            { isLoggingIn?
                <div id = 'UserForm'>
                    <UserForm />
                </div>
                :
                <div id = 'SearchContent'>
                    <h2>Food Search</h2>
                    { isLoggedIn?
                        <div>
                            <SearchField
                                  placeholder="Search..."
                                  classNames="test-class"
                                  onSearchClick={handleSubmit}
                                /><br/>
                            <br/>
                            { onClick?
                                <div>
                                    <div className = 'food-result'>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient} rel="noreferrer">{food}</a><br/>
                                        {calorie}<br/>
                                        {prep}<br/><br/>
                                        <img src= {image} alt = 'No image found :('/></span><br/>
                                </div>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient1}rel="noreferrer" >{food1}</a><br/>
                                        {calorie1}<br/>
                                        {prep1}<br/><br/>
                                        <img src= {image1} alt = 'No image found :('/></span><br/>
                                </div>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient2} rel="noreferrer" >{food2}</a><br/>
                                        {calorie2}<br/>
                                        {prep2}<br/><br/>
                                        <img src= {image2} alt = 'No image found :('/></span><br/>
                                </div>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient3} rel="noreferrer" >{food3}</a><br/>
                                        {calorie3}<br/>
                                        {prep3}<br/><br/>
                                        <img src= {image3} alt = 'No image found :('/></span><br/>
                                </div>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient4} rel="noreferrer" >{food4}</a><br/>
                                        {calorie4}<br/>
                                        {prep4}<br/><br/>
                                        <img src= {image4} alt = 'No image found :('/></span><br/>
                                </div>
                                <div className="food-list">
                                    <span><a target="_blank" href={ingredient5} rel="noreferrer" >{food5}</a><br/>
                                        {calorie5}<br/>
                                        {prep5}<br/><br/>
                                        <img src= {image5} alt = 'No image found :('/></span><br/>
                                </div>
                            </div>
                                </div>
                                :
                                <div className = 'sample-search'>
                                    <p>Use search field above</p>
                                </div>
                            }
                        </div>
                        :
                        <div>
                            <SearchField
                                  placeholder="please login to search..."
                                  classNames="test-class"
                                  onSearchClick={onClickAlert}
                                /><br/>
                            <div className = 'sample-search'>
                                <p>You are Viewing a sample food search! Please login to perform a custom search</p>
                            </div>
                            <div className = 'food-result1'>
                                <div className="food-list1">
                                    <span><a target="_blank" href='http://www.foodista.com/recipe/3X3HYGB4/skirt-steak-fajitas' rel="noreferrer" >Skirt Steak Fajitas</a><br/>
                                        696 calories<br/>
                                        45 minutes prep time<br/><br/>
                                        <img src= 'https://spoonacular.com/recipeImages/660234-312x150.jpg'/></span><br/>
                                </div>
                                <div className="food-list1">
                                    <span><a target="_blank" href='https://www.foodista.com/recipe/Y5X6DRHT/pasta-with-chicken-and-broccoli' rel="noreferrer" >Pasta With Chicken and Broccoli</a><br/>
                                        331 calories<br/>
                                        45 minutes prep time<br/><br/>
                                        <img src= 'https://spoonacular.com/recipeImages/654901-312x150.jpg'/></span><br/>
                                </div>
                                <div className="food-list1">
                                    <span><a target="_blank" href='https://www.foodista.com/recipe/C75THTG5/rice-pudding' rel="noreferrer" >Rice Pudding</a><br/>
                                        407 calories<br/>
                                        45 minutes prep time<br/><br/>
                                        <img src= 'https://spoonacular.com/recipeImages/658276-312x150.jpg'/></span><br/>
                                </div>
                            </div>
                        </div>
                    }
                </div>
            }
         <div id="footer">
              <img src={'/static/logo.png'} className = "logoImg" />
        </div>
        </div>
        );
}