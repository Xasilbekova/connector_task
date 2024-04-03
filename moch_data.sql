DROP DATABASE chat_db;
CREATE DATABASE chat_db;

CREATE TABLE IF NOT EXISTS user (  
    id SERIAL,  
    full_name VARCHAR(32) NOT NULL,  
    user_name VARCHAR(32) NOT NULL UNIQUE,  
    password VARCHAR(32) NOT NULL,  
    phone_number VARCHAR(13) NOT NULL
);

INSERT INTO user (full_name, user_name, password, phone_number) VALUES (
    'Aziz Shakirov', 'azizDoctor', 'qwerty', '+998977032636'
);