import pandas as pd
from config.app import App
from modelos.model import Autor, Libro, Editorial

def ingest_data(app: App):
    """
    Lee el archivo Excel (libros.xls) y crea/llena las tablas Autor, Editorial, Libro.
    """
    conn = app.bd.get_connection()

    Autor().create_table(conn)
    Editorial().create_table(conn)
    Libro().create_table(conn)


    path_excel = "files/libros.xlsx"

    df = pd.read_excel(path_excel, sheet_name="LIBROS")  


    df_autores = df['Autor'].drop_duplicates()
    data_autores = [(a,) for a in df_autores if pd.notna(a)]

    df_editoriales = df['Editorial'].drop_duplicates()
    data_editoriales = [(e,) for e in df_editoriales if pd.notna(e)]

    data_libros = []
    for idx, row in df.iterrows():
        if pd.notna(row['Autor']) and pd.notna(row['Editorial']) and pd.notna(row['Titulo']):
            data_libros.append((
                row['Titulo'],
                row['ISBN'],
                float(row['Precio']) if not pd.isna(row['Precio']) else 0.0,
                row['Autor'],
                row['Editorial']
            ))


    app.bd.insert_many("Autor", ["nombre"], data_autores)
    app.bd.insert_many("Editorial", ["nombre"], data_editoriales)
    app.bd.insert_many(
        "Libro",
        ["titulo", "isbn", "precio", "autor_nombre", "editorial_nombre"],
        data_libros
    )

    print("✅ Ingesta de datos completada.")
