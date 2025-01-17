from constants.enums import *
from objects.user import User
from objects.post import Post
from datetime import datetime, timedelta
import mysql.connector
import json

def create_connection():
    with open("database/configsettings.json", 'r') as config_file:
        config_settings= json.loads(config_file.read())
    cnx = mysql.connector.connect(user=config_settings['user'], password=config_settings['password'], 
    host=config_settings['host'], database=config_settings['database'], port=config_settings['port'])

    return cnx

def create_user(user):
    userCnx = create_connection()
    
    cursor = userCnx.cursor()
    
    create_user = "INSERT INTO users (name, phone_number, rating, county, profession) \
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
        newUser = User(name, phone_number, rating, county, profession)
    
    return newUser

def get_user_by_id(id):
    getUserCnx = create_connection()
    cursor = getUserCnx.cursor()

    get_user = "SELECT * FROM users WHERE user_id = " + str(id) + ";"

    cursor.execute(get_user)

    for (user_id, name, phone_number, rating, county, profession) in cursor:
        newUser = User(name, phone_number, rating, county, profession)

    return newUser

def create_post(post):
    postCnx = create_connection()
    cursor = postCnx.cursor()
    
    print(post.type, post.subType)
    create_post = "INSERT INTO posts (user_id, quantity, title, type, sub_type, location, price) \
    VALUES (" + str(post.user_id) + "," + str(post.quantity) + ",\'" + \
        post.title + "\',"  + str(post.type.value) + "," + str(post.subType.value) + ",\'" + str(post.location) + "\'," + str(post.price) + ");"

    cursor.execute(create_post)
    
    postCnx.commit()
    postCnx.close()
   
    return  "Post " + str(post) + " created successfully."

def delete_post(postId):
    postCnx = create_connection()
    cursor = postCnx.cursor()

    delete_post = "DELETE FROM posts WHERE post_id = " + str(postId) + ";"

    cursor.execute(delete_post)

    postCnx.commit()
    postCnx.close()

    return "Post deleted successfully"

def create_request(request):
    requestCnx = create_connection()
    cursor = requestCnx.cursor()
    
    create_request = "INSERT INTO requests (user_id, request_id, quantity, type, location, price) \
    VALUES (\'" + str(request.user_id) + "\',\'" + str(request.request_id) + "\',\'" + str(request.quantity) + "\'," + \
        request.type + "," + str(request.location) + "," + str(request.price) + ");"
    
    cursor.execute(create_request)
    
    requestCnx.commit()
    requestCnx.close()

    return  "Request " + str(request) + " created successfully."

def create_transaction(transaction):
    transactionCnx = create_connection()
    cursor = transactionCnx.cursor()
    
    create_transaction = "INSERT INTO transactions (post_id, request_id, review) \
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
    for (post_id, user_id, quantity, title, type, sub_type, location, price) in cursor:
        newPost = Post(post_id, user_id, title, type, sub_type, quantity, location, price)
        posts.append(newPost)
    
    getpostCnx.close()
    
    return posts

def get_posts_by_title(title):
    getpostCnx = create_connection()
    cursor = getpostCnx.cursor()
    
    get_posts = "SELECT * FROM posts WHERE title = " + "\'" + title + "\';"
    
    print(get_posts)

    cursor.execute(get_posts)
 
    posts = []
    for (post_id, user_id, quantity, title, type, subType, location, price) in cursor:
        newPost = Post(post_id, user_id, title, type, subType, quantity, location, price)
        posts.append(newPost)
    
    getpostCnx.close()
    
    return posts

def get_posts_by_subtype(type, subtype):
    getpostCnx = create_connection()
    cursor = getpostCnx.cursor()
    
    get_posts = "SELECT * FROM posts WHERE type = " + str(type.value) + " AND sub_type = " + str(subtype.value) + ";"
    
    print(get_posts)

    cursor.execute(get_posts)
 
    posts = []
    for (post_id, user_id, quantity, title, type, subType, location, price) in cursor:
        newPost = Post(post_id, user_id, title, type, subType, quantity, location, price)
        posts.append(newPost)
    
    getpostCnx.close()
    
    return posts

def update_post_quantity(postId, amount):
    cnx = create_connection()
    cursor = cnx.cursor()

    update_post_amount = "UPDATE posts SET quantity = " + str(amount) + " WHERE post_id = " + str(postId) + ";"

    cursor.execute(update_post_amount)

    cnx.commit()
    cnx.close()

    return "post updated successfully"

