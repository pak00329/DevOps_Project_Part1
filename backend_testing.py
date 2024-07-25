import requests
import pymysql

# Defining user details to be created
new_user_data = {
    'user_id': 27,
    'user_name': 'Wyclif'
}


# Function to post user data to the REST API
def post_user_data():
    new_user_id = new_user_data['user_id']
    print('userid:', new_user_id)
    url = f"http://127.0.0.1:5000/users/{new_user_id}"
    json_data = {
        "user_id": new_user_data['user_id'],
        "user_name": new_user_data['user_name']
    }
    response = requests.post(url, json=json_data)

    print(f"Response from POST: {response.text}")
    print(f"Status from POST: {response.status_code}")

    if response.status_code != 201:
        raise Exception(
            f"test failed: Unable to create user, status code: {response.status_code}, response: {response.text}")

    return response.json()


def get_user_data(user_id):
    url = f'http://127.0.0.1:5000/users/{user_id}'
    response = requests.get(url)

    print(f"Response from GET: {response.text}")
    print(f"Status Code from GET: {response.status_code}")

    if response.status_code != 200:
        raise Exception(
            f"test failed: GET request did not return 200, status code: {response.status_code}, response: {response.text}")

    return response.json()


def check_db(user_id):
    # database credentials and settings
    conn = pymysql.connect(
        host='127.0.0.1',
        user='user',
        password='password',
        database='mysql',
        port=3306
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data is None:
        raise Exception("test failed: User data not found in the database")

    return user_data


if __name__ == '__main__':
    # Step 1: Post new user data
    posted_data = post_user_data()
    user_id = posted_data.get('user_added').get('user_id')

    print(posted_data)
    if user_id is None:
        raise Exception("test failed: User ID not found in posted data")

    # Step 2: Verify by getting the user data
    retrieved_data = get_user_data(user_id)

    if retrieved_data != posted_data:
        raise Exception("test failed: Data retrieved does not match posted data")

    # Step 3: Check if the posted data is stored in the database
    check_db(new_user_data['user_id'])  # Check by user_id

    print("All tests passed successfully!")
