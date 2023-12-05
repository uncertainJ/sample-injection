import sqlite3
CONFIG = {
    "default_table": "users",
    "default_column": "username"
}
def get_data_by_config_value(value):
    # Use parameterized queries to prevent SQL injection
    query = f"SELECT * FROM {CONFIG['default_table']} WHERE {CONFIG['default_column']} = ?"
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query, (value,))
    result = cursor.fetchall()
    connection.close()
    return result
# Test
print(get_data_by_config_value("admin"))