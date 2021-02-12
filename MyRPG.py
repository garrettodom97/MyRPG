
import random
import sys

# class for weapons
class Weapon:

	# method to create weapon instances and assgin them proper damages and crit chances
	def __init__(self, type):
		self.name = type
		if (type == "daggers"):
			self.damage = 4
			self.crit = .7
		elif (type == "axe"):
			self.damage = 7
			self.crit = .23
		elif (type == "staff"):
			self.damage = 3
			self.crit = .05
		elif (type == "sword"):
			self.damage = 6
			self.crit = .3
		elif (type == "greatsword"):
			self.damage = 9
			self.crit = .1
		elif (type == "bow"):
			self.damage = 5
			self.crit = .55
		elif (type == "katana"):
			self.damage = 6
			self.crit = .4
		elif (type == "none"):
			self.damage = 1
			self.crit = .02
		else:
			print("Invalid Weapon Type")
		self.type = type

# classs for potions
class Potion:

	# method to create potion instances 
	def __init__(self, type):
		self.name = type
		if (type == "health potion"):
			self.effect = 25
		elif (type == "sp potion"):
			self.effect = 20
		else:
			print("Invaid Potion Type")


# class for armor
class Armor:

	# method to create armor instances and assign them proper AC values
	def __init__(self, type):
		self.name = type
		if (type == "plate"):
			self.AC = 7.5
			self.speed = 3
		elif (type == "chain"):
			self.AC = 8
			self.speed = 4
		elif (type == "leather"):
			self.AC = 8.5
			self.speed = 6
		elif (type == "robes"):
			self.AC = 9
			self.speed = 8
		elif (type == "none"):
			self.AC = 10
			self.speed = 10
		else:
			print("Invalid Armor Type")
		self.type = type

# class common to all characters
class RPGCharacter:
	
	# method for one character to attack another
	def fight(self, target):
		print(self.name, "attacks", target.name, "with a(n)", self.weapon.name)
		# check if thief dodged
		if isinstance(target, Thief):
			dodge = target.checkDodge()
			if (dodge == 1):
				print("Attack was dodged!")
				return
		# check if attack hits based on armor class
		hit_calc = random.randint(1, 100)
		if (100 * target.armor.AC < hit_calc):
			print("Attack missed!")
			return
		# calculate if a critical hit has activated
		crit_calc = random.randint(1, 100)
		if(100 * self.weapon.crit > crit_calc):
			target.health = target.health - round((self.weapon.damage * 2))
			print("Critical Hit for 2x Damage!")
			print(self.name, "does", self.weapon.damage * 2, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
		# deal normal damage otherwise
		else:
			target.health = target.health - self.weapon.damage
			print(self.name, "does", self.weapon.damage, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")

	# method to check if a target's health is still positive
	def checkForDefeat(self):
		if (self.health <= 0):
			print(self.name, "has been defeated!\n")
			print("Thanks for playing!")
			sys.exit()

	# method to dispaly all stats of a character
	def show(self):
		print()
		print(" ", self.name)
		print("    Current Health:", self.health)
		print("    Current Spell Points:", self.spellpoints)
		print("    Wielding:", self.weapon.name)
		print("    Wearing:", self.armor.name)
		print("    Armor Class:", self.armor.AC)
		print()

# subclass of RPGcharacter for the Fighter class
class Fighter(RPGCharacter):

	# method to create fighter instance and assign them proper stats
	def __init__(self, name):
		self.name = name
		none1 = Armor("none")
		self.armor = none1
		none2 = Weapon("none")
		self.weapon = none2
		self.health = 40
		self.spellpoints = 0

	# method for equipping fighter instance with a weapon instance
	def wield(self, type):
		self.weapon = type
		if (self.weapon.name == "sword" or self.weapon.name == "greatsword" or\
			self.weapon.name == "axe"):
			print(self.name, "is now wielding a(n)", self.weapon.name)
		else:
			print("Invalid weapon for this character class")

	# method for unequpping weapon instance
	def unwield(self):
		noneWpn = Weapon("none")
		self.weapon = noneWpn
		print(self.name, "is no longer wielding anything.")

	# method for equipping fighter instance with an armor instance
	def putOnArmor(self, type):
		self.armor = type
		if (self.armor.name == "plate" or self.armor.name == "chain" or\
			self.armor.name == "leather"):
			print(self.name, "is now wearing", self.armor.name)
		else:
			print("Armor type not allowed for this character class")

	# method for unequpping armor instance
	def takeOffArmor(self):
		noneArm = Armor("none")
		self.armor = noneArm
		print(self.name, "is no longer wearing anything.")

	# method for atcitivatin berserk mode
	def bash(self, target):
		damage_hold = self.weapon.damage
		self.weapon.damage = round(self.weapon.damage * 1.5)
		target.health = target.health - self.weapon.damage
		print(self.name, "bashed", target.name, "dealing", self.weapon.damage, "damage.")
		print(target.name, "is now down to", target.health, "health")
		self.weapon.damage = damage_hold
		self.health = self.health - self.weapon.damage
		print(self.name, "took", self.weapon.damage, "points of damage from bashing.")


# subclass of RPGcharacter for the wizard class
class Wizard(RPGCharacter):

	# method to create wizard instance and assign them proper stats
	def __init__(self, name):
		self.name = name
		none1 = Armor("none")
		self.armor = none1
		none2 = Weapon("none")
		self.weapon = none2
		self.health = 35
		self.spellpoints = 20

	# method for equipping wizard instance with a weapon instance
	def wield(self, type):
		self.weapon = type
		if (self.weapon.name == "staff"):
			print(self.name, "is now wielding a(n)", self.weapon.name)
		else:
			print("Invalid weapon for this character class")

	# method for unequpping weapon instance
	def unwield(self):
		noneWpn = Weapon("none")
		self.weapon = noneWpn
		print(self.name, "is no longer wielding anything.")

	# method for equipping wizard instance with an armor instance
	# regulates the wizard armor restrictions
	def putOnArmor(self, type):
		self.armor = type
		if (self.armor.name == "robes"):
			print(self.name, "is now wearing", self.armor.name)
		else:
			print("Armor type not allowed for this character class")

	# method for unequpping armor instance
	def takeOffArmor(self):
		noneArm = Armor("none")
		self.armor = noneArm
		print(self.name, "is no longer wearing anything.")

	# method to cast spell at a target
	def castSpell(self, spell, target):

		# displays spell being cast and the target
		print(self.name, "casts", spell, "at", target.name)

		# returns error message if spell name is not defined
		if (spell != "fireball" and spell != "lightning bolt" and spell != "heal"\
			and spell != "blizzard" and spell != "restore sp"):
			print("Unknown spell name. Spell Failed.")
			return -1
		# deal proper damage for spell and subtrat proper spell points from caster
		elif (spell == "fireball" and self.spellpoints >= 3):
			self.spellpoints -= 3
			target.health -= 5
			print(self.name, "does", 5, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
		elif (spell == "lightning bolt" and self.spellpoints >= 5):
			self.spellpoints -= 5
			target.health -= 7
			print(self.name, "does", 7, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
		elif (spell == "blizzard" and self.spellpoints >= 10):
			self.spellpoints -= 10
			target.health -= 10
			print(self.name, "does", 10, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
		elif (spell == "restore sp"):
			if (self.spellpoints < 5):
				self.spellpoints += 15
				restore = 15
			else:
				restore = 20 - self.spellpoints
				self.spellpoints = 20
				print(self.name, "restores", restore, "spell points")
			print(target.name, "now has", target.spellpoints, "spellpoints")
		# heal target without going over maximum health
		elif (spell == "heal" and self.spellpoints >= 5):
			self.spellpoints -= 5
			if isinstance(target, Fighter):
				if (target.health < 30):
					target.health += 10
					heal = 10
				else:
					heal = 40 - target.health
					target.health = 40
			if isinstance(target, Wizard):
				if (target.health < 25):
					target.health += 10
					heal = 10
				else:
					heal = 35 - target.health
					target.health = 35
			if isinstance(target, Thief):
				if (target.health < 20):
					target.health += 10
					heal = 10
				else:
					heal = 30 - target.health
					target.health = 30
			print(self.name, "heals", target.name, "for", heal, "health points")
			print(target.name, "is now at", target.health, "health")
		# print error message if target doesn't have enough spell points to cast desired spell
		else:
			print("Insufficient spell points")
			return -1

class Thief(RPGCharacter):

	# method to create thief instance and assign them proper stats
	def __init__(self, name):
		self.name = name
		none1 = Armor("none")
		self.armor = none1
		none2 = Weapon("none")
		self.weapon = none2
		self.health = 30
		self.spellpoints = 0

	# method for equipping thief instance with a weapon instance
	def wield(self, type):
		self.weapon = type
		if (self.weapon.name == "daggers" or self.weapon.name == "bow" or\
			self.weapon.name == "katana"):
			print(self.name, "is now wielding a(n)", self.weapon.name)
		else:
			print("Invalid weapon for this character class")

	# method for unequpping weapon instance
	def unwield(self):
		noneWpn = Weapon("none")
		self.weapon = noneWpn
		print(self.name, "is no longer wielding anything.")

	# method for equipping thief instance with an armor instance
	# regulates the thief armor restrictions
	def putOnArmor(self, type):
		self.armor = type
		if (self.armor.name == "chain" or self.armor.name == "leather"):
			print(self.name, "is now wearing", self.armor.name)
		else:
			print("Armor type not allowed for this character class")

	# method for unequpping armor instance
	def takeOffArmor(self):
		noneArm = Armor("none")
		self.armor = noneArm
		print(self.name, "is no longer wearing anything.")

	# method for giving thief a chance to dodge
	def checkDodge(self):
		chance = random.randint(1, 100)
		if (chance <= 30):
			return 1
		else:
			return 0

# method to battle first tournament opponent
def battleGrale(player1, Grale, dict, player1class, player1name, player2name):

	turn1 = 1
	turn2 = 1

	bash1 = 1
	bashGrale = 1

	print("Beginning battle against Grale the Mighty\n")

	while True:
		print("Player 1's turn: \n")
		print("Enter a command followed by a comma and space, then a target for the command")
		print("If the command is an attack or spell, the target is a character")
		print("If the command is to EQP the target is the desired weapon or armor. If it is to unequip, the target is 'none'")
		print("**ALL TARGETS IN LOWERCASE UNLESS CHARACTER NAME**")
		print("Commands:")
		print("ATK for attack")
		print("EQP for equip")
		print("CAST for casting a spell")
		print("UNEQ for unequpping any weapon and using bare hands")
		print("BASH for fighter ability: 1.5x dmg but take weapon's damage")
		print("POA for putting on armor")
		print("TOA for taking off armor\n")

		print("\n****************************************************************************\n")

		# loop for player to equip and then attack or cast
		didBash = turn(player1, player1class, player1name, turn1, bash1, dict, Grale, player2name)
		if (didBash == 1):
			bash1 = 0

		turn1 += 1
		if (bash1 < 3):
			bash1 += 1

		player1.checkForDefeat()

		if (Grale.health <= 0):
			print("Grale has been defeated!\n")
			print("****************************************************************************\n")
			return

		print("****************************************************************************\n")

		if (turn2 <= 1):
			Grale.wield(dict["sword"])
			Grale.putOnArmor(dict["leather"])

		Grale_move = random.randint(1, 100)
		if (bashGrale == 3 and Grale_move <= 70):
			Grale.bash(player1)
			bashGrale = 1
		else:
			Grale.fight(player1)

		turn2 += 1
		if (bashGrale < 3):
			bashGrale += 1

		player1.checkForDefeat()

		if (Grale.health <= 0):
			print("Grale has been defeated!\n")
			print("****************************************************************************\n")
			return

		player1.show()
		Grale.show()

		print("****************************************************************************\n")

# method to battle the second opponent
def battleSeriph(player1, Seriph, dict, player1class, player1name, player2name):

	turn1 = 1
	turn2 = 1

	bash1 = 1

	print("Beginning battle against Seriph the Crafty\n")

	while True:
		print("Player 1's turn: \n")
		print("Enter a command followed by a comma and space, then a target for the command")
		print("If the command is an attack or spell, the target is a character")
		print("If the command is to EQP the target is the desired weapon or armor. If it is to unequip, the target is 'none'")
		print("**ALL TARGETS IN LOWERCASE UNLESS CHARACTER NAME**")
		print("Commands:")
		print("ATK for attack")
		print("EQP for equip")
		print("CAST for casting a spell")
		print("UNEQ for unequpping any weapon and using bare hands")
		print("BASH for fighter ability: 1.5x dmg but take weapon's damage")
		print("POA for putting on armor")
		print("TOA for taking off armor\n")

		print("\n****************************************************************************\n")

		# loop for player to equip and then attack or cast
		didBash = turn(player1, player1class, player1name, turn1, bash1, dict, Seriph, player2name)
		if (didBash == 1):
			bash1 = 0

		turn1 += 1
		if (bash1 < 3):
			bash1 += 1

		player1.checkForDefeat()

		if (Seriph.health <= 0):
			print("Seriph has been defeated!\n")
			print("****************************************************************************\n")
			return

		print("****************************************************************************\n")

		if (turn2 <= 1):
			Seriph.wield(dict["bow"])
			Seriph.putOnArmor(dict["leather"])

		if (player1.health <= 12):
			Seriph.wield(dict["katana"])
			Seriph.fight(player1)
		elif (player1.health <= 10):
			Seriph.wield(dict["bow"])
			Seriph.fight(player1)
		elif (player1.health <= 8):
			Seriph.wield(dict["daggers"])
			Seriph.fight(player1)
		elif (player1.health <= 7):
			Seriph.wield(dict["katana"])
			Seriph.fight(player1)
		else:
			Seriph.fight(player1)

		turn2 += 1

		player1.checkForDefeat()

		if (Seriph.health <= 0):
			print("Seriph has been defeated!\n")
			print("****************************************************************************\n")
			return

		player1.show()
		Seriph.show()

		print("****************************************************************************\n")

def battleHogar(player1, Hogar, dict, player1class, player1name, player2name):

	turn1 = 1
	turn2 = 1

	bash1 = 1
	bashHogar = 1

	print("Beginning battle against Hogar the Fearsome\n")

	while True:
		print("Player 1's turn: \n")
		print("Enter a command followed by a comma and space, then a target for the command")
		print("If the command is an attack or spell, the target is a character")
		print("If the command is to EQP the target is the desired weapon or armor. If it is to unequip, the target is 'none'")
		print("**ALL TARGETS IN LOWERCASE UNLESS CHARACTER NAME**")
		print("Commands:")
		print("ATK for attack")
		print("EQP for equip")
		print("CAST for casting a spell")
		print("UNEQ for unequpping any weapon and using bare hands")
		print("BASH for fighter ability: 1.5x dmg but take weapon's damage")
		print("POA for putting on armor")
		print("TOA for taking off armor\n")

		print("\n****************************************************************************\n")

		# loop for player to equip and then attack or cast
		didBash = turn(player1, player1class, player1name, turn1, bash1, dict, Hogar, player2name)
		if (didBash == 1):
			bash1 = 0

		turn1 += 1
		if (bash1 < 3):
			bash1 += 1

		player1.checkForDefeat()

		if (Hogar.health <= 0):
			print("Hogar has been defeated!\n")
			print("****************************************************************************\n")
			return

		print("****************************************************************************\n")

		# Hogar's turn
		if (turn2 <= 1):
			if player1class == "fighter":
				Hogar.wield(dict["greatsword"])
				Hogar.putOnArmor(dict["leather"])
			elif player1class == "thief":
				Hogar.wield(dict["sword"])
				Hogar.putOnArmor(dict["plate"])
			else:
				Hogar.wield(dict["axe"])
				Hogar.putOnArmor(dict["leather"])

		if (bashHogar == 3):
			if player1.health <= 14:
				Hogar.wield(dict["greatsword"])
				Hogar.bash(player1)
			elif player1.health <= 11:
				Hogar.wield(dict["axe"])
				Hogar.bash(player1)
		else:
			if player1.health <= 9:
				Hogar.wield(dict["greatsword"])
				Hogar.fight(player1)
			elif player1.health <= 7:
				Hogar.wield(dict["axe"])
				Hogar.fight(player1)
			else:
				Hogar.fight(player1)

		turn2 += 1
		if (bashHogar < 3):
			bashHogar += 1

		player1.checkForDefeat()

		if (Hogar.health <= 0):
			print("Hogar has been defeated!\n")
			print("****************************************************************************\n")
			return

		player1.show()
		Hogar.show()

		print("****************************************************************************\n")



# method to let players use potions
def usePotions(player1, player1class):
	if (player1.healthpotions == 0 and player1.sppotions == 0):
		print("You have no more potions to use.")
		return
	elif (player1.healthpotions == 0):
		print("You have no more health potions to use.")
	else:
		print("You have", player1.healthpotions, "health potions remaining.")
		useHealth = int(input("Use a health potion (1) or don't (2)? "))
		while (useHealth != 1 and useHealth != 2):
			useHealth = int(input("Please enter either 1 or 2: "))
		if (useHealth == 1):
			if isinstance(player1, Fighter):
				if (player1.health < 15):
					player1.health += 25
				else:
					player1.health = 40
			if isinstance(player1, Wizard):
				if (player1.health < 10):
					player1.health += 25
				else:
					player1.health = 35
			if isinstance(player1, Thief):
				if (player1.health < 5):
					player1.health += 25
				else:
					player1.health = 30
			print("Health Poiton used, current health is", player1.health, "\n")
		if (player1.sppotions != 0):
			print("You have", player1.sppotions, "sp potions remaining.")
			useSp = int(input("Use an sp potion (1) or don't (2)? "))
			while (useSp != 1 and useSp != 2):
				useSp = int(input("Please enter either 1 or 2: "))
			if (useSp == 1):
				player1.spellpoints = 20
				print("SP Poiton used, current SP is", player1.spellpoints, "\n")

	player1.show()

# method for each player to take their turn
def turn(player1, player1class, player1name, turn1, bash1, dict, player2, player2name):
	action = 0
	if (turn1 % player1.armor.speed == 0):
		print("\n***", player1.name, "is exhausted. Turn skipped. ***\n")
		return 0
	while (action == 0 and turn1 >= 1):
		try:
			player1action, player1target = input("Perform an action: ").split(', ')
		except ValueError:
			print("Please enter a command and a target as specified")
			player1action, player1target = input("Perform an action: ").split(', ')
		if (player1action == "-1"):
			sys.exit()
		if (player1action == "EQP"):
			player1.wield(dict[player1target])
		elif (player1action == "UNEQ"):
			player1.unwield()
		elif (player1action == "POA"):
			player1.putOnArmor(dict[player1target])
		elif (player1action == "TOA"):
			player1.takeOffArmor()
		elif (player1target != player1name and player1target != player2name):
			print("Please enter a valid target for your action")
		elif (player1action == "BASH"):
			if(isinstance(player1, Fighter) and bash1 == 3):
				player1.bash(dict[player1target])
				action += 1
				return 1
			else:
				print("Ability not available")
		elif (player1action == "CAST" and player1class == "wizard"):
			spell = input("Enter spell would you like to cast on " + player1target + ": " )
			spell = spell.lower()
			spellStatus = player1.castSpell(spell, dict[player1target])
			if (spellStatus == -1):
				continue
			else:
				action += 1
		elif (player1action == "ATK"):
			player1.fight(dict[player1target])
			action += 1
		else:
			print("Invalid Command; Try again\n")
	return 0


def main(): 

	# initialize weapons
	sword = Weapon("sword")
	greatsword = Weapon("greatsword")
	axe = Weapon("axe")
	daggers = Weapon("daggers")
	bow = Weapon("bow")
	katana = Weapon("katana")
	staff = Weapon("staff")
	noneWpn = Weapon("none")

	# initialize armor
	plate = Armor("plate")
	chain = Armor("chain")
	leather = Armor("leather")
	robes = Armor("robes")
	noneArm = Weapon("none")

	# initialize potions
	healthPotion = Potion("health potion")
	spPotion = Potion("sp potion")

	# create dict for all items
	dict = {}
	dict ["sword"] = sword
	dict ["greatsword"] = greatsword
	dict ["axe"] = axe
	dict ["daggers"] = daggers
	dict ["bow"] = bow
	dict ["katana"] = katana
	dict ["staff"] = staff
	dict ["plate"] = plate
	dict ["chain"] = chain
	dict ["leather"] = leather
	dict ["robes"] = robes
	dict ["health potion"] = healthPotion
	dict ["sp potion"] = spPotion

	gameType = 0
	while (gameType != 1 and gameType != 2):
		gameType = int(input("\nSingle Player (1) or Multiplayer (2)? "))

	# display available weapons and spells
	print()
	print("####################################################################################\n")
	print("Welcome To My RPG\n")
	print("		    ^          ( \     / )          --				")
	print("		   / \        (   \ - /   )         |  )			")
	print("		   | |        (   / - \   )         |   )			")
	print("		   | |         ( / | | \ )          |    )			")
	print("		   | |             | |            }-|-----)--> 		")
	print("		 \ | | /           | |              |    )  		")
	print("		  \ - /            | |              |   )   		")
	print("		   | |             | |              |  )			")
	print("		   ---             ---              --			  \n")
	print("Classes:")
	print("Figher: Health - 40, Spell Points - 0, Ability - 1.5x damage but take weapon's damage")
	print("Thief: Health - 30, Spell Points - 0, Ability - Chance to dodge an attack each turn")
	print("Wizard: Health - 35, Spell Points - 20, Ability - Spellcaster\n")
	print("Class     Weapon/Spell     Damage    Crit Chance    Spell Effect    Cost")
	print("-------------------------------------------------------------------------")       
	print("Fighter     Sword            6          30%              -           -")
	print("Fighter     Greatsword       9          10%              -           -")
	print("Fighter     Axe              7          23%              -           -")
	print("Thief       Daggers          4          70%              -           -")
	print("Thief       Bow              5          55%              -           -")
	print("Thief       Katana           6          40%              -           -")
	print("Wizard      Staff            3           5%              -           -")
	print("Wizard      Fireball         5           -               -           3")
	print("Wizard      Lightning Bolt   7           -               -           5")
	print("Wizard      Blizzard        10           -               -          10")
	print("Wizard      Heal             -           -              10           5")
	print("Wizard      Restore SP       -           -              15           0\n")

	print("\nArmor rating is percent chance of getting hit (i.e. lower is better)")
	print("Armor speed is how many turns before you have to skip a turn\n")

	print("Armor          Classes       Armor Rating        Speed")
	print("-------------------------------------------------------")
	print("Plate            F                7.5              3")
	print("Chain           F, T               8               4")
	print("Leather         F, T              8.5              6")
	print("Robes            W                 9               8")
	print("None           F, T, W            10              10\n")

	print("Rules:")
	print("- Each player may equip or unequip a weapon during their turn")
	print("- They may also attack during their turn or cast a spell")
	print("- Once a player has attacked or cast a spell, their turn is over")
	print("- The speed of an armor piece determines how often you must skip a turn")
	print("- When a player reaches zero health, they have been defeated and the other player wins\n")
	print("####################################################################################\n")

	if gameType == 2:

		# create two players
		flag = 0
		while(flag == 0):
			print("Player 1:")
			player1class = input("Enter your class: ")		
			player1class = player1class.lower()
			player1name = input("Enter your name: ")
			if (player1class == "fighter"):
				player1 = Fighter(player1name)
				flag += 1
			elif (player1class == "thief"):
				player1 = Thief(player1name)
				flag += 1
			elif (player1class == "wizard"):
				player1 = Wizard(player1name)
				flag += 1
			else:
				print("Invalid Class; Try Again")

		dict[player1name] = player1
		player1.show()

		print()
		flag = 0
		while (flag == 0):
			print("Player 2:")
			player2class = input("Enter your class: ")		
			player2class = player2class.lower()
			player2name = input("Enter your name: ")
			if (player2class == "fighter"):
				player2 = Fighter(player2name)
				flag += 1
			elif (player2class == "thief"):
				player2 = Thief(player2name)
				flag += 1
			elif (player2class == "wizard"):
				player2 = Wizard(player2name)
				flag += 1
			else:
				print("Invalid Class; Try Again")

		dict[player2name] = player2
		player2.show()

		turn1 = 1
		turn2 = 1

		bash1 = 1
		bash2 = 1

		# loop for player's to take their turns
		while (True):
			print("Player 1's turn: \n")
			print("Enter a command followed by a comma and space, then a target for the command")
			print("If the command is an attack or spell, the target is a character")
			print("If the command is to EQP the target is the desired weapon or armor. If it is to unequip, the target is 'none'")
			print("**ALL TARGETS IN LOWERCASE UNLESS CHARACTER NAME**")
			print("Commands:")
			print("ATK for attack")
			print("EQP for equip")
			print("CAST for casting a spell")
			print("UNEQ for unequpping any weapon and using bare hands")
			print("BASH for fighter ability: 1.5x dmg but take weapon's damage")
			print("POA for putting on armor")
			print("TOA for taking off armor\n")

			print("\n****************************************************************************\n")

			# loop for player to equip and then attack or cast
			didBash = turn(player1, player1class, player1name, turn1, bash1, dict, player2, player2name)
			if (didBash == 1):
				bash1 = 0

			turn1 += 1
			if (bash1 < 3):
				bash1 += 1

			player1.checkForDefeat()
			player2.checkForDefeat()

			player1.show()
			player2.show()
			

			print("****************************************************************************\n")

			print("Player 2's turn: \n")
			print("Enter a command followed by a comma and then a target for the command")
			print("If the command is an attack or spell, the target is a character")
			print("If the command is to EQP the target is the desired weapon. If it is to unequip, the target is 'none'")
			print("If the command is an ability, target is the desired ability")
			print("Commands:")
			print("ATK for attack")
			print("EQP for equip")
			print("CAST for casting a spell")
			print("UNEQ for unequpping any weapon and using bare hands")
			print("BASH for fighter ability: 1.5x dmg but take weapon's damage")
			print("POA for putting on armor")
			print("TOA for taking off armor\n")

			print("\n****************************************************************************\n")

			# loop for player to equip and then attack or cast
			didBash = turn(player2, player2class, player2name, turn2, bash2, dict, player1, player1name)
			if (didBash == 1):
				bash2 = 0

			turn2 += 1
			if (bash2 < 3):
				bash2 += 1

			player1.checkForDefeat()
			player2.checkForDefeat()

			player1.show()
			player2.show()

			print("****************************************************************************\n")

	elif gameType == 1:

		print("The Tournament:")
		print("You will face 5 opponents in a row. You will have 3 health potions that") 
		print("restore 25 health each and if you are a wizard, 2 sp potions that retsore 20 sp each.")
		print("You may use these in between battles so use them wisely.")
		print("Good Luck. . .")
		print("####################################################################################\n")


		flag = 0
		while(flag == 0):
			print("Player 1:")
			player1class = input("Enter your class: ")		
			player1class = player1class.lower()
			player1name = input("Enter your name: ")
			if (player1class == "fighter"):
				player1 = Fighter(player1name)
				flag += 1
			elif (player1class == "thief"):
				player1 = Thief(player1name)
				flag += 1
			elif (player1class == "wizard"):
				player1 = Wizard(player1name)
				flag += 1
			else:
				print("Invalid Class; Try Again")

		# initialize player potions
		player1.healthpotions = 3
		if (player1class == "wizard"):
			player1.sppotions = 2
		else:
			player1.sppotions = 0

		dict[player1name] = player1
		player1.show()

		#-----------------------------------------------------------------------------

		# initilaize first opponent
		Grale = Fighter("Grale")
		player2name = "Grale"
		Grale.health = 30
		Grale.show()

		dict["Grale"] = Grale

		# fight first opponent
		battleGrale(player1, Grale, dict, player1class, player1name, player2name)

		player1.show()

		# give player the option to use potions
		usePotions(player1, player1class)

		#-----------------------------------------------------------------------------

		# initialize second opponent
		Seriph = Thief("Seriph")
		player2name = "Seriph"
		Seriph.show()

		dict["Seriph"] = Seriph

		# fight second opponent
		battleSeriph(player1, Seriph, dict, player1class, player1name, player2name)

		player1.show()

		# give player the option to use potions
		usePotions(player1, player1class)

		#-----------------------------------------------------------------------------

		# initialize third opponent
		Hogar = Fighter("Hogar")
		player2name = "Hogar"
		Hogar.show()

		dict["Hogar"] = Hogar

		# fight second opponent
		battleHogar(player1, Hogar, dict, player1class, player1name, player2name)

		player1.show()

		# give player the option to use potions
		usePotions(player1, player1class)
main()




















