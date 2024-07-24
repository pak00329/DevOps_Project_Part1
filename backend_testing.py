import requests
import pymysql

# Defining user details to be created
new_user_data = {
    'user_id': 27,
    'user_name': 'Wyclif'
}


# Function to post user data to the REST API
def post_user_data():
    url = 'http://127.0.0.1:5000/user'  # Ensure this is the correct endpoint for posting
    json_data = {
        "user_id": new_user_data[27],  # Include id in the data being sent
        "user_name": new_user_data['Wyclif']
    }
    response = requests.post(url, json=json_data)  # Use POST method for creating user

    if response.status_code != 201:  # Expected status code for created user
        raise Exception(
            f"test failed: Unable to create user, status code: {response.status_code}, response: {response.text}")

    return response.json()  # Return the response payload for further verification


# Function to get user data from the REST API
def get_user_data(user_id):
    url = f'http://127.0.0.1:5000/user/{user_id}'  # Use user_id here
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"test failed: GET request did not return 200, status code: {response.status_code}, response: {response.text}")

    return response.json()


# Function to check if the user data is stored in the database
def check_db(user_id):
    # database credentials and settings
    conn = pymysql.connect(
        host='127.0.0.1',  # Database host
        user='user',  # Database user
        password='password',  # Database password
        database='mysql',  # Change to your actual database name
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
if __name__ == '__main__':
    # Step 1: Post new user data
    posted_data = post_user_data()  # This creates a new user and returns the posted data
    user_id = posted_data.get('user_id')  # Assuming the posted response contains the user ID

    # Verify if user_id exists in the posted_data
    if user_id is None:
        raise Exception("test failed: User ID not found in posted data")

    # Step 2: Verify by getting the user data
    retrieved_data = get_user_data(user_id)

    # Check if the retrieved data matches the posted data
    if retrieved_data != posted_data:
        raise Exception("test failed: Data retrieved does not match posted data")

    # Step 3: Check if the posted data is stored in the database
    check_db(new_user_data['user_id'])  # Check by user_id

    print("All tests passed successfully!")
