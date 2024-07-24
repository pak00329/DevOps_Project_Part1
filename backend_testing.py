import requests
import pymysql

# Defining user details to be created
new_user_data = {
    'user_id': 27,
    'user_name': 'Wyclif'
}


# Function to post user data to the REST API
def post_user_data():
    url = 'http://127.0.0.1:5000/user'  # Change this to the correct endpoint for posting
    json_data = {
        "user_id": new_user_data['user_id'],  # Include id in the data being sent
        "user_name": new_user_data['user_name']
    }
    response = requests.post(url, json=json_data)  # Use POST method for creating user

    if response.status_code != 201:  # Expected status code for created user 201
        raise Exception("test failed: Unable to create user")

    return response.json()  # Return the response payload for further verification


# Function to get user data from the REST API
def get_user_data(user_id):
    url = f'http://127.0.0.1:5000/user/27'  # Use user_id here
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("test failed: GET request did not return 200")

    return response.json()


# Function to check if the user data is stored in the database
def check_db(user_id):
    # database credentials and settings
    conn = pymysql.connect(
        host='127.0.0.1',  # Database host
        user='user',  # Database user
        password='password',  # Database password
        database='mysql',  # Database name
        port=3306  # Database port
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))  # Use correct field for your query
    user_data = cursor.fetchone()
    conn.close()

    if user_data is None:
        raise Exception("test failed: User data not found in the database")

    return user_data


# Main execution
if __name__ == '__main__':  # Correct indentation
    # Step 1: Post new user data
    posted_data = post_user_data()  # This creates a new user and returns the posted data
    user_id = posted_data.get('user_id')  # Assuming the posted response contains the user ID

    # Step 2: Verify by getting the user data
    retrieved_data = get_user_data(user_id)

    # Check if the retrieved data matches the posted data
    if retrieved_data != posted_data:
        raise Exception("test failed: Data retrieved does not match posted data")

    # Step 3: Check if the posted data is stored in the database
    check_db(new_user_data['user_id'])  # Check by user_id

    print("All tests passed successfully!")
