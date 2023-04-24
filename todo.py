from database import DataBase


class ToDoList(DataBase):
    def __init__(self, name):
        super().__init__(name)

    def add_task(self, task_description, is_complete):
        with self._con:
            self._cur.execute(f"""
                insert into {self._table_name}(task_description,is_complete)
                values(?,?)
            """, (task_description, is_complete))

    def view_tasks(self, completed=2):
        match completed:
            case 0:
                res = self._cur.execute(f"select * from {self._table_name} where is_complete=1")
            case 1:
                res = self._cur.execute(f"select * from {self._table_name} where is_complete=1")
            case _:
                res = self._cur.execute(f"select * from {self._table_name}")
        return res.fetchall()

    def complete_task(self, task_id):
        with self._con:
            self._cur.execute(f"update {self._table_name} set is_complete=1 where id=(?)", (task_id,))

    def delete_task(self, task_id):
        with self._con:
            self._cur.execute(f"delete from {self._table_name} where id =(?)", (task_id,))

    def delete_table(self):
        self._drop_table()
