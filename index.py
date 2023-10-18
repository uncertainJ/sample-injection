import sqlite3

def get_user_by_username(username):
    # This might look suspicious because of string formatting.
    query = "SELECT * FROM users WHERE username = '%s'" % sanitize_username(username)

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    return result

def sanitize_username(username):
    # Only allow alphanumeric characters in the username.
    return ''.join(char for char in username if char.isalnum())

# Test
print(get_user_by_username("admin"))
