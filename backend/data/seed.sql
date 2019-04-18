CREATE TABLE IF NOT EXISTS User
  ( userID int, firstName varchar(255), lastName varchar(255), email varchar(255), userPassword varchar(255), location varchar(255), description TEXT, lastActive DATE);

CREATE TABLE IF NOT EXISTS Family
  ( familyID int, familyName varchar(255), familySize int)

CREATE TABLE IF NOT EXISTS FamilyTable 
  ( userID int, firstName varchar(255), lastName varchar(255), familyID int, description TEXT)

CREATE TABLE IF NOT EXISTS Ticket
  ( ticketID int, userID int, firstName varchar(255), lastName varchar(255), familyID int, description TEXT)

CREATE TABLE IF NOT EXISTS ChatSesssion 
  ( sessionID int )

CREATE TABLE IF NOT EXISTS ChatMessage
  (sessionID int, userID int, firstName varchar(255), lastName varchar(255), message TEXT, messageTime TimeStamp); 
