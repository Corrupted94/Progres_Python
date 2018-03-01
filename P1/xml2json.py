import xml.sax
import json

import escape_XMLChar

from xml.sax.saxutils import unescape

LIMIT_YEAR = 5


class MyHandler(xml.sax.ContentHandler):	
	def __init__(self):

		###self.donnee c'est un dictionnaire, car on veut dumper les data dans un json
		self.donnee = dict()
		self.key = ''
		self.publication = False
		print ("------------Init done--------------")
		print ("This process may take several minutes")
		self.authorlist = list ()
		self.importantdata = False
		
		self.isYearBalise = False
		self.correctYear = True

		self.tempString = ''
	
	def startElement(self, name, attrs):

		#si c'est une publication 
		if name == 'article' or name == 'inproceedings' or name == 'proceedings' or name == 'book' or name == 'incollection' or name =='phdthesis' or name == 'mastersthesis' :
			self.publication = True

			self.donnee['type'] = name
	
			for (k,v) in attrs.items ():
				if k== 'key':
					self.donnee['key'] = v

				
					

			
#_____________________________________________________________

		#si balise author
		elif name == 'author' :
			self.key = 'author'
			self.importantdata = True

		#si balise title
		elif name == 'title' : 
			self.key = 'title'
			self.importantdata = True

		#si balise year
		elif name == 'year' : 
			self.key = 'year'
			self.importantdata = True
			self.isYearBalise = True
		

		#si balise journal
		elif name == 'journal':
			self.key = 'journal'

			self.importantdata = True
		
		#si balise booktitle
		elif name == 'booktitle' :
			self.key = 'booktitle'
			self.importantdata = True

#______________________________________________________________
				

	def endElement(self, name):
		#close balise de type publication
		if name == 'article' or name == 'inproceedings' or name == 'proceedings' or name == 'book' or name == 'incollection' or name =='phdthesis' or name == 'mastersthesis' :
			
			
			if self.correctYear == True: 
				self.donnee ['author'] = self.authorlist
				writeInJson (self.donnee)

			#Reset les parametres à la sortie d'une balise de type publication 
			self.publication = False
			self.correctYear = True
			self.donnee = dict ()
			self.authorlist = list ()
		
		if name == 'title' or name == 'year' or name == 'journal' or name == 'booktitle' :
			self.donnee [self.key] =  (escape_XMLChar.xml_Escape(self.tempString))	
			self.tempString = ''		
			self.importantdata = False
			self.key = ''

		if name == 'author' :
			self.authorlist.append(escape_XMLChar.xml_Escape(self.tempString))	
			self.tempString = ''		
			self.importantdata = False
			self.key = ''

		if name == 'year' :
			self.isYearBalise = False
		

			
	
	def characters(self, content):
		if self.publication == True and self.importantdata == True:
			
			if self.isYearBalise == True:
				year = int(content)
				
				if  (year < 2017-LIMIT_YEAR):
					self.correctYear = False			
			
			self.tempString += content
			

####Valueur static pour savoir si c'est la premiere dump dans le fichier json
def firstElem ():
	firstElem.boolean = True
	
firstElem.boolean = False			


###Ecriture dans le Json (et creation du fichier)
def writeInJson (content):
	
	try : 	
		if firstElem.boolean == False :
			with open ('./dblp.json', 'w') as jsonfile:
				jsonfile.write ('[')
				json.dump (content, jsonfile)
				firstElem()
			jsonfile.close()
			
		else :
			with open ('./dblp.json', 'a') as jsonfile:
				jsonfile.write (',')
				json.dump (content, jsonfile)
				
			jsonfile.close()

		
			
	except IOError : 
		print ('Error : Impossible to dump in Json') 
	



parser = xml.sax.make_parser()


handler = MyHandler()
parser.setContentHandler(handler)
parser.parse(open ("./dblp.xml", 'r'))

####Fermeture du crochet du json
with open ('./dblp.json', 'a') as jsonfile:
	jsonfile.write (']')
				
jsonfile.close()



print ('------------Parsing Done-------------')


	
	



