import os
import time 

class hangman:
    def __init__(self):
        self.home()

    def clearConsole(self):
        os.system('cls')            

    def home(self):
        print("1- Novo jogo")
        print("2- Sair")
        option = int(input("Selecione a opção que deseja: "))

        if option == 1:
            self.clearConsole()
            palavra = input("Introduza uma palavra: ")
            self.clearConsole()
            self.game(palavra)
            time.sleep(3)

    listOfGuesses= []     # lista de guesses que vou dando ao longo do jogo
    tentativas = 0        # número de tentativas falhadas
    # Função responsável pelo início do jogo
    def game(self, palavra):
        for letra in palavra:
            if letra in self.listOfGuesses:
                print(letra, end=" ")
            else:
                if letra != " " and letra != "-":
                    print("_", end=" ")
                elif letra == ' ':
                    print(" ", end=" ")
                else:
                    print("-", end=" ")

        print("\n1- Introduzir palavra")
        print("2- Introduzir letra")

        self.updateMan()

        decision = int(input("Selecione a opção correspondente: "))

        guess = input("Tenta a tua sorte: ")
        if decision == 1:
            self.wordGuess(palavra, guess)
        else:
            self.letterGuess(palavra, guess)

    # Função que verifica se adivinhei a palavra
    def wordGuess(self, palavra, guess):
        if palavra == guess:
            self.clearConsole()
            print(f"Parabéns, acertaste! A palavra era {palavra}")
        else:
            self.tentativas += 1
            if self.tentativas == 10:
                self.clearConsole()
                print("Big L dude!")
                self.updateMan()
            else: 
                self.clearConsole()
                print("Nop, tenta de novo")
                self.game(palavra)

    # Função que verifica se adivinhei a letra
    def letterGuess(self, palavra, guess):
        self.clearConsole()
        if guess in palavra:
            self.listOfGuesses.append(guess)
            if self.win(palavra) == True:
                print(f"GG man, és o maior da tua terra. A palavra era {palavra}.")
            else:
                print("Boa!")
                self.game(palavra)
        else:
            self.tentativas += 1
            if self.tentativas == 10:
                self.clearConsole()
                print("Big L dude! Dedica-te à pesca")
                self.updateMan()
            else:
                self.clearConsole()
                print("Nop, tenta de novo")
                self.game(palavra)

    def win(self, palavra):
        r = True
        for letra in palavra:
            for letraGuess in self.listOfGuesses:
                if letra == "-" or letra == " ":
                    r = True
                    break
                elif letra == letraGuess:
                    r = True
                    break
                else:
                    r = False
            if r == False:
                r = False
                break        
        return r

    def updateMan(self):
        if self.tentativas == 1:
            print("\n\n\n\n\n___")
        elif self.tentativas == 2:
            print(" | ")
            print(" | ")
            print(" | ")
            print(" | ")
            print("_|_")
        elif self.tentativas == 3:
            print(" _______")
            print(" | ")
            print(" | ")
            print(" | ")
            print(" | ")
            print("_|_")
        elif self.tentativas == 4:
            print(" _______")
            print(" |      |")
            print(" | ")
            print(" | ")
            print(" | ")
            print("_|_")
        elif self.tentativas == 5:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" | ")
            print(" | ")
            print("_|_")
        elif self.tentativas == 6:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" |      |")
            print(" | ")
            print("_|_")
        elif self.tentativas == 7:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" |      |/")
            print(" | ")
            print("_|_")
        elif self.tentativas == 8:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" |     \|/")
            print(" | ")
            print("_|_")
        elif self.tentativas == 9:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" |     \|/")
            print(" |       \ ")
            print("_|_")
        elif self.tentativas == 10:
            print(" _______")
            print(" |      |")
            print(" |      O")
            print(" |     \|/")
            print(" |     / \ ")
            print("_|_")
  
hangman()

# print("   _______ ")        
# print("   |     | ")
# print("   |     O ")
# print("   |    \|/")
# print("   |     | ")
# print("  _|_   / \ ")