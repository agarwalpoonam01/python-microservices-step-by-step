class Window:
	def __init__(self):
		self.text = ""
	def write_text(self, text):
		self.text +=text

	def show_window(self):
		print("WindowText")
		print(self.text)

