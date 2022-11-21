from window import Window
from textfile import Textfile

storage = Textfile()
w = Window(storage)
w.write_text("I am from India")
w.show_window()

w.save_text()

