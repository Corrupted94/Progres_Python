from bottle import route, run, template,request
import json
import tool


LIMIT_YEAR = 5
LIMIT_PUBLICATION =100

#Stockage dans une variable le contenu du fichier json
##################################
content = list ()
with open ('./dblp_1.json', 'r') as fr:
	#on met le contenu du json dans content 
	content = json.load (fr)
	fr.close()


#Recherche de la publication en utilisant un identifiant de l'article (ex: http://localhost:8080/publications/journals/acta/GlabbeekGO15)
##################################
@route('/publications/<pubID:path>')
def getPublicationFromID(pubID):
	print (pubID)
	res = ''
	found = False

	#Parcours de chaque publication dans la liste de publications
	for publication in content :
		if found == True: 
			break	

		#Structure : { key1 : value1, ...}. Alors on verifie si value == l'identifiant. Si la publication au format JSON
		for value in publication.values():
			if value == pubID : 
				res = publication
				found = True
	#Erreur
	if res == '':
		return json.loads('{\"erreur\" : \"identifiant non reconnu\"}')
	
	else :
		print (res)
		return (res)



#______________________________________________________________________________#

#Recupere les informations tq le nombre de coauteurs et nombre de publications d'un autheur donné 
###################################
@route('/authors/<name>')
def getAuthorsInfo(name):
	nb_pub = 0
	nb_coautheurs = 0
	coauteurs = list()
	templist = list ()

	for publication in content : 

		#on cherche si key = 'author'. publication ['author'] renvoie la liste d'autheur pour une publication
		for key in publication.keys():
			if key == 'author':
				for author in publication ["author"]:
					templist.append (author) 
					
					#si dans liste des auteurs de la publication, on trouve l'auteur qu'on cherche, alors nb_pub +1 
					if author == name :
						nb_pub += 1
						for coauthTemp in templist:
							exist = False
							for coauth in coauteurs :
								if coauthTemp != name and coauth == coauthTemp :
										exist =True
							#si un coauteur ne se trouve pas dans la liste des coautheurs alors nb_coauteurs +1
							if exist == False :
								coauteurs.append (coauthTemp)
								nb_coautheurs += 1
				templist = list ()
							
								
						
			
	if nb_pub != 0:
		return json.loads ('{"publication_count" : "'+ str(nb_pub)+ '", "coauthors_count" : "' + str(nb_coautheurs) + '"}')

		
	else :
		return json.loads('{\"erreur\" : \"nom de l auteur inconnu\"}')
		
	
#______________________________________________________________________________#

#Recupere la liste des coauteurs d'un autheur donné
###################################
@route('/authors/<name>/coauthors')
def getCoAuthors(name):

	nb_coauteurs = 0
	coauteurs = list()
	templist = list ()

	for publication in content : 

		#on cherche si key = 'author'. publication ['author'] renvoie la liste d'autheur pour une publication
		for key in publication.keys():
			if key == 'author':
				for author in publication ["author"]:
					templist.append (author) 
					
					#si dans liste des auteurs de la publication, on trouve l'auteur qu'on cherche
					if author == name :
						
						for coauthTemp in templist:
							exist = False
							if coauthTemp == name :
								exist = True
							
							for coauth in coauteurs :
								if coauth == coauthTemp :
									exist =True

							#si un coauteur ne se trouve pas dans la liste des coautheurs alors nb_coauteurs +1
							if exist == False :
								coauteurs.append (coauthTemp)
								nb_coauteurs += 1
				templist = list ()
												
						
			
	if nb_coauteurs != 0:
		return json.loads ('{"coauthor_count" : "'+ str(nb_coauteurs)+ '", "coauthors" : ' + str (coauteurs).replace ('\'', '\"') + '}')

		
	else :
		return json.loads('{\"erreur\" : \"cet auteur n a pas de coauteurs\"}')
		
		



#______________________________________________________________#
#Recupere la liste des publications d'un auteur
###################################

@route('/authors/<name>/publications')
def getAuthorsPub(name):
	
	res = '{\"publications\" : ['
	count = 0
		
	for publication in content : 
				#on cherche si key = 'author'. publication ['author'] renvoie la liste d'autheur pour une publication
		for key in publication.keys():
			if key == 'author':
				for author in publication ["author"]: 
					
					#si dans liste des auteurs de la publication, on trouve l'auteur qu'on cherche
					if author == name :
						if count != 0:
							res+= ','
								
						res += json.dumps(publication)
						count += 1

		
	
	if res == '{\"publications\" : [':
		return json.loads('{\"erreur\" : \"impossible de retourner les publications de l auteur\"}')
	
	else :	
		res += ']}'
		return (json.loads (res))


#__________________________________________________________________#
#Rechercher un auteur
###################################
@route ('/search/authors/<searchString>')
def searchAuthor (searchString):
		
		
		auteurs = list()
	
	
		for publication in content : 

		#on cherche si key = 'author'. publication ['author'] renvoie la liste d'autheur pour une publication
			for key in publication.keys():
				if key == 'author':
	
						for aut in publication["author"]:

							exist = False
							for aut2 in auteurs :
								
								if aut == aut2 :
									exist =True
							#appel du regex pour faire un match
							if exist == False :
								regexmatch = tool.match (searchString, aut)
								if regexmatch != "":
									auteurs.append (regexmatch)					
		#Default 
		start = request.query.start
		count = request.query.count
		if request.query.start == "":
			start = 0
		else :
			start = int (request.query.start)
		if request.query.count == "":
			count = LIMIT_PUBLICATION
		else :
			count = int (request.query.count)
		

		if start > len(auteurs):
			return json.loads('{\"erreur\" : \"auteurs[start_count] : out of array\"}')
		
		else : 
			first = True
			res = '{\"searchString\" : \"' + searchString + '\",\"list\" : ['
			if count > len(auteurs):
				count = len(auteurs)
			for i in range(start, start+count):	
				if first == False:
					res+= ','
				first = False
				res += '\"' + auteurs[i] + '\"'

			res += ']}'
			return json.loads(res)


#________________________________________________________________#
#Search publication 
###############
@route ('/search/publications/<searchString>')
def searchPublication (searchString):
	
	publicationlist = list ()
	
	for publication in content : 

		exist = False
		for tempPub in publicationlist :
					
			if tempPub == publication["title"] :
				exist = True
			
		print (publication["title"])	
		#appel du regex pour faire un match
		if exist == False :
			regexmatch = tool.match (searchString, publication["title"])
			if regexmatch != "":
				publicationlist.append (regexmatch)

	

	
	#Default 
	start = request.query.start
	count = request.query.count
	if request.query.start == "":
		start = 0
	else :
		start = int (request.query.start)
	if request.query.count == "":
		count = LIMIT_PUBLICATION
	else :
		count = int (request.query.count)
	

	if start > len(publicationlist):
		return json.loads('{\"erreur\" : \"publication[start_count] : out of array\"}')
	
	else : 
		first = True
		res = '{\"searchString\" : \"' + searchString + '\",\"list\" : ['

		if count > len(publicationlist):
			count = len(publicationlist)
		for i in range(start, start+count):	
			if first == False:
				res+= ','
			first = False
			res += '\"' + publicationlist[i] + '\"'
		
		res += ']}'

		print (res)
		return json.loads(res)



#______________________________________________________#
#________________________________________________________________#
#Get Distance 
###############
#@route ('/authors/<name1>/distance/<name2>')
#def getDistance (name1, name2):

#	parcoured = list ()
#	print (tool.getCoAuthorList (content, name1, name2, parcoured))

		

	

	


run(host='localhost', port=8080)

