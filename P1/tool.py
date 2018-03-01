import re



def match (string1, string2):


	r = "^" + string1.replace ("*", "[A-Za-z .-ÀÁÂÃÄÅàáâãäåÒÓÔÕÖØòóôõöøÈÉÊËèéêëÇçÌÍÎÏìíîïÙÚÛÜùúûüÿÑñ_]{1,}").replace("%", "[A-Za-z .-ÀÁÂÃÄÅàáâãäåÒÓÔÕÖØòóôõöøÈÉÊËèéêëÇçÌÍÎÏìíîïÙÚÛÜùúûüÿÑñ_]") + "$"
	if re.match(r, string2):
		
		return string2

	else :
		return ""
		


def getCoAuthorList (content, name1, res, parcoured,size):
		
	
	coauteurs = list()


	#if name1 not in parcoured:
	for publication in content : 

				#on cherche si key = 'author'. publication ['author'] renvoie la liste d'autheur pour une publication
		for key in publication.keys():
			if key == 'author':
				if name1 in publication["author"]:
					for np in publication["author"]:
						if np not in coauteurs and np !=name1:
								
								coauteurs.append (np)
					


	

	if name1 not in parcoured:
		rep = dict ()
		rep["parent"] = name1
		rep["marked"] = False
		rep["fils"] = coauteurs
		res.append (rep)
		parcoured.append (name1)
		
		


	for coa in coauteurs:
		size -=1
		if size > 0:
			getCoAuthorList (content, coa, res, parcoured, size)
			
		
		
	

	
		



			
	
def calculateDistance (array, name ,name1, name2, count, res, parcoured) : 
	
	current = list ()
	end = list ()
	for elem in array :
		if elem["parent"] == name1:
			current = elem["fils"]

		if elem["parent"] == name2:
			end = elem["fils"]
	
		
	

	for currentP in current : 
		if currentP in end:
			res.add (currentP)
			calculateDistance (array, name ,name1, currentP, count, res, parcoured)


		else:
			parcoured.append (name1)
				

	







