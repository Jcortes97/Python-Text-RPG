"""
Author: Jaycee Cortes
Date: November 28, 2017
Description: Text based adventure gamethat requires you, the player, to traverse across the
grid to save a princess. Across this journey, you will meet randomly generated enemies
that will attempt to end your journey as well as find items that will help you.
"""



#imports random and json modules
import random
import json


class Character:
  def __init__(self): #Creates a baseline for newly created characters
    self.name = ""
    self.health = 1
    self.health_max = 1
    self.damage = 1
    self.intellect = 1
    self.dexterity = 1
    self.level = 0
  def battledamage(self, enemy): #Calculates damage given and taken during battle
    damage = min(max(random.randint(0, self.damage) - random.randint(0, enemy.health), 0), enemy.health)
    enemy.health = (enemy.health - damage)
    if damage == 0:
      print (("%s evades %s's attack.") % (enemy.name, self.name))
    else: print (("%s did %d damage to %s!") % (self.name, damage, enemy.name))
    return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player): #Creates a profile for enemies, Encounters are randomly generated
    Character.__init__(self)
    self.enemies = ['bandit', 'bear', 'demon', 'ghost', 'gnoll', 'harpy', 'mercenary', 'minotaur', 'scavenger', 'treant', 'wolf', 'zombie']
    self.name = (('a %s') % (random.choice(self.enemies)))
    self.health = random.randint(1, 15)
    self.damage = random.randint(1, player.damage) + 5
    self.dexterity = random.randint(1, player.dexterity) + 5

class Player(Character):
  def __init__(self): #Creates a new baseline for characters who haven't picked a class, starts the character off at a certain column and row
    Character.__init__(self)
    self.state = 'normal'
    self.rpclass = 'none'
    self.health = 10
    self.health_max = 10
    self.damage = 10
    self.intellect = 10
    self.dexterity = 10
    self.level = 1
    self.locCol = 2
    self.locRow = 11
  def search(self): #Allows the user to search a cell in a grid for an enemy or treasure indefinitely, it allows the user to "grind" (continuously kill monsters over and over again in order to get stronger)
    if self.state != 'normal': #won't let player search if they are in a battle
      print('You can\'t search in the middle of a fight, nerd.')
    else:
      print ("You head deeper into the forest while shouting for the princess to hear you")
      if random.randint(0, 1): #randomly lets players encounter a monster
        self.enemy = Enemy(self)
        print (("You encountered %s!") % (self.enemy.name))
        self.state = 'fight'
      else:
        if random.randint(0, 1): #randomly lets player become 'tired' (weaker) as they move to provide a more immersive experience
          self.tired()
  def left(self): #Moves characters towards the left on the grid
    if self.state != 'normal':
      print(('%s can\'t do that in the middle of a fight, nerd.') % (self.name))
    else:
      self.locCol = self.locCol - 1
      self.foundInCell = grid[self.locRow][self.locCol]
      print('Now at row:', self.locRow, '   col:', self.locCol, '    cell contains:', self.foundInCell)
      if random.randint(0, 1): #random encounter while moving
        self.enemy = Enemy(self)
        print (("%s ambushes you!") % (self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
  def right(self): #Moves characters towards the right on the grid
    if self.state != 'normal':
      print(('%s can\'t do that in the middle of a fight, nerd.') % (self.name))
    else:
      self.locCol = self.locCol + 1
      self.foundInCell = grid[self.locRow][self.locCol]
      print('Now at row:', self.locRow, '   col:', self.locCol, '    cell contains:', self.foundInCell)
      if random.randint(0, 1): #random encounter while moving
        self.enemy = Enemy(self)
        print (("%s ambushes you!") % (self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
  def up(self): #Moves characters upwards on the grid
    if self.state != 'normal':
      print(('%s can\'t do that in the middle of a fight, nerd.') % (self.name))
    else:
      self.locRow = self.locRow - 1
      self.foundInCell = grid[self.locRow][self.locCol]
      print('Now at row:', self.locRow, '   col:',self. locCol, '    cell contains:', self.foundInCell)
      if random.randint(0, 1): #random encounter while moving
        self.enemy = Enemy(self)
        print (("%s ambushes you!") % (self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
  def down(self): #Moves characters downwards the left on the grid
    if self.state != 'normal':
      print(('%s can\'t do that in the middle of a fight, nerd.') % (self.name))
    else:
      self.locRow = self.locRow + 1
      self.foundInCell = grid[self.locRow][self.locCol]
      print('Now at row:', self.locRow, '   col:', self.locCol, '    cell contains:', self.foundInCell)
      if random.randint(0, 1): #random encounter while moving
        self.enemy = Enemy(self)
        print (("%s ambushes you!") % (self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
  def RPGClasses(self): #Shows available classes to players and provides a brief description for said classes
      classesRPG = {
          'Cleric': {
              'Health': 'Medium',
              'Damage': 'Low',
              'Intellect': 'High',
              'Dexterity': 'Low',
              'Description' : 'Clerics are wielders of the light- they have low damage, but a high chance to level up.',
              },
          'Mage': {
              'Health': 'Low',
              'Damage': 'Very High',
              'Intellect' : 'Very High',
              'Dexterity' : 'Low',
              'Description': 'Mages are frail and practice mystical arts to quickly burst down enemies.',
              },
          'Rogue': {
              'Health': 'Low',
              'Damage': 'Medium',
              'Intellect': 'Medium',
              'Dexterity': 'Very High',
              'Description': 'Rogues are swift and rely on agility to dodge attacks and run away from enemies.',
              },
          'Warrior': {
              'Health': 'Very High',
              'Damage': 'High',
              'Intellect': 'Very Low',
              'Dexterity': 'Very Low',
              'Description': 'Warriors are sturdy and are highly trained in close combat.'
              }
          }
      while (direction == 'RPGClasses'):
          for name, stats in classesRPG.items():
              print("Class: ", name)
              print("Health: ", stats['Health'], "\n", "Damage:", stats['Damage'], "\n", "Intellect: ", stats['Intellect'], "\n",
                    "Dexterity: ", stats['Dexterity'], "\n", stats['Description'], "\n")

          print("Enter a class that interests you the most. Choose wisely! ")
          break        
  def Cleric(self): #Lets players be a cleric and have their stats adjusted accordingly if they have not picked a class prior to this
      if self.rpclass == 'none':
          self.health += 20
          self.health_max += 20
          self.damage += 0
          self.intellect += 10
          self.dexterity += 0
          self.rpclass = 'cleric'
          print('You are a wielder of the light')
      else: #doesn't allow players to change classes if they have picked one before
          print('You already have an occupation!')
  def Mage(self): #Lets players be a mage and have their stats adjusted accordingly if they have not picked a class prior to this
      if self.rpclass == 'none':
          self.health += 10
          self.health_max += 10
          self.damage += 20
          self.intellect += 20
          self.dexterity += 0
          self.rpclass = 'mage'
          print('You are a practitioner of the mystical arts.')
      else: #doesn't allow players to change classes if they have picked one before
          print('You already have an occupation!')
  def Rogue(self): #Lets players be a rogue and have their stats adjusted accordingly if they have not picked a class prior to this
      if self.rpclass == 'none':
          self.health += 10
          self.health_max += 10
          self.damage += 5
          self.intellect += 5
          self.dexterity += 20
          self.rpclass = 'rogue'
          print('You are a savage thief.')
      else:
          print('You already have an occupation!')
  def Warrior(self): #Lets players be a warrior and have their stats adjusted accordingly if they have not picked a class prior to this
      if self.rpclass == 'none':
          self.health += 50
          self.health_max += 50
          self.damage += 10
          self.intellect -= 5
          self.dexterity -= 5
          self.rpclass = 'warrior'
          print('You are a proud warrior.')
      else: #doesn't allow players to change classes if they have picked one before
          print('You already have an occupation!')
  def exit(self): #Allows players to exit the game whenever they want
    print ("You were driven to madness due to not finding the princess.\nYOU DIED.")
    self.health = 0
    #documents that the player has not finished the game in the save file
    with open(filename, 'a') as file_object:
        file_object.write("\nDid not finish.")
    file_object.close()
  def help(self): #Shows players a list of available commands
    for o in Assist:
        print(o)
  def combat(self): #tells players how to fight
    fighting = {
        'Battle Commands': {
            'What does flee do?': 'Flee allows you to run away from encounters',
            'What does attack do?': 'While in battle, it lets you damage an enemy.',
            }
        }
    while (direction == 'combat'):
        for com, bat in fighting.items():
            print('The', com)
            print("What does flee do?", bat['What does flee do?'], "\n\n", "What does attack do? ", bat['What does attack do?'], "\n")

        print('Hope that helped. Now get back in there!')
        break
  def general(self): #tells players all the general commands for the game (i.e. exiting the game, moving around)
      basics = {
          'Basics': {
              'What does exit do?': 'Exit allows you to exit the game',
              'What does help do?': 'Help shows all available options',
              'What does search do?': 'Search allows players to search for monsters in a spot indefinitely',
              'What does status do?': 'Status displays your current level and health and class',
              'What does rest do?': 'Rest allows you to restore some health out of combat',
              'What does left do?': 'Left allows you to move left on the map',
              'What does right do?': 'Right allows you to move right on the map',
              'What does up do?': 'Up allows you to move upward on the map',
              'What does down do?': 'Down allows you to go downward on the map',
              }
          }
      while (direction == 'general'): #while loop that prints the dictionary 'neatly'
          for gen, eral in basics.items():
              print('The', gen)
              print('What does exit do?', eral['What does exit do?'], "\n\n", 'What does help do?', eral['What does help do?'], "\n\n",'What does search do?', eral['What does search do?'], "\n\n",
                    'What does search do?', eral['What does search do?'], "\n\n", 'What does status do?', eral['What does status do?'], "\n\n", 'What does rest do?', eral['What does rest do?'], "\n\n",
                    'What does left do?', eral['What does left do?'], "\n\n", 'What does right do?', eral['What does right do?'], "\n\n", 'What does up do?', eral['What does down do?'], "\n\n",)

          print('Hope that helped. Now get back in there!')
          break
  def LootAndInventory(self): #explains the inventory system and what to do with items
      InventorySystem = {
          'Loot and Inventory System': {
              'What does Inventory do?': 'Inventory allows you to see every item you\'ve picked up so far.',
              'What does Loot do?': 'Loot allows you to look for treasure in the area when prompted to',
              'What does EquipRobes do?': 'Allows you to equip Robes if you have found them',
              'What does EquipLeatherBreastplate do?': 'Allows you to equip Leather Breastplates if you have found them',
              'What does EquipSteelPauldrons do?': 'Allows you to equip Steel Pauldrons if you have found them',
              'What does EquipSteelBoots do?': 'Allows you to equip Steel Boots if you have found them',
              'What does EquipSteelGauntlets do?': 'Allows you to equip Steel Gauntlets if you have found them',
              'What does UseHealthPotion do?': 'Allows you to restore health if you have found a health potion',
              }
          }
      while (direction == 'LootAndInventory'): #while loop that prints the dictionary 'neatly'
          for inv, sys in InventorySystem.items():
              print('The', inv)
              print('What does Inventory do?', sys['What does Inventory do?'], "\n\n", 'What does Loot do?', sys['What does Loot do?'], "\n\n", 'What does EquipRobes do?', sys['What does EquipRobes do?'], "\n\n",
                    'What does EquipLeatherBreastplate do?', sys['What does EquipLeatherBreastplate do?'], "\n\n", 'What does EquipSteelPauldrons do?', sys['What does EquipSteelPauldrons do?'], "\n\n",
                    'What does EquipSteelBoots do?', sys['What does EquipSteelBoots do?'], "\n\n", 'What does EquipSteelGauntlets do?', sys['What does EquipSteelGauntlets do?'], "\n\n",
                    'What does UseHealthPotion do?', sys['What does UseHealthPotion do?'], "\n\n",)

          print('Hope that helped. Now get back in there!')
          break
  def status(self): #Shows players how much health they have and what level they are
      print (("level: %d\nhealth: %d/%d\nclass: %s") % (self.level, self.health, self.health_max, self.rpclass))  
  def Loot(self): #shows items and appends them into the inventory when found
    if self.state != 'normal':
      print('No time now, do it after the fight!')
    else:
      self.MyInventory = []
      self.TreasureNames = ['LeatherBreastplate', 'SteelPauldrons', 'Robes', 'SteelGauntlets', 'SteelBoots', 'HealthPotion']
      self.TreasureLoot = random.choice(self.TreasureNames)
      self.MyInventory.append(self.TreasureLoot)
      print(('You found %s!') % (self.TreasureLoot))
  def Inventory(self): #Shows the player what is available in their inventory
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          print(self.MyInventory)
  def EquipRobes(self): #Allows players to equip Robes and have their stats adjusted accordingly, won't allow players to equip items during battle
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          self.health_max += 3
          self.intellect += 10
          self.MyInventory.remove('Robes')
  def EquipLeatherBreastplate(self): #Allows players to equip a Leather Breastplate and have their stats adjusted accordingly, won't allow players to equip items during battle
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          self.health_max += 5
          self.dexterity += 10
          self.MyInventory.remove('LeatherBreastplate')
  def EquipSteelPauldrons(self): #Allows players to equip Steel Pauldrons and have their stats adjusted accordingly, won't allow players to equip items during battle
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          self.health_max += 7
          self.dexterity -= 5
  def EquipSteelGauntlets(self): #Allows players to equip Steel Gauntlets and have their stats adjusted accordingly, won't allow players to equip items during battle
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          self.health_max += 5
          self.dexterity -= 3
          self.MyInventory.remove('SteelGauntlets')
  def EquipSteelBoots(self): #Allows players to equip Steel Boots and have their stats adjusted accordingly, won't allow players to equip items during battle
      if self.state != 'normal':
          print('You can\'t do that now.')
      else:
          self.health_max += 6
          self.dexterity -= 4
          self.MyInventory.remove('SteelBoots')
  def UseHealthPotion(self): #Allows players to use a Health Potion to restore health
      self.health += 10
      self.MyInventory.remove('HealthPotion')
      print('Health is restored')
  def tired(self): #Players' well-being in the game deteriorates over time to provide a more immersive experience
    print ("You feel weary...")
    self.health = max(1, self.health - 1)
  def rest(self): #Allows players to rest to restore health as well as encounter surprise attacks from enemies while asleep while also allowing the player to oversleep for a immersive experience
    if self.state != 'normal':
      print('You can\' rest in the middle of a battle, nerd.')
    else:
      print ("You fell asleep.")
      if random.randint(0, 1):
        self.enemy = Enemy(self)
        print (("%s attacks you in your sleep!") % (self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health += random.randint(1, self.health_max)
          print('You feel well rested! Better get going.')
        else: print ("You overslept and now feel even worse..")
        self.health -= 1
  def flee(self): #Allows the player to run from fights
    if self.state != 'fight': #makes the player tired if they 'flee' during a normal state
      print(("%s runs from... nothing???") % (self.name))
      self.tired()
    else:
      if random.randint(1, self.dexterity + 5) > random.randint(1, self.enemy.dexterity):
        print (("You ran away from %s.") % (self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else:
        print (("You were too slow to escape from %s!") % (self.enemy.name))
        self.enemy_attacks()  
  def attack(self): #Allows players to attack and level up to increase stats
    if self.state != 'fight':
      print ("You attack nothing...? You uh... wanna save your energy for attacking enemies that are... uh... y'know... around?")
      self.tired()
    else:
      if self.battledamage(self.enemy):
        print (("%s has been slain!") % (self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if random.randint(0, self.intellect) < 4:
          self.health += random.randint(1, 5)
          self.health_max += random.randint(1, 5)
          self.damage += random.randint(0, 5)
          self.intellect += random.randint(0, 5)
          self.dexterity += random.randint(0, 5)
          self.level += 1
          print ("You leveled up!")
      else: self.enemy_attacks()
  def enemy_attacks(self): #ends the game when an enemy kills the player
    if self.enemy.battledamage(self):
      print(("You were killed by %s!\nYOU DIED.") %(self.enemy.name))
      #documents that the player has died to an enemy in the save file
      with open(filename, 'a') as file_object:
        file_object.write("\nDied to an enemy.")
      file_object.close()
  def Talk(self): #End of the game prompt when the player has reached the 'END' of the game, upon reaching the end of the game, there will be 3 alternative "endings"
      self.NPC = input('Oh, dearest me. I miss my family. Oh kind sir or ma\'am, I don\'t mean to assume in 476 AD, but would you please help me? Yes/No ')
      if self.NPC == 'Yes':
          print('Oh, thank you! Thank you!')
          print('You and the princess return swiftly to her kingdom. The king grants his daughter\'s hand in marriage and the two of you live happily ever after.')
          with open(filename, 'a') as file_object:
              file_object.write("\nGot a happy ending. ;)")
          file_object.close()
          self.health = 0 #all of the options 'kill' the player so to speak in order to end the game
      else:
          self.twoNPC = input('Wh-what? What the hell do you mean \'No\'?!? Do you not realize who I am? I can have you killed! (what do you do? Kill/Leave) ')
          if self.twoNPC == 'Kill':
              print('Wh-why...')
              print('After dispatching the princess, you quickly bury her body and leave the forest. The overwhelming guilt of murdering the princess drives you mad.')
              with open(filename, 'a') as file_object:
                  file_object.write("\nGot bad ending 1.")
              file_object.close()
              self.health = 0 #all of the options 'kill' the player so to speak in order to end the game
          else:
              print('Hmmph, fine!')
              print('After leaving the princess, you quickly leave the forest. Several years later, you stumble upon the very same forest you entered long ago. You find scattered remains of a young girl with tally marks carved on a tree nearby. Seems the poor girl never got back home.')
              with open(filename, 'a') as file_object:
                  file_object.write("\nGot bad ending 2.")
              file_object.close()
              self.health = 0 #all of the options 'kill' the player so to speak in order to end the game
  def Descriptions(self): #Explains the functions of each command
      WhatDo = {
          'Commands': {
              'What does exit do?': 'Exit allows you to exit the game',
              'What does help do?': 'Help shows all available options',
              'What does status do?': 'Status displays your current level and health and class',
              'What does rest do?': 'Rest allows you to restore some health out of combat',
              'What does flee do?': 'Flee allows you to run away from encounters',
              'What does Inventory do?': 'Inventory allows you to see every item you\'ve picked up so far.',
              'What does Loot do?': 'Loot allows you to look for treasure in the area when prompted to',
              'What does attack do?': 'While in battle, it lets you damage an enemy.',
              'What does left do?': 'Left allows you to move left on the map',
              'What does right do?': 'Right allows you to move right on the map',
              'What does up do?': 'Up allows you to move upward on the map',
              'What does down do?': 'Down allows you to go downward on the map',
              'What does EquipRobes do?': 'Allows you to equip Robes if you have found them',
              'What does EquipLeatherBreastplate do?': 'Allows you to equip Leather Breastplates if you have found them',
              'What does EquipSteelPauldrons do?': 'Allows you to equip Steel Pauldrons if you have found them',
              'What does EquipSteelBoots do?': 'Allows you to equip Steel Boots if you have found them',
              'What does Talk do?': 'Talk allows you to chat with NPC\'s when prompted to.',
              }
          }
      while (direction == 'Descriptions'): #while loop that prints the dictionary 'neatly'
          for opt, func in WhatDo.items():
              print("The", opt)
              print("What does exit do?", func['What does exit do?'], "\n\n", "What does help do? ", func['What does help do?'], "\n\n",
                    "What does status do? ", func['What does status do?'], "\n\n", "What does rest do? ", func['What does rest do?'], "\n\n",
                    "What does flee do?", func['What does flee do?'], "\n\n", "What does Inventory do?", func['What does Inventory do?'],
                    "\n\n", "What does Loot do?", func['What does Loot do?'], "\n\n", "What does attack do?", func['What does attack do?'], "\n\n",
                    "What does left do?", func['What does left do?'], "\n\n", "What does right do?", func['What does right do?'], "\n\n",
                    "What does up do?", func['What does up do?'], "\n\n", "What does down do?", func['What does down do?'], "\n\n",
                    "What does EquipRobes do?", func['What does EquipRobes do?'], "\n\n",
                    "What does EquipLeatherBreastplate do?", func['What does EquipLeatherBreastplate do?'], "\n\n", "What does EquipSteelPauldrons do?",
                    func['What does EquipSteelPauldrons do?'], "\n\n", "What does EquipSteelBoots do?", func['What does EquipSteelBoots do?'], "\n\n",
                    "What does Talk do?", func['What does Talk do?'], "\n")

          print("Hope that helped")
          break

#defines filename
filename = 'RPGGameSave.json'

try:
    with open('RPGGameSave.json', 'r') as file_object: #reads the file 'RPGGameSave.json'
        save = file_object.read() #save is set to the file being read
        print(save) #prints file information
except FileNotFoundError: #instead of printing an error, a new file is created
    print("User doesn't exist on system") #message printed instead of error
    username = input("Enter your username: ") #allows new user to insert new username
    scoreboard = ("***Previous Adventurers*** \n")#prints header for save file
    with open('RPGGameSave.json', 'w') as file_object: #adds header and username
        file_object.write(scoreboard) #adds scoreboard to .json file
        json.dump(username, file_object) #adds username to .json file
        print("saving info for next time")

else:
    username = input("Enter your username: ") #lets new users insert their info
    with open('RPGGameSave.json', 'a') as file_object: #adds new information
        file_object.write("\n\"%s\"" % (username))
        print("saving info for next time")

#sets p to class player
p = Player()
p.name = input("Enter your character's name:  ") #allows user to insert a name for their character
print ("Type \'help\' to learn more about how to play the game.\n") #lets user know how to get access to all commands
print (("%s stumbles upon a forest looking for a lost princess.") % (p.name)) 
print ("To get started, type \'RPGClasses\' to see the list of all available classes.") #lets user know which classes are available and how to access them

#strings on the grid that prompt what the player should do    
DIALOGUE = "HEY! LISTEN! You are on the edge of the map. Be careful."           
SPECIAL = "You hear faint crying in the distance- better check it out."
EMPTY = "Nothing here... better move on."
TREASURE = 'You find a suspicious spot on the ground... might be worth digging up. Type \'Loot\' to look look around for loot.'
ENCOUNTER = 'Area seems too quiet... I should look around just in case, rest up or prepare myself for the next encounter. \nType \'search\' to look around, \'rest\' to restore health, \'inventory\' to view my current stash.\n Or move on by typing \'up\', \'left\', \'down\', \'right\'.'
END = 'You\'ve found the princess you were looking for! (Type \'Talk\' to initiate a conversation with the princesss'

#displays number of rows and columns in the grid
NROWS_IN_GRID = 13 
NCOLS_IN_GRID = 6 
grid = [\
          [DIALOGUE,  DIALOGUE,   DIALOGUE,   DIALOGUE,   DIALOGUE,   DIALOGUE],\
          [DIALOGUE,  TREASURE,   ENCOUNTER,  SPECIAL,    TREASURE,   DIALOGUE],\
          [DIALOGUE,  TREASURE,   SPECIAL,    END,        SPECIAL,    DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  SPECIAL,    ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  TREASURE,   ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  TREASURE,   ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  TREASURE,   EMPTY,      ENCOUNTER,  ENCOUNTER,  DIALOGUE],\
          [DIALOGUE,  DIALOGUE,   DIALOGUE,   DIALOGUE,   DIALOGUE,   DIALOGUE],\
          ]
#loop that lets the game start if there is an empty variable in the grid
while True:
    p.locRow =random.randrange(NROWS_IN_GRID)
    p.locCol =random.randrange(NCOLS_IN_GRID)
    if grid[p.locRow][p.locCol] == EMPTY:
        break

Assist = ['type \'combat\' to learn how to fight', 'type \'general\' to learn general commands for the game', 'type \'LootAndInventory\' to learn how the inventory and item system works', 'type \'Descriptions\' for a brief explanation for ALL of the commands.']
#dictionary of options that the player is allowed to use
Options = {
  'exit': Player.exit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'search': Player.search,
  'flee': Player.flee,
  'Inventory': Player.Inventory,
  'Loot': Player.Loot,
  'attack': Player.attack,
  'left': Player.left,
  'right': Player.right,
  'up': Player.up,
  'down': Player.down,
  'RPGClasses': Player.RPGClasses,
  'Cleric': Player.Cleric,
  'Mage': Player.Mage,
  'Rogue': Player.Rogue,
  'Warrior': Player.Warrior,
  'EquipRobes': Player.EquipRobes,
  'EquipLeatherBreastplate': Player.EquipLeatherBreastplate,
  'EquipSteelPauldrons': Player.EquipSteelPauldrons,
  'EquipSteelBoots': Player.EquipSteelBoots,
  'Talk': Player.Talk,
  'Descriptions': Player.Descriptions,
  'combat': Player.combat,
  'general': Player.general,
  'LootAndInventory': Player.LootAndInventory,
  }

#lets user know where they start
print('Starting at  row:', p.locRow, '  col:', p.locCol)

#lets user play game via calling functions through the options dictionary
while(p.health > 0): #if health is more than 0, the game continues
  direction = input("Enter command: ") #allows user to call functions via input
  args = direction.split()
  if len(args) > 0:
    optionFound = False
    for c in Options.keys(): #for loop that searches for the option in the dictionary
      if args[0] == c[:len(args[0])]: #if found, said function will be called
        Options[c](p)
        optionFound = True
        break
    if not optionFound:
      print (("%s is not a valid command") % (direction)) #message displayed if the option typed was not found in the options dictionary






