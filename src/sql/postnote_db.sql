-- Create the Postnote database and select it for use. --
CREATE DATABASE Postnote;
USE Postnote;

-- Create the user table so users can login and create notes. --
CREATE TABLE User
(
  UserID int AUTO_INCREMENT NOT NULL,
  Username VARCHAR(50) NOT NULL,
  Email VARCHAR(256) NOT NULL,
  Password VARCHAR(256) NOT NULL,
  UserType int NOT NULL,
  PRIMARY KEY (UserID)
);

-- Create the Note table that will store a users notes. --
CREATE TABLE Note
(
  NoteID int AUTO_INCREMENT NOT NULL,
  Title VARCHAR(256) NOT NULL,
  Message LONGTEXT NOT NULL,
  Username VARCHAR(50) NOT NULL,
  NoteType INT NOT NULL,
  LastUpdate DATE NOT NULL,
  PRIMARY KEY (NoteID)
);