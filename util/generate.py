from abc import ABC, abstractstaticmethod

class IGenerator(ABC):
	@abstractstaticmethod
	def generate(self):
		pass

class OTP(IGenerator):
	def generate(self)->str:
		string:str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		otp:str = ""
		length:int = len(string)
		for i in range(5):
			otp += string[math.floor(random.random() * length)]
		return otp

