CREATE DATABASE agendai ;

USE agendai ;

CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(60) NOT NULL UNIQUE,
    password VARCHAR(250) NOT NULL,
    active BIT DEFAULT(1),
    CONSTRAINT pk_users_id PRIMARY KEY (id)     
);

CREATE TABLE contacts(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    apelido VARCHAR(30) NOT NULL,
    email VARCHAR(250) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    active BIT DEFAULT(1)
    CONSTRAINT pk_contacts_id PRIMARY KEY (id)     
);