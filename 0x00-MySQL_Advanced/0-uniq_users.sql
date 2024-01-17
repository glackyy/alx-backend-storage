-- A Script that creates a table users
-- with the following fields: id, email, name

CREATE TABLE IF NOT EXISTS users (
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(250) NOT NULL UNIQUE,
        name varchar(250),
)