from os import system
from random import randint

gametitle = "Castle Dungeons - An interactiive story game"
system("mode 110, 30")
system("title" + gametitle)

def cls():
	system('cls')

character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print("Castle Dungeons - An interactiive fiction game in python")
def Intro():
	print("")
	print("In this adventure, you are the hero.")
	print("Your choices, skills and a bit of luck will influence the outcome of the game.")
	print("")
	print("An evil sorcerer is holding your fellow adventureres capitive.")
	print("Will you succeed to free your friends from the castle dungeon, or peril trying to fight the final boss????")
	print("")
	start=input("Press Enter to continue...")

Intro()

def create_character():
	cls()
	global character_name
	character_name = input("""
	Lets's begin by creating your charcater.
	What is your character name?

		> """)
	global character_race
	while character_race is None:
		race_choice = input("""
		Choose your character race from the list below by entering the relevant number:
		1 - Elf
		2 - DragonBorn

		> """)
		if race_choice=="1":
			character_race="Elf"
		elif race_choice=="2":
			character_race="DragonBorn"
		else:
			print("Not a valid choice!")
	cls()
	global character_class
	while character_class is None:
		class_choice = input("""
		Choose your character class from the list below by entering the relevant number:
		1 - Warrior
		2 - Wizard

		> """)
		if class_choice=="1":
			character_class="Warrior"
		elif class_choice=="2":
			character_class="Wizard"
		else:
			print("Not a valid choice!")

create_character()

def create_character_skill_sheet():
	cls()
	global character_name, character_class, character_race, character_strength, character_life, character_dexterity, character_magic
	print("""
	Now let's determine your character's skills which you will use throughout the game. 
	In this game your character has four skills:

	- Strength, which will be used in combat or strength course test.
	- Dexterity, which will be used for ability test
	- Magic, which will be used for casting spells or use/inspect magic items
	- Life, which determines the life energy, the points lost on injury, 
	  and whenever life reaches 0, your character dies.

	Depending on your race and charcter, you will have a certain point base already calculated by the game.
	You can increase your skills by rolling a 6-faced die.

	Here are yout base Character Skills Sheet
	""")

	character_strength = 5
	character_magic = 0
	character_dexterity = 3
	character_life = 10

	if character_race=="Elf":
		character_strength=character_strength+3
		character_magic+=6
		character_dexterity+=4
		character_life+=2
	elif character_race=="DragonBorn":
		character_strength=character_strength+5
		character_life+=4		

	if character_class=="Warrior":
		character_strength=character_strength+3
		character_life+=3
	elif character_class=="Wizard":
		character_magic+=4

	print("""
	Name: """+character_name+
	"""
	Race: """+character_race+
	"""
	class: """+character_class+
	"""

	strength: """+str(character_strength)+
	"""
	Dexterity: """+str(character_dexterity)+
	"""
	Magic: """+str(character_magic)+
	"""
	Life: """+str(character_life)+"""

	""")

	input("Press enter to apply your skills modifiers...")

create_character_skill_sheet()

def modify_skills():
	cls()
	global character_dexterity, character_strength, character_life
	print("To modify your skills, roll a six face die for each of your skills, and the game will add it to your skills sheet")
	input("Press ENTER to roll for Strength..")
	roll=randint(1, 6)
	print("You rolled: "+str(roll))
	character_strength+=roll
	input("Press ENTER to roll for Dexterity..")
	roll=randint(1, 6)
	print("You rolled: "+str(roll))
	character_dexterity+=roll
	input("Press ENTER to roll for Life..")	
	roll=randint(1, 6)
	print("You rolled: "+str(roll))
	character_life+=roll
	input("Press ENTER to continue..")
	cls()
	print("""
	Congratulations! You have completed your character creation!
	Your final character sheet is:

	Name: """+character_name+
	"""
	Race: """+character_race+
	"""
	class: """+character_class+
	"""

	strength: """+str(character_strength)+
	"""
	Dexterity: """+str(character_dexterity)+
	"""
	Magic: """+str(character_magic)+
	"""
	Life: """+str(character_life)+"""

	""")
	
	input("Press ENTER to begin your adventure, if you dare...")

modify_skills()

def Scene_1():
	cls()
	choice=None
	while choice is None:
		user_input = input("""
		You have enterened the Castle Dungeons..
		It is dark, however thankfully your torch is lit and you a=can see up to 20 feet away from you.
		The stone walls are damp, the smell of rats and orcs is strong.
		You walk down a narrow corridor, until you reach a thick stone wall.

		The corridor continues on the left, and on the right.

		What will you do?

		1 - Turn left
		2 - Turn right
		>""")
		if user_input=="1" or user_input=="left":
			choice="1"
			Scene_2()
		elif user_input=="2" or user_input=="right":
			choice="2"
			Scene_3()
		else:
			print("""
				Not a valid choice, type a number or left/right
				""")

def Scene_2():
	cls()
	choice=None
	while choice is None:
		user_input = input("""
		From the darkness behind you.. you hear a strange noise.

		What will you do?

		1 - Continue walking
		2 - Stop to listen
		>""")
		if user_input=="1" or user_input=="continue":
			choice="1"
			combat()
		elif user_input=="2" or user_input=="stop":
			choice="2"
			skill_check()
		else:
			print("""
				Not a valid choice, type a number or continue/stop
				""")

def Scene_3():
	cls()
	choice=None
	while choice is None:
		user_input = input("""
		From the darkness behind you.. you hear a strange noise.

		What will you do?

		1 - Continue walking
		2 - Stop to listen
		>""")
		if user_input=="1" or user_input=="continue":
			choice="1"
			combat()
		elif user_input=="2" or user_input=="stop":
			choice="2"
			skill_check()
		else:
			print("""
				Not a valid choice, type a number or continue/stop
				""")

def skill_check():
	cls()
	print("A giant rock falls from the ceiling, roll a die to see if you can dodge it... or you will be be crushed???")
	roll=randint(1,6)
	print("You rolled: "+str(roll))
	if roll+character_dexterity>10:
		print("""
		You have doged the rock...but the danger doesn't end here. The voices continues and it seems closer now...
		Are you ready to approach it??
		""")
		input("Press ENTER to continue...")
		combat()
	else:
		print("""
		You were crushed by the rock. You die. The game is over...
		""")
		input("Press ENTER to exit the game...")

def combat():
	cls()
	global character_life
	print("A horrible orc attacks you!")
	input("Press ENTER to continue the fight...")
	orc=[10,14]
	while orc[1]>0 and character_life > 0:
		char_roll = randint(1,6)
		print("You rolled: "+str(char_roll))
		mon_roll = randint(1,6)
		print("Monster rolled: "+str(mon_roll))
		if char_roll+character_strength >= mon_roll+orc[0]:
			print("You hit the monster!")
			orc[1] = orc[1]-randint(1,6)
		else:
			print("The monster hits you!")
			character_life= character_life - randint(1,6)
		if character_life>0:
			print("You defeated the orc!!!")
			input("press ENTER to exit the game....")
		else:
			print("You got defeated by the orc...you die and now you will never be abke to free your friends....")
			input("press ENTER to exit the game....")		
Scene_1()









