/* eslint react/no-unescaped-entities: 0 */
import * as React from 'react';


export function About() {
    
    return (
        <div id = 'About'>
            <div className = 'a1'>
                <h1>Who We Are?</h1>
                <p>
                We aim to provide healthy food options, meal plans, workout plans, and also deliver a live chat feature accessible from the browser.
                This web app provides a secure Google login that allows users to identify themselves, a custom statistical profile for body macros,
                workouts, and a food search tool that shows a meal, its calorie count, preparation time and a link to the recepie. 
                This app also features a  live chat platform through which users can communicate with each other.<br/>
                </p>
            </div>
            <div className = 'a2'>
                <h1>Team Members</h1>
                <div className = 'team-intro'>
                    <div className = 'team-member'>
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
                        <img src="./static/Andy.png" className="member-picture"/>
                        <h4>Andy Martinez</h4>
                        <div className="logos">
                        <a href="https://github.com/senorando" target="_blank" className="git-logo" rel="noreferrer" ><i className="fa fa-github" ></i></a>
                        <a href="https://www.linkedin.com/in/Andy-Martinez-/" target="_blank" rel="noreferrer" ><i className="fa fa-linkedin" ></i></a>
                        </div>
                       
                        <p>
                            Hi, I'm Andy! I came up with the idea of this app because as someone into fitness, 
                            I want to have a good fitness app that has all aspects combined into it, nutrition and exercise.
                            I handled a lot of the backend and frontend of the app and orchestrated the database persistence on the app. 
                            I also created the fitness API/database from scratch since we couldn't find an API online.
                            I've enjoyed making this app despite the difficulties it's had and I'm looking forward to more full stack development in the future!
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Oreo.png" className="member-picture"/>
                        <h4>Oreoluwa Akeredolu</h4>
                        <div className="logos">
                        <a href="https://github.com/atorisemofe" target="_blank" rel="noreferrer" ><i className="fa fa-github" ></i></a>
                        <a href="https://www.linkedin.com/in/Oreoluwa-Akeredolu/" target="_blank" rel="noreferrer" ><i className="fa fa-linkedin" ></i></a>
                        </div>
                        <p>
                            Hello, I'm Oreoluwa Akeredolu. I'm a current student at NJIT persuing a degree in Computer Science.
                            I enjoy the process of problem solving, which has lead me down the path to absolutely adoring
                            all aspects of the software development process.  Working on this project has absolutely
                            exposed me to learning new technoloiges and how it is to truly work in a team enviroment.
                            I'm glad to be working with such an awesome team.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Jinal.png" className="member-picture"/>
                        <h4>Jinal patel</h4>
                        <div className="logos">
                        <a href="https://github.com/jsp88" target="_blank" rel="noreferrer" ><i className="fa fa-github" ></i></a>
                        <a href="https://www.linkedin.com/in/jinal-patel-07/" target="_blank" rel="noreferrer" ><i className="fa fa-linkedin" ></i></a>
                        </div>
                        <p>
                            Hello, I'm Jinal Patel. I'm a current student at NJIT pursuing a degree in Computer Science. 
                            I'm extremely eager to introduce our site that me and my team member has been dealing with.
                            I enjoyed working on the frontend development part of this project and gained knowlage in the backend development while learning new technologies.
                            This was a perfect opportunity to demostrate valueable skills such as team collaboration and leadership.
                        </p>
                    </div>
                    <div className = 'team-member'>
                        <img src="./static/Nisrag.png" className="member-picture"/>
                        <h4>Nisrag Patel</h4>
                        <div className="logos">
                        <a href="https://github.com/np575" target="_blank" rel="noreferrer" ><i className="fa fa-github" ></i></a>
                        <a href="https://www.linkedin.com/in/nisarg-patel-/" target="_blank" rel="noreferrer" ><i className="fa fa-linkedin" ></i></a>
                        </div>
                        <p>
                            Hello, I'm Nisarg Patel. I'm a rising senior at NJIT persuing a degree in Computer Science.
                            I enjoy working on the team enviroment while showcasing my skills and learning form others.
                            I implemented most of the logic in the backend code and handled front-end functionalities in the project.  
                            Building this project, collaborating with the team and an industrial mentor who taught me various new technologies
                            and how they work has been a wonderful experience.
                            I now look forward to improving my skills and practice in fullstack development.<br/>
                        </p>
                    </div>
                </div>
            </div>
            <div className = "a4">
                <h1>Frequently Asked Questions</h1>
                <div className="container">
                <div className="box box-1">
                    <h2>How did we make Gut Buster?</h2>
                    <p>
                    A list of the most notable technologies used in this web-app are included at the bottom of this page.<br/><br/>
                    For the backend, the main programming language we used was Python. With Python, we utilized the Flask Micro-Framework 
                    to serve web pages. Along with this, we used socket.io to interface between the front-end and the back-end. Persistence 
                    was achieved using Postgresql and SQLAlchemy to provide an easy interface to interact with the database via Python.<br/><br/>
                    Comments are stored in the database, as well as future user information and preferences. For the front-end, the main technology that 
                    we used was functional React.js, as well as some vanilla HTML, CSS, and Javascript. A number of different packages were
                    utilized with React as well, which can be found on the Github page.<br/><br/>
                    Collaboration was utilized using Git and Github. Final deployment of this web app was done on Heroku.
                    </p>
                </div>
                
                <div className="box box-2">
                    <h2>Why did we create Gut Buster?</h2>
                    <p>
                    Our goal for the users of The Gut Buster is to provide them with the information needed on a daily basis as it pertains to their health and fitness.<br/><br/>
                    Nowadays, a lot of the information people use in their day-to-day lives is spread across a variety of different applications, making it is very difficult
                    to locate the specific information needed from fitness apps.<br/><br/>
                    However, with The Gut Buster, we aim to provide a healthier lifestyle and help our clients achieve their health goals effectively by tracking body measurements
                    and workout patterns.<br/><br/>
                    Gut Buster offers its clients many benefits like helping them monitor their daily diet needs and progress. Gut Buster also provides a tool to improve lifestyle habits
                    through constant reminders about health goals, thus keeping clients motivated.
                    </p>

                </div>
            </div>
            </div>
            <div className = "a3">
                <h1>Technologies</h1>
                <div className="technologies">
                    <ul className="technologies-list">
                        <li>
                            <a href="https://flask.palletsprojects.com/en/1.1.x/"rel="noreferrer"  target="_blank">Python Flask</a><br/>
                            <a href="https://reactjs.org/"rel="noreferrer"  target="_blank">React.js</a><br/>
                            <a href="https://www.postgresql.org/" rel="noreferrer" target="_blank">Postgresql</a><br/>
                            <a href="https://www.heroku.com/" rel="noreferrer" target="_blank">Heroku</a><br/>
                            <a href="https://circleci.com/" rel="noreferrer" target="_blank">Circle CI</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
}