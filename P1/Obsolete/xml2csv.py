import xml.sax
import csv

import escape_XMLChar

from xml.sax.saxutils import unescape

LIMIT_YEAR = 5


class MyHandler(xml.sax.ContentHandler):	
	def __init__(self):
		self.donnee = list()
		self.key = ''
		self.publication = False
		print ("------------Init done--------------")
		print ("This process may take several minutes")
		self.authorNumber = 1
		self.importantdata = False
		
		self.isYearBalise = False
		self.correctYear = True

		self.tempString = ''
	
	def startElement(self, name, attrs):

		#si c'est une publication 
		if name == 'article' or name == 'inproceedings' or name == 'proceedings' or name == 'book' or name == 'incollection' or name =='phdthesis' or name == 'mastersthesis' :
			self.publication = True
			self.key += 'type=' + name
			self.donnee.append (self.key)
			self.key = ''
			for (k,v) in attrs.items ():
				if k== 'key':
					self.key += 'key=' + v
					self.donnee.append (self.key)
					self.key = ''
				
					

			
#_____________________________________________________________
		#si balise author
		elif name == 'author' :
			if not self.authorNumber >5:
				self.key += 'author' + str (self.authorNumber) + '='
				self.authorNumber += 1
				self.importantdata = True

		#si balise title
		elif name == 'title' : 
			self.key += 'title='
			self.importantdata = True

		#si balise year
		elif name == 'year' : 
			self.key += 'year='
			self.importantdata = True
			self.isYearBalise = True
		

		#si balise journal
		elif name == 'journal':
			self.key += 'journal='

			self.importantdata = True
		
		#si balise booktitle
		elif name == 'booktitle' :
			self.key += 'booktitle='
			self.importantdata = True

#______________________________________________________________
				

	def endElement(self, name):
		#close balise de type publication
		if name == 'article' or name == 'inproceedings' or name == 'proceedings' or name == 'book' or name == 'incollection' or name =='phdthesis' or name == 'mastersthesis' :
			
			
			if self.correctYear == True: 
				
				writeInCsv (self.donnee)

			#Reset les parametres à la sortie d'une balise de type publication 
			self.publication = False
			self.authorNumber = 1
			self.correctYear = True
			self.donnee = list()
		
		if name == 'author' or name == 'title' or name == 'year' or name == 'journal' or name == 'booktitle' :
			self.donnee.append (escape_XMLChar.xml_Escape(self.tempString))	
			self.tempString = ''		
			self.importantdata = False

		if name == 'year' :
			self.isYearBalise = False
		

			
	
	def characters(self, content):
		if self.publication == True and self.importantdata == True:
			
			if self.isYearBalise == True:
				year = int(content)
				
				if  (year < 2017-LIMIT_YEAR):
					self.correctYear = False			
			
			new_content = self.key + content
			self.tempString += new_content
			self.key = ''
			

def writeInCsv (content):
	
	try : 	
	
		with open ('./dblp.csv', 'a') as csvfile:
			writer = csv.writer(csvfile, delimiter =';')
			writer.writerow (content) 
			

	except IOError : 
		print ('File not found') 
		with open ('./dblp.csv', 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter =';')
			writer.writerow (content) 

			writer.close()
		csvfile.close()



parser = xml.sax.make_parser()

handler = MyHandler()
parser.setContentHandler(handler)
parser.parse(open ("./dblp.xml", 'r'))

print ('Parsing Done')
	
	



