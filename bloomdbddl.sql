CREATE DATABASE bloomdb;

USE bloomdb;

CREATE TABLE users
(
    user_id int not null AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) not null,
    phone_number bigint not null,
    rating float,
    county varchar(255) not null,
    profession varchar(255) not null
);

ALTER TABLE users AUTO_INCREMENT=1000000;

CREATE TABLE posts
(
    post_id int not null AUTO_INCREMENT PRIMARY KEY,
    user_id int not null,
    quantity int not null,
    type varchar(255),
    location varchar(255),
    price int not null,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

ALTER TABLE posts AUTO_INCREMENT=2000000;

CREATE TABLE transactions
(
    transaction_id int not null AUTO_INCREMENT PRIMARY KEY,
    seller_id int not null,
    buyer_id int not null,
    post_id int not null,
    review int not null,
    FOREIGN KEY (seller_id) REFERENCES users(user_id),
    FOREIGN KEY (buyer_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

ALTER TABLE transactions AUTO_INCREMENT=3000000;