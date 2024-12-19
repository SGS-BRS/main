import mysql.connector
from mysql.connector import Error

# Chave de API fictícia (vulnerabilidade)
API_KEY = "12345-abcde-67890-fghij-12345-huashusa"

# Conexão com o banco de dados usando MySQL Connector (com falhas de segurança)
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='test',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Connected successfully to the database")
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Falha de segurança: SQL Injection
def get_user_data(connection, user_input):
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

# Falha de segurança: Cross-Site Scripting (XSS)
def display_user_data(user_data, comment):
    for row in user_data:
        print(f"id: {row[0]} - Name: {row[1]} - Comment: {comment}")

# Função principal
def main():
    connection = create_connection()
    if connection:
        user_input = input("Enter username: ")
        comment = input("Enter comment: ")
        user_data = get_user_data(connection, user_input)
        if user_data:
            display_user_data(user_data, comment)
        else:
            print("0 results")
        connection.close()

if __name__ == "__main__":
    main()
