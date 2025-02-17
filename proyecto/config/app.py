
from config.database import Database
from config.mail import Mail

class App:
    def __init__(self, path_db):

        smtp_server = "sandbox.smtp.mailtrap.io"
        port = 2525
        user = "USUARIO_MAILTRAP"
        password = "PASSWORD_MAILTRAP"


        self.bd = Database(path_db)

        self.mail = Mail(smtp_server, port, user, password)