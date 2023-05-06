import requests
import random
import string

# Generate a random name and email address
name_response = requests.get('https://names.drycodes.com/1?nameOptions=boy_names')
name = name_response.text.strip()
email = f"{name.lower().replace(' ', '')}{random.randint(100, 999)}@example.com"

# Set the user agent
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; TCL UnionTV Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'

# Set the request headers
headers = {
    'User-Agent': user_agent,
    'Referer': 'https://m.vidio.com/users/register',
    'Origin': 'https://m.vidio.com'
}

# Set the POST data
data = {
    'email': email,
    'password': 'password',
    'password_confirmation': 'password',
    'full_name': name
}

# Send the POST request
response = requests.post('https://m.vidio.com/users/register', headers=headers, data=data)

# Check if the registration was successful
if 'registered' in response.text:
    # Registration was successful, save the email and password to a file
    with open('accounts.txt', 'a') as f:
        f.write(f"{email}|password\n")
    print(f"Registration successful. Email: {email}, Password: password")
else:
    # Registration failed, display an error message
    print("Registration failed.")
