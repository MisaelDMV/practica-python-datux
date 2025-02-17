import sqlite3
from rich.progress import Progress

class Database:
    def __init__(self, path_db: str):
        self.path_db = path_db

    def init_connection(self):
        try:
            self.connection = sqlite3.connect(self.path_db)
        except Exception as e:
            print("Error al conectar con la BD:", e)

    def get_connection(self):
        if not hasattr(self, 'connection'):
            self.init_connection()
        return self.connection

    def insert_many(self, table: str, columns: list, data: list):
        if not data:
            print(f"⚠️ No hay datos para insertar en {table}.")
            return

        MAX_BATCH_SIZE = 500
        num_batches = (len(data) // MAX_BATCH_SIZE) + 1

        column_names = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

        with Progress() as progress:
            task = progress.add_task(f"[green]Insertando en {table}...", total=num_batches)

            for i in range(num_batches):
                batch = data[i * MAX_BATCH_SIZE : (i + 1) * MAX_BATCH_SIZE]
                if batch:
                    cursor = self.connection.cursor()
                    cursor.executemany(query, batch)
                    self.connection.commit()

                progress.update(task, advance=1)

        print(f"✅ Se insertaron {len(data)} filas en la tabla '{table}'.")

    def close_connection(self):
        if hasattr(self, 'connection'):
            self.connection.close()
            print("Conexión a la BD cerrada.")