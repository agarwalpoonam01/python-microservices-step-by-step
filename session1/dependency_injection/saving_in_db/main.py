from window import Window
from database import Database

storage = Database()


w = Window(storage)
w.write_text("I am from India")
w.show_window()

w.save_text()


