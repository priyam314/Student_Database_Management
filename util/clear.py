class Entry:
	def __init__(self, *args):
		pass
	def clear(self):
		for i in range(len(args)):
			args[i].delete(0, 'end')
			