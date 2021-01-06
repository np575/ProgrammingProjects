"""app.py"""
# pylint: disable=C0116
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=W0612
from os.path import join, dirname
from dotenv import load_dotenv
import os, flask, flask_sqlalchemy, flask_socketio, datetime, pytz
from flask import request
from calories_count import bmr_cal, daily_caloric_need, calculate_macro
from spoonacular import foodsearch, mealplan
import workout
from quotes import return_quotes

MESSAGE_RECEIVED_CHANNEL = "message received"
app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)

DATABASE_URI = os.environ["DATABASE_URL"]

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()
import models

online_users = []
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def emit_all_messages(channel):
    db_messages = [db_message for db_message in db.session.query(models.Chat).all()]
    all_messages = []
    for i in range(0, len(db_messages)):
        msg = db_messages[i]
        usr = db.session.query(models.Users).filter_by(id=msg.user_id).scalar()
        if i > 0:
            prev_msg = db_messages[i - 1].user_id
        else:
            prev_msg = "none"
        all_messages.append(
            {
                "name": usr.name,
                "text": msg.text,
                "time": msg.time,
                "image": usr.imgUrl,
                "email": usr.id,
                "prev_email": prev_msg,
            }
        )
    socketio.emit(channel, {"allMessages": all_messages})


def calculate_age(birth_date):
    today = datetime.datetime.now()
    return int((today - birth_date).days / 365)


def get_user_details(user_email):
    current_user = db.session.query(models.Users).filter_by(id=user_email).scalar()
    macros = db.session.query(models.Macros).filter_by(email=current_user.id).scalar()

    date = str(datetime.datetime.now().date())
    lastlogin = str(current_user.date)
    lastlogin = lastlogin.replace("[('", "")
    lastlogin = lastlogin.replace("',)]", "")
    calories = str(
        (
            db.session.query(models.Macros)
            .filter_by(email=current_user.id)
            .scalar()
            .max_cal
        )
    )
    calories = calories.replace("[(", "")
    calories = calories.replace(",)]", "")
    age = calculate_age(current_user.birthday)
    if date > lastlogin:
        newmeal = mealplan(calories)
        meal = db.session.query(models.Meals).get(1)
        meal.breakfast = (newmeal["breakfast"],)
        meal.lunch = (newmeal["lunch"],)
        meal.dinner = (newmeal["dinner"],)
        meal.meal_cal = (newmeal["nutrients"]["calories"],)
        meal.meal_carb = (newmeal["nutrients"]["carbohydrates"],)
        meal.meal_prot = (newmeal["nutrients"]["protein"],)
        meal.meal_fat = (newmeal["nutrients"]["fat"],)
        meal.email = (current_user.id,)
        db.session.commit()
        user_details = {
            "id": current_user.id,
            "height": current_user.height,
            "age": age,
            "gender": current_user.gender,
            "activityLevel": current_user.activityLevel,
            "goal_weight": current_user.goal_weight,
            "bmr": macros.bmr,
            "maxCal": macros.max_cal,
            "maxProt": macros.max_prot,
            "maxCarb": macros.max_carb,
            "maxFat": macros.max_fat,
            "breakfastMeal": meal.breakfast,
            "lunchMeal": meal.lunch,
            "dinnerMeal": meal.dinner,
            "calMeal": meal.meal_cal,
            "carbMeal": meal.meal_carb,
            "protMeal": meal.meal_prot,
            "fatMeal": meal.meal_fat,
        }
        socketio.emit("profile details", user_details)
    else:
        meals = db.session.query(models.Meals).filter_by(email=current_user.id).scalar()
        user_details = {
            "id": current_user.id,
            "height": current_user.height,
            "age": age,
            "gender": current_user.gender,
            "activityLevel": current_user.activityLevel,
            "goal_weight": current_user.goal_weight,
            "bmr": macros.bmr,
            "maxCal": macros.max_cal,
            "maxProt": macros.max_prot,
            "maxCarb": macros.max_carb,
            "maxFat": macros.max_fat,
            "breakfastMeal": meals.breakfast,
            "lunchMeal": meals.lunch,
            "dinnerMeal": meals.dinner,
            "calMeal": meals.meal_cal,
            "carbMeal": meals.meal_carb,
            "protMeal": meals.meal_prot,
            "fatMeal": meals.meal_fat,
        }
        socketio.emit("profile details", user_details)


def emit_all_user_weights(user_email, sid):
    weights = []
    date = []
    for user_weight in (
        db.session.query(models.Weight).filter_by(email=user_email).all()
    ):
        weights.append(user_weight.weight)
        date.append(str(user_weight.id)[0:10])

    socketio.emit(
        "most recent weight",
        {
            "weight": weights,
            "date": date,
            "sid": sid,
        },
    )


def displaying_quotes():

    quotes = return_quotes()
    print(quotes)
    socketio.emit("quotes", quotes)


@socketio.on("new entry")
def on_new_entry(data):

    db.session.add(
        models.Weight(datetime.datetime.now(), data["weight"], data["email"])
    )
    db.session.commit()

    height_update = 0
    age = 0
    gender_update = ""

    user_email = data["email"]
    user_id = data["sid"]
    weight_update = data["weight"]
    user = db.session.query(models.Users).filter_by(id=user_email).scalar()

    height_update = user.height
    birth = user.birthday
    age = calculate_age(birth)
    gender = user.gender
    activityLevel = user.activityLevel
    goal_weight = user.goal_weight

    meal = db.session.query(models.Meals).filter_by(email=user_email).scalar()

    bmr = bmr_cal(weight_update, height_update, age, gender)
    print(bmr)
    calories_need = daily_caloric_need(bmr, int(activityLevel))
    print(calories_need)
    macro_update = calculate_macro(calories_need)
    print(macro_update)

    maxCal = macro_update["MaxCalories"]
    minCal = macro_update["MinCalories"]
    maxProtein = macro_update["MaxProtein"]
    minProtein = macro_update["MinProtein"]
    maxCarbs = macro_update["MaxCarbs"]
    maxFat = macro_update["MaxFat"]
    minFat = macro_update["MinFat"]

    data = {
        "id": user.id,
        "height": height_update,
        "age": age,
        "gender": gender,
        "activityLevel": activityLevel,
        "goal_weight": goal_weight,
        "bmr": bmr,
        "maxCal": maxCal,
        "maxProt": maxProtein,
        "maxCarb": maxCarbs,
        "maxFat": maxFat,
        "breakfastMeal": meal.breakfast,
        "lunchMeal": meal.lunch,
        "dinnerMeal": meal.dinner,
        "calMeal": meal.meal_cal,
        "carbMeal": meal.meal_carb,
        "protMeal": meal.meal_prot,
        "fatMeal": meal.meal_fat,
    }

    socketio.emit("User Details", data)

    socketio.emit("not editing", "User is no longer editing")
    emit_all_user_weights(user_email, user_id)
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)


@socketio.on("workout entry")
def on_workou_entry(data):
    workout_entry = {
        "level": data["level"],
        "split": data["split"],
        "email": data["email"],
        "name": data["name"],
    }
    print("\nNew Workout Entry Received!")
    db.session.add(
        models.Workout(
            workout_entry["level"],
            workout_entry["split"],
            workout_entry["email"],
        )
    )
    db.session.commit()

    plan = workout.Workout(workout_entry["level"], workout_entry["split"]).plan
    clean_plan = []

    for day in plan["days"]:
        clean_plan.append(
            {
                "title": day,
                "workout": plan["days"][day],
            }
        )
    socketio.emit(
        "set plan",
        {
            "sid": request.sid,
            "clean_plan": clean_plan,
            "name": workout_entry["name"],
            "email": workout_entry["email"],
        },
    )
    displaying_quotes()


@socketio.on("new text input")
def on_new_message(data):
    new_str = data["entry"]

    date = datetime.datetime.now()
    time = str(
        datetime.datetime.now(pytz.timezone("US/Eastern")).strftime("%H:%M")
    )  # NYC time
    time_str = months[date.month - 1] + " " + str(date.day) + " \n@" + time

    user_id = data["email"]
    db.session.add(models.Chat(data["entry"], time_str, user_id))
    db.session.commit()
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    displaying_quotes()


@socketio.on("new food search")
def on_new_food_search(data):
    current_user = db.session.query(models.Users).filter_by(id=data["user"]).scalar()
    calorie = db.session.query(models.Macros).filter_by(email=current_user.id).scalar()
    food_name = {"food": data["food_search"]}
    food_response = foodsearch(food_name["food"], calorie.max_carb)
    socketio.emit("food response", food_response)
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    displaying_quotes()


@socketio.on("new user input")
def on_new_user(data):
    date = str(datetime.datetime.now().date())
    measurements = {
        "height": data["height"],
        "weight": data["weight"],
        "birthday": data["birthday"],
        "gender": data["gender"],
        "activityLevel": int(data["activityLevel"][0]),
        "goal_weight": data["goal_weight"],
    }
    birthday = datetime.datetime.strptime(measurements["birthday"], "%Y-%m-%d")
    age = calculate_age(birthday)
    print("\nAge: " + str(age))
    google_usr = {
        "name": data["name"],
        "email": data["email"],
        "sid": request.sid,
        "imgUrl": data["imgUrl"],
    }
    bmr = bmr_cal(
        measurements["weight"],
        measurements["height"],
        age,
        measurements["gender"],
    )
    calories = daily_caloric_need(bmr, measurements["activityLevel"])
    macros = calculate_macro(calories)
    meals = mealplan(calories)
    profile_data = {
        "weight": data["weight"],
        "activityLevel": data["activityLevel"],
        "MaxCalories": macros["MaxCalories"],
    }
    # To fetch the recipes from API getting the variable ready
    db.session.add(
        models.Users(
            google_usr["email"],
            google_usr["name"],
            measurements["height"],
            birthday,
            measurements["gender"],
            measurements["activityLevel"],
            date,
            google_usr["imgUrl"],
            measurements["goal_weight"],
        )
    )
    db.session.commit()

    db.session.add(
        models.Macros(
            bmr,
            macros["MaxCalories"],
            macros["MinCalories"],
            macros["MaxProtein"],
            macros["MinProtein"],
            macros["MaxCarbs"],
            macros["MinCarbs"],
            macros["MaxFat"],
            macros["MinFat"],
            google_usr["email"],
        )
    )
    db.session.commit()

    db.session.add(
        models.Meals(
            meals["breakfast"],
            meals["lunch"],
            meals["dinner"],
            meals["nutrients"]["calories"],
            meals["nutrients"]["carbohydrates"],
            meals["nutrients"]["protein"],
            meals["nutrients"]["fat"],
            google_usr["email"],
        )
    )
    db.session.commit()

    db.session.add(
        models.Weight(
            datetime.datetime.now(), measurements["weight"], google_usr["email"]
        )
    )
    db.session.commit()

    print(
        "Created db Entry for "
        + google_usr["name"]
        + " with email "
        + google_usr["email"]
    )
    socketio.emit("success login", google_usr)
    socketio.emit("is not logging in", "")
    online_users.append(google_usr)
    get_user_details(google_usr["email"])
    emit_all_user_weights(google_usr["email"], google_usr["sid"])
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    displaying_quotes()


@socketio.on("google sign in")
def on_google_sign_in(data):
    print("User is attempting to sign in...")
    google_usr = {
        "name": data["name"],
        "email": data["email"],
        "sid": request.sid,
        "imgUrl": data["imgUrl"],
    }
    login_success = True
    for user in online_users:
        if user["email"] == google_usr["email"]:
            login_success = False
            logged_usr = user
            print(
                "\nLogin Failed!\nUser with email '"
                + google_usr["email"]
                + "' is already logged in!"
            )
            res1 = (
                "Email: '"
                + google_usr["email"]
                + "' is already logged in!"
                + "If this isn't you, please change your password immediately"
            )
            res2 = "Someone just tried to login as you! If you weren't aware of this, please change your password."
            socketio.emit("failed login", {"res": res1}, room=request.sid)
            break
    if login_success:
        if (
            db.session.query(models.Users.id).filter_by(id=google_usr["email"]).scalar()
            is None
        ):
            print("New User: " + google_usr["name"])
            socketio.emit(
                "is logging in",
                {"res": "User is attempting to login", "sid": request.sid},
            )
            socketio.emit("new form", google_usr)
        else:
            print("Welcome Back! " + google_usr["name"])
            online_users.append(google_usr)
            socketio.emit("success login", google_usr)
            get_user_details(google_usr["email"])
            emit_all_user_weights(google_usr["email"], google_usr["sid"])
            displaying_quotes()
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)


@socketio.on("google sign out")
def on_google_sign_out(data):
    for user in online_users:
        if user["sid"] == request.sid:
            online_users.remove(user)
            break
    print("\nUser with SID '" + request.sid + "' has successfully signed out")
    socketio.emit("success logout", {"sid": request.sid})


@socketio.on("connect")
def on_connect():
    print("\nConnected")
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)


@socketio.on("disconnect")
def on_disconnect():
    for user in online_users:
        if user["sid"] == request.sid:
            online_users.remove(user)
            break
    print("\nDisconnected")
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)


@app.route("/")
def home():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template("home.html")


@app.route("/profile")
def profile():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template("profile.html")


@app.route("/workout")
def workout_log():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template("workout.html")


@app.route("/about")
def about():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template("about.html")


@app.route("/foodsearch")
def food_search():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template("foodSearch.html")


if __name__ == "__main__":
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True,
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
