
import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="vitalijaltunin",
                                  # пароль, который указали при установке PostgreSQL
                                  password="0",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="vitalijaltunin")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE skills
                          (ID INT PRIMARY KEY     NOT NULL,
                          vacancy           TEXT    NOT NULL,
                          skill           TEXT    NOT NULL); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")