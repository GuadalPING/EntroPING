import math  # import math

__author__ = "Eduardo"
__copyright__ = "Copyright 2019, GuadalPING SL"
__credits__ = ["Ismael Joyera Aguilar", "Diego Gamaza", "Alejandro Santamaría"]
__license__ = "GNU/GPLv3"
__version__ = "1.0.0"
__email__ = "guadalping@gmail.com"

class colours:  # for printing colored text in terminal
    def __init__(self):
        self.red = "\033[1;31m"
        self.yellow = "\033[93m"
        self.end = "\033[0m"

class TextInfo:  # class Text info

	def __init__(self, userfile):  # constructor
		self.a = {}  # dict for vars with number
		self.text = ""  # string from file
		self.length = 0  # length of string
		self.entropy = 0  # entropy
		self.file = userfile  # file pwd

	def getTextLen(self):  # first method, get text from file and length
		with open(self.file, "r") as e:
			self.text = e.readlines()
			self.text = ''.join(self.text).replace("\n", "").lower()
			self.length = len(self.text)
			
	def getChars(self):  # save iterations of chars to "a" dict
		for i in self.text:  # for char in string
			if i not in self.a:  # if char not in a ( 0 ), set to 1
				self.a[i] = 1
			else:  # if is in dict
				self.a[i] += 1  # increase
				
	def ProbAndEntropy(self):  # get Prob of char and entropy of string
		for i in self.a:  # for char in string
			prob = self.a[i] / (self.length)  # prob
			I = math.log((1/prob), 2)  # get I
			self.entropy += prob*I
			yield "probabilidad de {0} es {1:.4f}, I: {2:.4f}".format(i,prob, I)  # for each iteration return prob and I
		yield colourful.yellow + "Entropía: {:.4f}".format(self.entropy) + colourful.end # when bucle ends ( all chars ), returns entropy

if __name__ == "__main__":  # execute all methods
	colourful = colours()
	print(colourful.red + "Guadalping Tools" + colourful.end)
	files = input("Ruta del archivo (solo nombre si es la misma ruta): ")
	getTextInfo = TextInfo(files)
	getTextInfo.getTextLen()
	getTextInfo.getChars()
	for char in getTextInfo.ProbAndEntropy():
		print(char)
