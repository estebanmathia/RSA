import math
from random import *
from tqdm import tqdm

def Chiffrement(e,n,message):


	messageascii = str("")

	for i in range(len(message)):
		nombredezerodefin = 3 - len(str(ord(message[i])))
		if nombredezerodefin == 3:
			nombredezerodefin = 0
		messageascii = str(messageascii) + "0"*int(nombredezerodefin) + str(ord(message[i]))
	#conversion en une chaine de valeur ascii du message

	nombredezerodefin = (len(str(n))-1)-(len(messageascii)%(len(str(n))-1))

	if nombredezerodefin == (len(str(n))-1):
		nombredezerodefin = 0
	messageascii = str(messageascii) + "0"*int(nombredezerodefin)
	#le messageascii contient suffisament de zero de fin pour une découpe en blocs de longueur (n-1) ex de longueur: n=785 longueur = 2

	messagechiffre = []

	for i in range(len(messageascii)//(len(str(n))-1)):
		messagechiffre.append(str(pow(int(messageascii[(i*(len(str(n))-1)):(i+1)*(len(str(n))-1)]),e,n)))

	messagechiffre = ','.join(messagechiffre)
	'''
	messageascii[(i*(n-1)):(i+1)*(n-1)] correspond au debut et fin de chaque bloc de longueur (n-1) ex: n=785 longueur = 2
	qui est ensuite élevé à la puissance e modulo n
	'''
	return messagechiffre


def Dechiffrement(d,n,messagechiffre):



	messagechiffre = messagechiffre.split(',')
	messageascii = str("")
	for i in range(len(messagechiffre)):
		nombredezerodefin = (len(str(n))-1) - len(str(pow(int(messagechiffre[i]),d,n)))
		if nombredezerodefin == len(str(n))-1:
			nombredezerodefin = 0
		messageascii = str (messageascii) + "0"*int(nombredezerodefin) + str(pow(int(messagechiffre[i]),d,n))
	'''
	messagechiffre[(i*(n-1)):(i+1)*(n-1)] correspond au debut et fin de chaque bloc de longueur (n-1) ex: n=785 longueur = 2
	qui est ensuite élevé à la puissance d modulo n
	'''

	message = str("")
	for i in range(len(messageascii)//3):
		message = str(message) + str(chr(int(messageascii[(i*3):(i+1)*3])))
	'''
	l'objectif est de réussir à convertir une suite de chiffre en caracteres ascii
	'''
	return str(message)


def Cle(ordredegrandeur):


	def estpremier(n):
		"""estpremier(n): dit si un nombre est premier (renvoie True ou False)"""
		if n<7:
			if n in (2,3,5):
				return True
			else:
				return False
		# si n est pair et >2 (=2: cas traité ci-dessus), il ne peut pas être premier
		if n & 1 == 0:
			return False
		# autres cas
		k=3
		r=math.isqrt(n)
		while k<=r:
			if n % k == 0:
				return False
			k+=2
		return True

	a = 0
	while not a == 4:
		a in tqdm(range(4))

		if a == 0:
			test = 0
			while test == 0:
				p = randint(1,ordredegrandeur)
				if estpremier(p):
					test = 1
				else:
					test = 0
			a = a + 1
			a in tqdm(range(4))

		if a == 1:
			test = 0
			while test == 0:
				q = randint(1,ordredegrandeur)
				if estpremier(q):
					test = 1
				else:
					test = 0
			a = a + 1
			a in tqdm(range(4))

		if a == 2:
			z = (p-1)*(q-1)
			n = p*q
			e = randint(1,ordredegrandeur)

		
			while not math.gcd(e,z) == 1:
				e = e +1
			a = a + 1
			a in tqdm(range(4))

		if a == 3:
			d = 0
			while not ((d*e)%z) == 1:
				d = d + 1
			a = a + 1
			a in tqdm(range(4))				

	phrasereponseune = "Le couple public (e;n) est : (" + str(e) + ";" + str(n) + "). " + "Le couple privé (d;n) est : (" + str(d) + ";" + str(n) + ")"
	return phrasereponseune


if __name__ == "__main__":
	choix = int(input("Que voulez vous faire ? Chiffrement(1); Déchiffrement(2); Création clé aléatoire(3) : "))

	if choix == 1:
		e = int(input ("e : "))
		n = int(input ("n : "))
		# le couple (e;n) est la clé publique avec e l'exposant et n le module
			
		message = str(input("message : "))
		print(Chiffrement(e,n,message))

	if choix == 2:
		d = int(input("d : "))
		n = int(input("n : "))
		# le couple (d;n) est la clé privé avec d l'exposant et n le module
		messagechiffre = str(input("Message chiffré : "))
		print(Dechiffrement(d,n,messagechiffre))

	if choix == 3:
		ordredegrandeur = int(input("ordre de grandeur ? (ex : 50000) "))
		print(Cle(ordredegrandeur))