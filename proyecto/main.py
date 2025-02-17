from config.app import App
from controller.menu import menu

if __name__ == "__main__":
     app = App("./mi_proyecto.db") 
     menu(app)