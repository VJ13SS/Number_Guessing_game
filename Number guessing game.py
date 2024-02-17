'''HEY ALL ...THE CODE SHARED BEKOW IS A SIMPLE NUMBER GUESSING GAME WHERE THE COMPUTER WILL GUESS A NUMBER AND THE USERS NEED TO IDENTIFU IT...YOU WILL BE GIVEN TWO CHOICE EASY OR JATD AMD THUS CAN CUSTOMISE YOUR DIFFICULTY AND PLAY THE GAME....
THE CODE USES 5 FUNCTIONS:
	1.random_number
	2.Difficulty
	3.user_input
	4.input_validation
	5.main
I HAD TRIED MY BEST TO INCORPORATE THE LOGIC AND TO DEMONSTRATE THE WORKING OF FUNCTIONS,LOOPS,ERROR HANDLINGS,ETC HERE.. 
HOPE YOU WILL ENJOY

   By VJ 13 SS'''
import random

def random_number():#To generate a random number 
	number=random.randint(0,51)
	return number

def choose_difficulty():
		while True:
			print('\nEnter your mode of difficulty: ')	
			difficulty=input('\nType E-for Easy or H for Hard: ').lower()
			#To check difficulty
			if(difficulty=='easy' or difficulty=='e'):
				turns=10
				break
			elif(difficulty=='hard' or difficulty =='h'):
				turns=5
				break
			else:
				print('Invalid Input Enter again')
				continue
		return difficulty,turns
def user_input(difficulty,turns,num):
			if(num%2!=0):
				num_type = 'odd'
			else:
				num_type='even'
			choice=0
			while (choice<turns):
				if(difficulty=='easy' or difficulty=='e'):
					#Provided hints at easy level
					print(f'\nHint....The number is {num_type}\n')
				try:
					value=int(input('\nEnter the number: '))
				except(ValueError):
					print('Invalid Input')
				else:
						result=input_validation(value,num)
						if(result=='win'):
							print('\nYou won...The number is ',num)
							return #returns back to main function
						if(result=='close'):
							print('\nYou are too close')
							
						if(result=='back'):
							print('\nYou are too back')
						
						if(result=='far'):
							print('\nYou are too far')
							
						choice=choice+1
						print(f'\nYou have {turns-choice} turns left\n')
			print(f'\nYou lose...The number is {num}')
			
def input_validation(value,num):
							if(value>50 or value<0):
								print('\nYour input is more than 50 or less than 0')
								print('Enter again\n')
								return #Control moves bavk to the previous user input function
								
							else:
								if(value==num):
									return 'win'
								elif((num-3)<=value<=(num+3)):
									return 'close'
								elif(value<num-3):
									return 'back'
								else:
									return 'far'
							
def main():
	print('''WELCOME TO NUMBER GUESSING GAME''')
	while True:
		choice=input('\nDo you wish to play the game....?:(Type Y or N) ').lower()
		
		if(choice=='y'):
			print('\nA number is selected in random between 0 and 50 by the computer..Try to guess it amd win the challenge...')
			print('\n')
			number=random_number()#Gets random number
			difficulty,turns=choose_difficulty()#Choose difficulty 
			get_input=user_input(difficulty,turns,number)
		else:
			print('Thank you')
			break
	
main()