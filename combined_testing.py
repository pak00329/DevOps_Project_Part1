import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define user data
new_user_data = {'userID': 28, 'userName': 'Lebron James'}

# Function to post user data to the REST API
def post_user_data():
    url = 'http://127.0.0.1:5000/user/28'  # Replace with your API URL
    response = requests.post(url, json=new_user_data)
    if response.status_code != 201:  # Assuming 201 Created is the expected status for POST
        raise Exception("test failed: Unable to create user")
    return response.json()

# Function to get user data from the REST API
def get_user_data(user_id):
    url = f'http://127.0.0.1:5000/user/28'  
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("test failed: GET request did not return 200")
    return response.json()

# Function to check if data is stored in the database
def check_db(user_id):
    schema_name = "mydb"
    host = "127.0.0.1"
    port = 3306
    user = "user"
    password = "password"

    # Establish the database connection
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=schema_name)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE userID = %s", (user_id,))  # Use userID for the query
    user_data = cursor.fetchone()
    conn.close()

    if user_data is None:
        raise Exception("test failed: User data not found in the database")
    return user_data

# Function to perform Selenium Webdriver tests
def selenium_test(user_id):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(f'http://127.0.0.1:5000/user/28')  
        user_name_element = driver.find_element(By.CSS_SELECTOR, ".username")  # element locator for the username

        if user_name_element.text != new_user_data['userName']:  # Change to userName
            raise Exception("test failed: User name does not match")
    finally:
        driver.quit()

# Main execution
if __name__ == '__main__':
    # Step 1: Post user data
    posted_data = post_user_data()
    user_id = posted_data.get('userID')  # Assuming the posted data returns the userID

    # Step 2: Verify posted data
    retrieved_data = get_user_data(user_id)
    if retrieved_data != posted_data:
        raise Exception("test failed: Retrieved data does not match posted data")

    # Step 3: Check if data is stored in the database
    check_db(new_user_data['userID'])  # Change to userID

    # Step 4: Selenium test for the web interface
    selenium_test(user_id)

    print("All tests passed successfully!")
