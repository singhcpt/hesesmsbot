from enums import *
from user import User
from post import Post
from datetime import datetime, timedelta
import mysql.connector
import json

def create_connection():
    with open("configsettings.json", 'r') as config_file:
        config_settings= json.loads(config_file.read())
    cnx = mysql.connector.connect(user=config_settings['user'], password=config_settings['password'], 
    host=config_settings['host'], database=config_settings['database'], port=config_settings['port'])

    return cnx

def create_user(user):
    userCnx = create_connection()
    
    cursor = userCnx.cursor()
    
    create_user = "INSERT INTO Users (name, phone_number, rating, county, profession) \
        VALUES (\'" + user.name + "\'," + str(user.number) + "," + str(user.reliability) + ",\'" + user.county \
            + "\',\'" + user.profession + "\');"

    cursor.execute(create_user)
    
    userCnx.commit()
    userCnx.close()

    return  "User " + str(user) + " created successfully."

def get_user_id(phone_number):

    userCnx = create_connection()
    
    cursor = userCnx.cursor()
    
    get_uid = "SELECT user_id FROM users WHERE phone_number = " + str(phone_number) + ";"
    
    
    cursor.execute(get_uid)

    uid = ""

    for user_id in cursor:
        uid = user_id
    
    userCnx.close()

    return uid[0] if len(uid) > 0 else None

def get_user(number):
    getUserCnx = create_connection()
    cursor = getUserCnx.cursor()

    get_user = "SELECT * FROM users WHERE phone_number = " + str(number) + ";"

    cursor.execute(get_user)

    for (user_id, name, phone_number, rating, county, profession) in cursor:
        newUser = User(name, phone_number, county, profession)
    
    return newUser

def create_post(post):
    postCnx = create_connection()
    cursor = postCnx.cursor()
    
    create_post = "INSERT INTO Posts (user_id, quantity, type, location, price) \
    VALUES (" + str(post.user_id) + "," + str(post.quantity) + ",\'" + \
        post.crop + "\',\'" + str(post.location) + "\'," + str(post.price) + ");"

    cursor.execute(create_post)
    
    postCnx.commit()
    postCnx.close()
   
    return  "Post " + str(post) + " created successfully."

def create_request(request):
    requestCnx = create_connection()
    cursor = requestCnx.cursor()
    
    create_request = "INSERT INTO Requests (user_id, request_id, quantity, type, location, price) \
    VALUES (\'" + str(request.user_id) + "\',\'" + str(request.request_id) + "\',\'" + str(request.quantity) + "\'," + \
        request.type + "," + str(request.location) + "," + str(request.price) + ");"
    
    cursor.execute(create_request)
    
    requestCnx.commit()
    requestCnx.close()

    return  "Request " + str(request) + " created successfully."

def create_transaction(transaction):
    transactionCnx = create_connection()
    cursor = transactionCnx.cursor()
    
    create_transaction = "INSERT INTO Transactions (post_id, request_id, review) \
    VALUES (\'" + str(transaction.post_id) + "\',\'" + str(transaction.request_id) + "\',\'" + str(transaction.review) + ");"
    
    cursor.execute(create_transaction)
    
    transactionCnx.commit()
    transactionCnx.close()

    return  "Transaction " + str(transaction) + " created successfully."

def get_posts(type, max, location):
    getpostCnx = create_connection()
    cursor = getpostCnx.cursor()
    
    get_posts = "SELECT * FROM Posts WHERE type = " + "\'" + type + "\'"
    get_posts += " AND price <= " + str(max)
    get_posts += " AND location = " + "\'" + location + "\';"
    
    print(get_posts)

    cursor.execute(get_posts)
 
    posts = []
    for (post_id, user_id, quantity, type, location, price) in cursor:
        newPost = Post(user_id, type, quantity, location, price)
        posts.append(newPost)
    
    getpostCnx.close()
    
    return posts

