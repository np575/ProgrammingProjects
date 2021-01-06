 ## Gut Buster
We aim to provide healthy food options, meal plans, workout plans, and also deliver a live chat feature accessible from the browser. This web app provides a secure Google login that allows users to identify themselves, a custom statistical profile for body macros, workouts, and a food search tool that shows a meal, its calorie count, preparation time and a link to the recepie. This app also features a live chat platform through which users can communicate with each other.

***
### Heroku Link
[Gut Buster](http://gut-buster-v2.herokuapp.com/)

# To use this repository and deploy the app, you must follow these steps:
1.Set up React
cd ~/environment && git clone https://github.com/senorando/project3-gut-buster && cd project3-gut-buster/
2.	Install your stuff!
a) npm install
b) pip install flask-socketio
c) pip install eventlet
d) npm install -g webpack
e) npm install --save-dev webpack
f) npm install socket.io-client --save
g) npm install 'react-scroll'
h) npm install recharts
⚠️ ⚠️ ⚠️ If you see any error messages, make sure you use sudo pip or sudo npm. If it says "pip cannot be found", run which pip and use sudo [path to pip from which pip] install ⚠️ ⚠️ ⚠️
3.	If you already have psql set up, SKIP THE REST OF THE STEPS AND JUST DO THE FOLLOWING COMMAND:
sudo service postgresql start
4.	Copy your sql.env file into your new directory.
Getting PSQL to work with Python
1.	Update yum: sudo yum update, and enter yes to all prompts
2.	Upgrade pip: sudo /usr/local/bin/pip install --upgrade pip
3.	Get psycopg2: sudo /usr/local/bin/pip install psycopg2-binary
4.	Get SQLAlchemy: sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1

# Setting up PSQL
1.	Install PostGreSQL: sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
Enter yes to all prompts.
2.	Initialize PSQL database: sudo service postgresql initdb
3.	Start PSQL: sudo service postgresql start
4.	Make a new superuser: sudo -u postgres createuser --superuser $USER
⚠️ ⚠️ ⚠️ If you get an error saying "could not change directory", that's okay! It worked! ⚠️ ⚠️ ⚠️
5.	Make a new database: sudo -u postgres createdb $USER
⚠️ ⚠️ ⚠️ If you get an error saying "could not change directory", that's okay! It worked! ⚠️ ⚠️ ⚠️
6.	Make sure your user shows up:
a) psql
b) \du look for ec2-user as a user
c) \l look for ec2-user as a database
7.	Make a new user:
a) psql (if you already quit out of psql)
REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.
b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!
create user [some_username_here] superuser password '[some_unique_new_password_here]';
c) \q to quit out of sql
8.	cd into lect11 and make a new file called sql.env and add SQL_USER= and SQL_PASSWORD= in it
9.	Fill in those values with the values you put in 7. b)
Enabling read/write from SQLAlchemy
There's a special file that you need to enable your db admin password to work for:
1.	Open the file in vim: sudo vim /var/lib/pgsql9/data/pg_hba.conf If that doesn't work: sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)
2.	Replace all values of ident with md5 in Vim: :%s/ident/md5/g
3.	After changing those lines, run sudo service postgresql restart
4.	Ensure that sql.env has the username/password of the superuser you created!

# Steps to get the Google oauth working
1.	Go to https://console.developers.google.com/ and sign up using your PERSONAL google account.
2.	Click "CREATE PROJECT" or in the dropdown menu called "Select a Project" in the top, click "NEW PROJECT".
3.	Make a new project wiht desired name. "No organization" is fine. 3.Click "Credentials" in the left hand bar, then click "+ CREATE CREDENTIALS" and then click "OAuth client ID".
4.	If you see a warning that says "To create an OAuth client ID, you must first set a product name on the consent screen", do the following steps: 1. Click the "CONFIGURE CONSENT SCREEN" button. 2. Choose "External" 3. For "Application name," specify the name you choose or something similar. 4. Press save. 5.Go back to Credentials -> Create Credentials -> OAuth client ID. Click "web application".
5.	insert both the links in Authorized JavaScript origins and Authorized redirect URIs and save you urls there where you want to run it.
6.	install google-react button by using npm install react-google-login.

# Steps to get the Spoonacular API working
1.  sign up for the Spoonacular API key by navigating to the https://spoonacular.com/food-api/console .
2. log in to your account and go to https://spoonacular.com/food-api/console#Profile and find your API keys and configureditin sql.env.

# Run the app first before deploying it on Heroku:
1.	Run your code!
a) npm run watch. If prompted to install webpack-cli, type "yes"
b) sudo service postgresql start to start psql services. c) In a new terminal, python app.py. d) Preview Running Application (might have to clear your cache by doing a hard refresh)

# Steps to deploy the app on Heroku:
0.Sign up for heroku at heroku.com | Install heroku by running npm install -g heroku. 1.Go through the following steps: heroku login -i && heroku create (this will give you the heroku app link) git push heroku master 
2. Configure your sql.env with your own DATABASE_URL.
 3. Run heroku addons:create heroku-postgresql:hobby-dev to setup the db for the heroku. 
4. Run PGUSER-SQL_USER heroku pg:push postgres DATABASE_URL | heroku pg:push postgres DATABASE_UR set up the heroku database build. 
5. herokupg:psql and check the table content by using select * from table_name. 
6.exit the psql by \q. 5. Add Procfile and requirements.txt to deploy the app on heroku. 7.. use pip freeze > requirements.txt && echo "web: python app.py" > Procfile. 
8. Use git git pull origin master && git push origin master. 
9.use git remote -v to make sure both git and heroku origin's are correct as you want. 
10.. then, push to heroku by git push heroku master.


#### Individual Work

1. Andy Martinez *senorando*  
i. Created the DB   
ii. Made the Home page  
iii. Created the conditional rendering on the home and profile pages  
iv. Managed current user on each client via sockets  
v. Cleaned up React by putting most of the HTML in components 
vi. Worked on fitness plan for user in backend.  
vii. Display elements for the weekly workout plan.   
viii. Setup CircleCI   

2. Jinal Patel *jsp88*  
i.   Initialize the html and jsx files  
ii.  Create add contents profiile.jsx  
iii. Create make form userform.jsx.  
iv.  Handle the frontend rendering for home.jsx and profile.jsx. 
v.   Implemented Pie chart and line graph and displayed on Profile Page. 
vi.  Made workour form and Setup database for the workout log.  
vii. style the app in general. 


3. Nisarg Patel *np575*  
i. Added jsx files for the flow of login/home/profile page.  
ii. Added logic for bmr and daily calorie needs based on fitness goal.  
iii. Figured out possible socket to client for bmr/daily calorie needs and Added sockets to fetch the information through API.  
iv. Fixed Backend logic and added input validation to the Userform.  
vi. Created The workout db to generate workout plan.Redo macro calculation after weight update on the profile page.
vii.Added the live chat feature with conditional rendering.  
viii. socket back the food search response to client and added tests for unmocked/mocked to increase coverage.Cleaned up python code using pylint and eslint.  

4. Oreoluwa Akeredolu *atorisemofe*  
i. Initialized app.py  
ii. Created navigation bar between all pages  
iii. Created Search bar for food search page  
iv. Created Spoonacular API call function to create meal plans  
v.  Cleaned up python code using pylint 
vi. Organized page elements with CSS.   
vii. Implemented landing page.  
viii. Set Logo in App.

***
