CREATE DATABASE Postnote;
USE Postnote;

CREATE TABLE API_Key (
	KeyID int Auto_Increment Not Null,
    APIKey varchar(256) Not Null,
    Primary Key(KeyID)
);

CREATE TABLE Post (
	PostID int Auto_Increment Not Null,
	Title varchar(500) Not Null,
    Message longtext Not Null,
    Date date Not Null,
    PostedBy varchar(256) Not Null,
    Primary Key(PostID)
)