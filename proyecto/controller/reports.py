import pandas as pd
from config.app import App

def generar_reporte(app: App):
    """
    Genera un reporte sencillo de la tabla Libro.
    Exporta a CSV y envía por correo.
    """
    conn = app.bd.get_connection()

    query = """
    SELECT titulo, isbn, precio, autor_nombre, editorial_nombre
    FROM Libro
    ORDER BY precio DESC
    """
    df = pd.read_sql_query(query, conn)

    # Guardar a CSV
    path_csv = "./files/reporte_libros.csv"
    df.to_csv(path_csv, index=False, encoding="utf-8")

    # Enviar por correo
    destinatario = "test@example.com"
    asunto = "Reporte de Libros"
    cuerpo = "Hola, adjunto el reporte de libros."
    app.mail.send_email(destinatario, asunto, cuerpo, path_csv)

    print("✅ Reporte generado y enviado.")