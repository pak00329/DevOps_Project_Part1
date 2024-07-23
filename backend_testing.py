import requests
import pymysql

# Defining user details to be created
new_user_data = {
    'user_id': 27,
    'user_name': 'Wyclif'
}

# Function to post user data to the REST API
def post_user_data():
    url = 'http://api.example.com/users'  
    response = requests.post(url, json=new_user_data)
    
    if response.status_code != 201:  # Expected status code for created user 201 
        raise Exception("test failed: Unable to create user")
    
    return response.json()  # Return the response payload for further verification

# Function to get user data from the REST API
def get_user_data(user_id):
    url = f'http://api.example.com/users/{user_id}'  
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("test failed: GET request did not return 200")
    
    return response.json()

# Function to check if the user data is stored in the database
def check_db(user_id):  # Change to use user_id
    # Replace these database credentials and settings as needed
    conn = pymysql.connect(
        host='127.0.0.1',      # Database host
        user='your_database_user',           # Database user
        password='your_database_password',   # Database password
        database='your_database_name',       # Database name
        port=3306            # Database port
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data is None:
        raise Exception("test failed: User data not found in the database")
    
    return user_data

# Main execution
if __name__ == '__main__':
    # Step 1: Post new user data
    posted_data = post_user_data()  # This creates a new user and returns the posted data
    user_id = posted_data.get('id')  # Assuming the posted response contains the user ID

    # Step 2: Verify by getting the user data
    retrieved_data = get_user_data(user_id)

    # Check if the retrieved data matches the posted data
    if retrieved_data != posted_data:
        raise Exception("test failed: Data retrieved does not match posted data")

    # Step 3: Check if the posted data is stored in the database
    check_db(new_user_data['user_id'])  # Check by user_id

    print("All tests passed successfully!")
