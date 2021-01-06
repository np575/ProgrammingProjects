# Livechatapp-Nisarg Patel

This repository demostrates an sample public chat application with both the client-server connection with the use of Socket.io, React.js with the Flask (Python),HTML,CSS on AWS Cloud9. The python being the server as the backend and the React is for the client side.
The final version of the app is deployed on Heroku which can be found by clicking here: https://hidden-lowlands-04121.herokuapp.com/ (Please Full-screen the App in a new tab preferrebaly Google Chrome and set the zoom to 100% because of css it might look differently in other devices. Also configure cookie settings, chrome://settings/content/cookies  

Prerequisite: Flask, Python, HTML/CSS,React,Socket.io, knowledge in API, Google Oauth log-in.

# To use this repository and deploy the app, you must follow these steps:

# Set up React  
0. `cd ~/environment && git clone https://github.com/Sresht/lect11-starter/ && cd lect11-starter`    
1. Install your stuff!    
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`    
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` :warning: :warning: :warning:    
2. If you already have psql set up, **SKIP THE REST OF THE STEPS AND JUST DO THE FOLLOWING COMMAND**:   
`sudo service postgresql start`    
3. Copy your `sql.env` file into your new directory.
  
# Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo /usr/local/bin/pip install --upgrade pip`  
3. Get psycopg2: `sudo /usr/local/bin/pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`    
  
# Setting up PSQL  
  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:    
    a) `psql` (if you already quit out of psql)    
    ## REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.   
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!  
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`    
    c) `\q` to quit out of sql    
8. `cd` into `lect11` and make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it  
9. Fill in those values with the values you put in 7. b)  
  
  
# Enabling read/write from SQLAlchemy  
There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)   
  
# This steps shows how the Unittesting was done in this repository.

# Steps to get coverage running for the pylint: Coverage Report
0. coverage run -m --source=. unittest tests/*.py
1. coverage html
3. A new fiule should get created called htmlcov/index.html
4. Preview that file to check the Coverage Report.

# Steps to install necessary tools to install pylint and eslint
0. pip install pylint
1. pip install black
2. npm install -g eslint
3. npm init
* press enter to accept all default values
4. eslint --init
"To check syntax, find problems, and enforce code style"
"JavaScript modules (import/export)"
"React"
"Browser"
"Use a popular style guide"
"Javascript"
"Yes" in the end.

# Steps to check all the files using pylint and estlint
0. pylint <python files> for example: python app.py
1. estlint <jsx files> for example: estlint Button.jsx
* eslint --fix Button.jsx to fix some of the errors.
  
# Steps to run both unittest files under tests
0. python unmocked_unit_tests.py
1. python mocked_unit_tests.py
