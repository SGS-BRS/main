import mysql.connector
from mysql.connector import Error

# Chave fictícia (vulnerabilidade)
rsa_private_key = """-----BEGIN RSA PRIVATE KEY-----MIICWwIBAAKBgFnnJoFQBlRK389MZHphjXGiFb2PUcn8V6oaOEtm9LmaNoPoRrLDYgaqQHj9HnkSQHaSPF7HWv79lRiEFg/0j1hJj7eKcD0RDwV5PBjwCgaL2yF5/bxQH4StAVOmMarXO5C0PnyJZ6oNW6en6XTKLhFFA7rBOX9DoNvG/puR8MWNAgMBAAECgYAWTc10uWjIksbRxA8NeZRAw8iG/b550PvivJyIwGMohMTPltmrUePI6YYTPiDIQqnxgLgvf1/o8PqDWYmrra2+Gk1ls3jYdR97NIm7kb1d9bh4+0f4RmPdKyOu/tZ7uaOeIN6sOIQH0kINYSjpBUzV31aGP2Ql7S8dzrMfnZdCwQJBALH33uzcBlYSC1t/6Rp9mar6b6Uu3maTf9TVK+MvttnROx74vB9PMLD4r51AT91QsHHSELmcuNyfSCmAAFMlwPECQQCBUljclRS0qNyD1912x5WgHHfEYvz8zRGpMPyovLqItQRgt+cAtaL4gGLynQSEupAi58NZZu/64jpsBkLvdI5dAkBHFw+aqA1z5kNZKpAv/8oZjW55mm5GpVbj6r9cQhwViEnIhm2HSDfYCY8FDsKYUnoZDWOW8W662nmV8kau8B7RAkAs93k2mg/tEZo7rd+v4Y5BciSjANh+/r9ZWVNBSP6Dco3nI4sLUB0u01WUjsx3aneb64Kdn5FqZydxUGwN3zVxAkEAlNFVWZ/WsOXHYu2QTurW4J9CrgPX+o5RRRLkzThocSUChfSAqyfy32ROSjPuxQmeFpYkpbh+ACWpYhOLVpNS2Q==-----END RSA PRIVATE KEY-----"""

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
