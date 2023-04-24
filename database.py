import sqlite3


class DataBase:
    def __init__(self, name):
        self._con = sqlite3.connect("todo.sql3")
        self._cur = self._con.cursor()
        self._table_name = "todo_" + name
        self._create_table()

    def _create_table(self):
        self._cur.execute(f"""
                            create table if not exists {self._table_name}
                            (
                            id integer primary key autoincrement,
                            task_description text,
                            is_complete boolean default 1
                            );
                        """)
        self._con.commit()

    def _drop_table(self):
        self._cur.execute(f"drop table {self._table_name}")

