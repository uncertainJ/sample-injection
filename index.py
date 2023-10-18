import sqlite3

def get_user_by_id(user_id):
    # This might look suspicious because of string concatenation.
    query = "SELECT * FROM users WHERE id = " + str(user_id)

    # However, the user_id is always an integer and not from user input.
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    return result

# Test
print(get_user_by_id(1))
