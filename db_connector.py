#On this file, we will set up four functions the DB connector will deal with this. Create, Read, Update, Delete
# Establishing a connection to DB
import pymysql

# Function for always connecting to the database
def dataBaseConnector():
    schema_name = "mydb"

    host = "127.0.0.1"
    port = 3306
    user = "user"
    password = "password"

    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=schema_name)
    return conn


def createRecords(userID, userName):
    connection = dataBaseConnector()
    cursor = connection.cursor()

    #  using the prepared statement (%s for the values), then create data/values in a table
    query = f"INSERT into mydb.users (id, name) VALUES (%s, %s)"
    cursor.execute(query, (userID, userName))

    # Save into the Database
    connection.commit()
    cursor.close()
    connection.close()
    return "Success"


# Read Records from The Database
def readRecord(userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {userID};")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        message = {"Success": True, "user_id": result[0], "userName": result[1]}
    else:
        message = {"Success": False, "Message": "ID Does not exist"}

    return message


# Update Records In A Database
def updateRecords(userID, userName):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"UPDATE users SET name = %s WHERE id = %s"
    result = cursor.execute(query, (userName, userID))
    connection.commit()
    cursor.close()
    connection.close()
    if result:
         message = {"Success": True, "user_id": userID, "userName": userName}
    else:
         message = {"Success": False, "Message": "ID Does not exist"}
    return message


# Delete Records In A Table
def deleteRecords (userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"DELETE FROM users WHERE id = %s"
    result = cursor.execute(query, (userID))
    connection.commit()
    cursor.close()
    connection.close()
    if result:
         message = {"Success": True, "user_id": userID, "userName": "User Deleted"}
    else:
         message = {"Success": False, "Message": "ID Does not exist"}
    return message


#print(readRecord(userID=2))
# print(createRecords(13, "Kwame"))
print(updateRecords(userID=13, userName="Kwame_Bruce"))


# print(deleteRecords(userID = 1))

# print(readRecord(3))

