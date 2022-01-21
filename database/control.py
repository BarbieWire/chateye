import psycopg2


class Database:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__password = password
        self.__database = database
        self.user = user

    def connect(self):
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            password=self.__password,
            user=self.user
        )
        connection.autocommit = True
        return connection

    @staticmethod
    def create_table(connection, table):
        with connection.cursor() as curs:
            curs.execute(f'CREATE TABLE {table} (id SERIAL PRIMARY KEY, firstuser VARCHAR, seconduser VARCHAR)')

    @staticmethod
    def create(connection, chat_id, table):
        with connection.cursor() as curs:
            curs.execute(f"INSERT INTO {table} (firstuser) VALUES (%s)", (chat_id,))

    @staticmethod
    def get_queue(connection, table):
        with connection.cursor() as curs:
            curs.execute(F"SELECT * FROM {table}")
            return curs.fetchall()

    @staticmethod
    def insert(connection, table, fuid, suid):
        with connection.cursor() as curs:
            curs.execute(f"INSERT INTO {table} (firstuser, seconduser) VALUES (%s, %s)", (fuid, suid))

    @staticmethod
    def delete_queue(connection, chat_id):
        with connection.cursor() as curs:
            curs.execute(F"DELETE FROM queue WHERE firstuser = '{chat_id}'")

    @staticmethod
    def queue_check(connection, chat_id, table):
        with connection.cursor() as curs:
            curs.execute(F"SELECT * FROM {table} WHERE firstuser = '{chat_id}'")
            data = curs.fetchall()
            if data == []:
                return False
            else:
                return True

    @staticmethod
    def dialogs_check(connection, chat_id):
        with connection.cursor() as curs:
            curs.execute(F"SELECT * FROM dialogs WHERE firstuser = '{chat_id}'")

            data = curs.fetchall()
            if data == []:
                curs.execute(F"SELECT * FROM dialogs WHERE seconduser = '{chat_id}'")
                data = curs.fetchall()
                if data == []:
                    return (False,)
                else:
                    return True, 2, data[0][1]
            else:
                return True, 1, data[0][2]

    @staticmethod
    def seconduser(connection, chat_id):
        with connection.cursor() as curs:
            curs.execute(F"DELETE FROM dialogs WHERE firstuser = '{chat_id}'")

    @staticmethod
    def firstuser(connection, chat_id):
        with connection.cursor() as curs:
            curs.execute(F"DELETE FROM dialogs WHERE seconduser = '{chat_id}'")
