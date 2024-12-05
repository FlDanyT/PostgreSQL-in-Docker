import psycopg2
from config import host, user, password, db_name, port
import time
import psycopg2.extras


time.sleep(5)


try:
  
  
  connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=port
  )
  
  
  connection.autocommit = True # Автоматическое сохранение изменений
  
  
  # Смотрим версию
  with connection.cursor() as cursor:
    cursor.execute(
      "SELECT version();"
    )
    print(cursor.fetchone())
    
  # Создание таблицы
  with connection.cursor() as cursor:
    cursor.execute(
      """CREATE TABLE users(
        id serial PRIMARY KEY,
        first_name varchar(50) NOT NULL,
        nick_name varchar(50) NOT NULL);"""
    )


  time.sleep(5)
  arr =  [['14141'], ['name1'],
   ['14142'], ['name2'],
   ['14143'], ['name3'],
   ['14144'], ['name4'],
   ['14145'], ['name5'],
   ]
  
  
  # Переформатируем данные в список кортежей
  data_tuples = list(zip(arr[::2], arr[1::2]))
  data_tuples = [(int(item[0][0]), item[1][0]) for item in data_tuples]


  # Добавление данных в базу
  with connection.cursor() as cursor:
      psycopg2.extras.execute_values(cursor, """
        INSERT INTO users (first_name, nick_name) VALUES %s
    """, data_tuples)
      connection.commit()
  
  
  # Добавление данных в базу
  with connection.cursor() as cursor:
      cursor.execute(
      """INSERT INTO users (first_name, nick_name) VALUES
      ('Oleg', 'barracuda');""",
    )

  
  # Получаем данные из базы
  with connection.cursor() as cursor:
        cursor.execute(
        """SELECT nick_name FROM users WHERE first_name = '14145';""",
      )
        print(cursor.fetchone())


  # Удаление таблицы
  with connection.cursor() as cursor:
        cursor.execute(
        """DROP TABLE users;""",
      )
        
        
except Exception as _ex:
  print("[INFO] Error while working with PostgreSQL", _ex)
else:
  if connection: # Завершение работы базы данных
    connection.close()
    print("Завершение работы базы данных")