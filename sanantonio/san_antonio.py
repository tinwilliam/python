# -*- coding: utf8 -*-

print("hello you !")

quotes = [
    "Ecoutez-moi,Mr Shakespeare, nous avons beau être ou ne pas être,nous sommes !","On doit pouvoir choisir entre s'écouter parler et se faire entendre"]

characters = ["alvin et les Chipmunks","Babar","Betty Boop","Calimero","Casper","Le chat potté","Kirikou"]

user_answer = input("tapez entree pour connaitre une autre citation ou B pour quitter")
#Show random quote
if user_answer =="B" :
	pass
elif user_answer =="C":
	print("C pas la bonne réponse ! Et ")
else:
	pass
    #show another quote


def show_random_quote(my_list):
	
	#get a random number
	quote = my_list[1]
	print(quote)
	#get a quote from an array
	#show the quote in the interpreter, print
show_random_quote(quotes)