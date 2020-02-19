import random
import sys

print('What is your name?')
name=input()

cat = {'name':'cat', 'domestic':'is', 'sound':'meows', 'clue':'is a feline'}
dog = {'name':'dog', 'domestic':'is', 'sound':'barks', 'clue':"is the man's best friend"}
elephant = {'name':'elephant', 'domestic':"isn't", 'sound':'It has a long nose', 'clue':'it has really big ears'}


Animallist=[cat, dog, elephant]
SecretAnimal=random.choice (Animallist)

print (SecretAnimal['name'])

print(name+', I am thinking an animal')

print('Take a guess')
animal_guess=input()

if SecretAnimal['name']!=animal_guess:
    print ('Nope, I could give you a clue ', SecretAnimal['domestic'], ' a domestic one. '
    'Try Again')
    animal_guess=input()
else:
    print('Perfect!!, '+name+' you have guessed my animal')
    sys.exit()

if SecretAnimal['name'] != animal_guess:
    print ("nope, I could give you a second clue,", "it", SecretAnimal ['sound'])
    animal_guess=input()
else:
    print('Perfect!!, '+name+' you have guessed my animal')
    sys.exit()

    
if SecretAnimal['name']!= animal_guess:
    print ("nope, I could give you a third clue,", "it", SecretAnimal ['clue'])
    print('Last chance')
    animal_guess=input()
else:
    print('Perfect!!, '+name+' you have guessed my animal')
    sys.exit()
 
