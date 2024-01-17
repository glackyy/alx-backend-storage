-- A Script that creates a table users
-- with the follow fields: id, email, name
-- Country requirements(enumeration of US, CO and TN)
CREATE TABLE IF NOT EXISTS users(
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(250) NOT NULL UNIQUE,
        name varchar(250),
        country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
)