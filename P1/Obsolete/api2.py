from bottle import route, run, template



LIMIT_YEAR = 5
LIMIT_PUBLICATION =100

#Stockage dans une variable le contenu du fichier csv
##################################
content = list ()
with open ('./dblp.csv', 'r') as fr: 
	content = fr.readlines()
	fr.close()

#Recherche de la publication en utilisant un identifiant de l'article (ex: http://localhost:8080/publications/journals/acta/GlabbeekGO15)
##################################
@route('/publications/<pubID:path>')
def getPublicationFromID(pubID):
	print (pubID)
	res = ''
	found = False
	for line in content :
		key = line.split(';')[0].split(' ')
		
		if found == True: 
			found = False
			break	

		for value in key:
			
			if value[0:4] == 'key=':
					
				if value [4:] == pubID:
					res = line
					found = True
	if res == '':
		return 'Error'
	
	else :
		res = res.replace(';', ' ')
		res += '<br />'
		print(res)
		return (res)


#Affiche les 100 premieres publications
####################################
@route('/publications')
def getPublications():
	count = 0	
	res = ''
			
	for line in content :	
	
		if count > LIMIT_PUBLICATION :
			break

		else :
			count += 1
			res += line.replace(';',' ') 
			res += '<br />'
			
			
		
	if res == '':
		return 'Error'
	
	else :
		res = res.replace(';', ' ')
		res += '<br />'
		
		return (res)


#Get author info
###################################
@route('/authors/<name>')
def getAuthorsInfo(name):
	nb_pub = 0
	coauteurs = list()
	
	#format d'entrée prenom_nom
	name = name.replace('_', ' ')
		
	for line in content : 
		
		#fields = champs dans un ligne
		fields = line.split(';')

		coauteursTemp = list ()
		isCorrectData = False

		#value = un champ
		for value in fields :
			if value[:6] == 'author':

				if value [8:] == name:
					nb_pub+=1
					isCorrectData = True

				else :
					coauteursTemp.append(value[8:])
		
		if isCorrectData ==True:
			for coaTemp in coauteursTemp :
				exist = False	
				for coa in coauteurs :
					if coa == coaTemp :
						exist =True

				if exist ==False :
					coauteurs.append(coaTemp)

				else :
					exist = True
	
	return name + " a " + str(nb_pub) + " publications et " + str(len(coauteurs)) + " coauteurs."	
		
				
#Get author publications
###################################

@route('/authors/<name>/publications')
def getAuthorsPub(name):
	
	res = ''

	#format d'entrée prenom_nom
	name = name.replace('_', ' ')
		
	for line in content : 
		
		#fields = champs dans un ligne
		fields = line.split(';')

		

		#value = un champ
		for value in fields :
			if value[:6] == 'author':

				if value [8:] == name:
					res += line
					res += '<br />'

	
	return res	


#Get coauthors
###################################
@route('/authors/<name>/coauthors')
def getCoAuthors(name):
	nb_pub = 0
	coauteurs = list()
	
	#format d'entrée prenom_nom
	name = name.replace('_', ' ')
		
	for line in content : 
		
		#fields = champs dans un ligne
		fields = line.split(';')

		coauteursTemp = list ()
		isCorrectData = False

		#value = un champ
		for value in fields :
			if value[:6] == 'author':

				if value [8:] == name:
					nb_pub+=1
					isCorrectData = True

				else :
					coauteursTemp.append(value[8:])
		
		if isCorrectData ==True:
			for coaTemp in coauteursTemp :
				exist = False	
				for coa in coauteurs :
					if coa == coaTemp :
						exist =True

				if exist ==False :
					coauteurs.append(coaTemp)

				else :
					exist = True
	
	return coauteurs	
		

run(host='localhost', port=8080)

