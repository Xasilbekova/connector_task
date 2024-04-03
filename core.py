import mysql.connector

class Core:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = 'root',
                database = 'chat_db'
            )
        except Exception as err:
            print(err)
        

    def insert_user(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    INSERT INTO user (full_name, user_name, password, phone_number) VALUES (
                        '{user["fullname"]}', 
                        '{user['username']}', 
                        '{user['password']}', 
                        '{user['phone_number']}'
                    );
                """
                cursor.execute(sql)
                self.connection.commit()
        except Exception as err:
            print(err)
        else:
            print("User saqlandi.")

    def get_all_users(self):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    SELECT *FROM user;
                """
                cursor.execute(sql)
                data = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return data
        
    def update_user(self, user):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    UPDATE user 
                    SET 
                        full_name = '{user['fullname']}', 
                        user_name = '{user['username']}',
                        password = '{user['password']}',
                        phone_number = '{user['phone_number']}'
                    WHERE id = '{user['id']}';
                """
                cursor.execute(sql)
        except Exception as err:
            return err
        else:
            self.connection.commit()
            return 'OK'
        
    def delete_user(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM user WHERE id = '{user_id}'"
                cursor.execute(sql)
        except Exception as err:
            return err
        else:
            self.connection.commit()
            return 'OK'