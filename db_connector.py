import pymysql
import os

# Function to connect to the database with error handling
def dataBaseConnector():
    schema_name = "mydb"
    host = "127.0.0.1"
    port = 3306
    user = os.getenv("DB_USER", "default_user")  # Using environment variables or a secure way to configure
    password = os.getenv("DB_PASSWORD", "default_password")

    try:
        conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=schema_name)
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None

def createRecords(userID, userName):
    connection = dataBaseConnector()
    if connection is None:
        return {"Success": False, "Message": "Database connection failed"}

    cursor = connection.cursor()
    query = "INSERT INTO users (id, name) VALUES (%s, %s)"

    try:
        cursor.execute(query, (userID, userName))
        connection.commit()
    except pymysql.MySQLError as e:
        return {"Success": False, "Message": str(e)}
    finally:
        cursor.close()
        connection.close()

    return {"Success": True}

def readRecord(userID):
    connection = dataBaseConnector()
    if connection is None:
        return {"Success": False, "Message": "Database connection failed"}

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (userID,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return {"Success": True, "user_id": result[0], "userName": result[1]}
    else:
        return {"Success": False, "Message": "ID Does not exist"}

def updateRecords(userID, userName):
    connection = dataBaseConnector()
    if connection is None:
        return {"Success": False, "Message": "Database connection failed"}

    cursor = connection.cursor()
    query = "UPDATE users SET name = %s WHERE id = %s"
    cursor.execute(query, (userName, userID))
    connection.commit()

    success = cursor.rowcount > 0  # This will check if any rows were affected
    cursor.close()
    connection.close()

    if success:
         return {"Success": True, "user_id": userID, "userName": userName}
    else:
         return {"Success": False, "Message": "ID Does not exist"}

def deleteRecords(userID):
    connection = dataBaseConnector()
    if connection is None:
        return {"Success": False, "Message": "Database connection failed"}

    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (userID,))
    connection.commit()

    success = cursor.rowcount > 0  # This will check if any rows were affected
    cursor.close()
    connection.close()

    if success:
        return {"Success": True, "user_id": userID, "userName": "User Deleted"}
    else:
        return {"Success": False, "Message": "ID Does not exist"}

# Example test calls (uncomment for testing)
# print(readRecord(userID=2))
# print(createRecords(13, "Kwame"))
# print(updateRecords(userID=13, userName="Kwame_Bruce"))
# print(deleteRecords(userID=1))
# print(readRecord(3))
