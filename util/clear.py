class Form:
	def clear(self, *args):
		for i in range(len(args)):
			args[i].delete(0, 'end')
			