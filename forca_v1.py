# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor OK
	def __init__(self, word):
		self.word = word
		self.missed = []
		self.correct = []
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			return self.correct.append(letter)
		return self.missed.append(letter)
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		maxChance = 6
		if len(self.missed) == maxChance:
			return True
		return False
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		list1 = []
		for l in self.word:
			if l not in list1:
				list1.append(l)
			continue
		if len(list1) == len(self.correct):
			return True
		return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		numLetter = []
		agrVai = ''
		index = 0
		for i in range(len(self.word)):
			numLetter.append('_')
		for elem in numLetter:
			agrVai += elem + ' '
		if len(self.correct) == 0:
			print('\nPalavra: ' + agrVai)
		else:
			for word in self.correct:
				for w in self.word:
					if w == word:
						numLetter.pop(index)
						numLetter.insert(index, w)
						index += 1
					else:
						index += 1
						continue
				index = 0
			agrVai = ''
			for word in numLetter:
				agrVai += word + ' '
			print('\nPalavra: ', agrVai)
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		if len(self.missed) != 0:
			index = len(self.missed)
			print(board[index])
		else:
			index = len(self.missed)
			print(board[index])




# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over() and not game.hangman_won():
		correct = ''
		wrong = ''

	# Verifica o status do jogo
		game.print_game_status()
		game.hide_word()

		if game.missed == []:
			print('\nLetras erradas: ')
		else:
			for letter in game.missed:
				wrong += letter + '-'
			print('\nLetras erradas: ' + wrong)
		if game.correct == []:
			print('\nLetras corretas: ')
		else:
			for letter in game.correct:
				correct = correct + letter + '-'
			print('\nLetras corretas: ' + correct)
		print('\n\n')
		letter = input("Digite uma letra: ")
		game.guess(letter)


	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
