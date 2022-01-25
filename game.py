import random

'''
Class Definitions for generic monsters and a Player Character
'''
class Creature:
    def __init__(self, name, health, defense, attack):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.name = name

    def fight(self, otherCreature):
        damage = self.attack - otherCreature.defense
        if damage < 0:
            damage = 0
        otherCreature.health = otherCreature.health - damage
        print(self.name + " attacks " + otherCreature.name + " for " + str(damage) + " damage!")

    # Printing out the attributes of our object
    def printStats(self):
        print("========== " + self.name + " ==========")
        print("HEALTH: " + str(self.health))
        print("ATTACK: " + str(self.attack))
        print("DEFENSE: " + str(self.defense))
        print("==========================")

class Hero(Creature):
    def __init__(self, name, health, defense, attack):
        super().__init__(name, health, defense, attack)
        self.weapon = None
        self.potions = 3

    def selectWeapon(self):
        userChoice = int(input("Please select a Weapon: 1) Sword/Shield, 2) Axe | >>"))
        if userChoice == 1:
            self.weapon = "Sword and Shield"
            self.attack += 3
            self.defense += 3
        else:
            self.weapon = "Axe"
            self.attack += 5

        print("You have chosen the " + self.weapon)

    def heal(self):
        if self.potions > 0:
            self.health += 30
            self.potions -= 1
            print("You drank a potion and healed for 10 hit points!")
            print("Your current health is: " + str(self.health))
        else:
            print("You're out of potions!")    
# ============ Setting up new Objects ============

while True:
    # Player Character
    myCharacter = Hero("Hero", 50, 5, 15)

    # CPU Monster
    dragon = Creature("Dragon", 100, 5, 15)
    # Randomly Generated Monster
    monsterList = ["Goblin", "Dragon", "Slime", "Troll", "Spider"]

    # GAME Introduction
    def introduction():
        print("Welcome to Dragon Quest!")
        myCharacter.printStats()
        myCharacter.selectWeapon()
        myCharacter.printStats()

    # Start of the Game
    introduction()
    generatedMonster = Creature(random.choice(monsterList), random.randrange(80, 120, 1), random.randrange(1, 10, 1), random.randrange(5, 20, 1))

    print("A " + generatedMonster.name + " stands before you!")
    # GAME LOOP
    turns = 1
    while myCharacter.health > 0 and generatedMonster.health > 0:
        print("========== TURN: " + str(turns) + "==========")
        userChoice = int(input("Would you like to attack[1] or heal?[2] | >>"))
        if userChoice == 1:
            myCharacter.fight(generatedMonster)
        else:
            myCharacter.heal()

        generatedMonster.fight(myCharacter)

        if myCharacter.health <= 0:
            myCharacter.health = 0
            print("The " + myCharacter.name + " has died! You lose!")

        if generatedMonster.health <= 0:
            generatedMonster.health = 0
            print("The " + generatedMonster.name + " has died! You win!")

        print(myCharacter.name + " has " + str(myCharacter.health) + " health remaining!")
        print(generatedMonster.name + " has " + str(generatedMonster.health) + " health remaining!")

        turns += 1
    # Check if player wants to play again    
    playAgain = int(input("Do you want to play again? Yes[1] or No[2] | >>"))
    if playAgain == 2:
        #Player does not want to play again
        print("Thanks for playing. Hope to see you again")
        break
    else:
        #Player wants to play again
        print("Restarting the game....")