# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi,Mr Shakespeare, nous avons beau être ou ne pas être,nous sommes !","On doit pouvoir choisir entre s'écouter parler et se faire entendre"]

characters = ["alvin et les Chipmunks","Babar","Betty Boop","Calimero","Casper","Le chat potté","Kirikou"]


def show_random_quote(my_list):
	
	item = my_list[0]
	return item

user_answer = input("tapez entree pour connaitre une autre citation ou B pour quitter")


while user_answer != "B":
	print(show_random_quote(quotes))

	user_answer = input("tapez entree pour connaitre une autre citation ou B pour quitter")

for character in characters :

        n_character = character.capitalize()
        print(n_character)
print(show_random_quote(quotes))
