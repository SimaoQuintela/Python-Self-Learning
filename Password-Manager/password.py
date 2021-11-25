import os

dictionary = {
}
class passwordManager:

	def __init__(self):
		self.home()

	def clearConsole(self):
		os.system('cls')

	def updateDictionary(self):
		file = open('dictionary.txt', 'r')
		for line in file:
			(key, value) = line.split()
			dictionary[key] = value

		file.close()

	def home(self):
		self.updateDictionary()
		print("1- Verificar password\n2- Adicionar password\n3- Remover password\n4- Sair")
		option = int(input("Escolha a opção que quer: "))
		self.clearConsole()

		if option == 1:
			self.verifyPassword()
		elif option == 2:
			self.add()
		elif option == 3:
			self.remove()

	def verifyPassword(self):
		for key in dictionary:
			print(key)

		app = input("Insira o nome da rede social: ")
		
		if app in dictionary.keys():
			self.clearConsole()
			print("Password: " + dictionary[app] + "\n")
			self.home()
		else:
			self.clearConsole()
			print("Rede social inexistente. Quer tentar de novo?")
			decision = int(input("1- Sim\n2- Não\nEscolha a sua opção: "))
			if decision == 1:
				self.clearConsole()
				self.verifyPassword()
			else: 
				self.clearConsole()
				self.home()

	def add(self):
		for key in dictionary:
			print(key)

		app = input("Insira a app: ")
		password = input("Insira a password: ")

		#acrescentar a nova app ao documento de texto
		file = open('dictionary.txt', 'a')
		new_line = app + " " + password + "\n"
		file.write(new_line)
		file.close()

		#acrescentar a nova app ao dicionário
		dictionary[app] = password
		self.clearConsole()
		print("App acrescentada com sucesso\n")
		self.home()


	def remove(self):
		for key in dictionary:
			print(key)

		app = input("Insira a app: ")
		# apagar a app do dicionário 
		del dictionary[app]

		# ler cada linha do ficheiro que contem o dicionario 
		file = open('dictionary.txt', 'r')
		lines = file.readlines()
		file.close()

		new_file = open('dictionary.txt', 'w')

		for line in lines:
			if line.split()[0] != app:
				new_file.write(line)  

		new_file.close()
		self.clearConsole()
		print("App removida com sucesso\n")
		self.home()




passwordManager()