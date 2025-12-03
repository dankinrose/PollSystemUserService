DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    age INT NOT NULL,
    address VARCHAR(255),
    join_date DATE NOT NULL,
    is_registered TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
