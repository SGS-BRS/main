import mysql.connector
from mysql.connector import Error

# Chave de API fictícia (vulnerabilidade)
rsa_private_key = "MIICWgIBAAKBgFHwxHivn5GzkxpaNir63VHXLF3fdvy0rH+zoyALRAX9aaF31YiRUSTsD2tw0WmP5HjzuLbZs5PAvjEElha2np20K0heY23Q8cT6pSHDBrT+zox4AZNP6u4PqsHt47B/uVdgHMu7UVQZWAp8QewVyfI8hxGvaj3I9Bwdle6R49+1AgMBAAECgYAiHeQ/96exy5oJE9yP4qm5xKSFZWCucS+NcCcQVYB6GfwcLb/rv82QWPVGn8+hazcOoTOcdmJNt6e40xcG1/yMZkXlMoNSQT1u2TTy5lNXm1lwHYpdm+qDcdR6HdlTwvHQbzgT/1T0QXWrsqMmjbeF3HSWsQ3JeRPsBfl3IAhooQJBAJlBKICl3GtQRQC23ydq2nNO5A7YbWgvB+r45YPwpgWW99dyLXzlBSnG+xzEk90O1ii/a+9woyOqlvbOoY0NfYkCQQCI4BdJlDS6ZeDFcRGrhwIQUz2BgHs/l83Slhw5u3xeexfIKEtLvuGMzjpF3C7Za8Db0D/IbtCXjtdKK9qE7lHNAkBy5j4mjbO/JVRGn9SY6ezUDK7BTpRgSvqFuYviKtdeU3yHo8vk2pPPaaa1P9CYKNp5fGLBBtLZF7nNWsgWR6n5AkBfvwILQlUwHpwBAXsu1Z4n9VKNCGcusO4VZVQRPoldPhYAuc8SCVCVwp0YyVEsXifmm+JCPuJDYnRPOiX93wfxAkA6WJoIPOW7gt9a71kBL8Z5/AYU7Y8Sg4MwuDIwzPFTcjHPNJQFkVHR0FnLnkXXxQEA2rHRRdgvWf4eRwddArXS"

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
