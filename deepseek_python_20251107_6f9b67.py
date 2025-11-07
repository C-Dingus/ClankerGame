"""
Eldoria: The Crystal of Souls
A text-based RPG adventure game
Generated entirely by AI
"""

import random
import time
import sys

class Player:
    """Player class to handle character creation, stats, and inventory"""
    
    def __init__(self):
        self.name = ""
        self.character_class = ""
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.current_area = "Village of Beginnings"
        self.quest_progress = 0
        self.choices_made = []
    
    def create_character(self):
        """Handle character creation process"""
        print("\n=== CHARACTER CREATION ===")
        self.name = input("What is your name, adventurer? ")
        
        print(f"\nWelcome, {self.name}! Choose your path:")
        print("1. Warrior - Master of combat with high Strength")
        print("2. Mage - Weaver of spells with high Magic")
        print("3. Rogue - Shadow walker with high Agility")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice == "1":
                self.character_class = "Warrior"
                self.strength = 15
                self.agility = 8
                self.magic = 5
                self.inventory = ["Iron Sword", "Health Potion"]
                break
            elif choice == "2":
                self.character_class = "Mage"
                self.strength = 5
                self.agility = 8
                self.magic = 15
                self.inventory = ["Oak Staff", "Mana Potion", "Health Potion"]
                break
            elif choice == "3":
                self.character_class = "Rogue"
                self.strength = 8
                self.agility = 15
                self.magic = 5
                self.inventory = ["Dagger", "Lockpicks", "Health Potion"]
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        print(f"\nExcellent! You are now a {self.character_class}!")
        self.display_stats()
    
    def display_stats(self):
        """Display current player stats"""
        print(f"\n=== {self.name.upper()} THE {self.character_class.upper()} ===")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Magic: {self.magic}")
    
    def display_inventory(self):
        """Show player's inventory"""
        if not self.inventory:
            print("\nYour inventory is empty.")
            return
        
        print("\n=== INVENTORY ===")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item}")
    
    def use_item(self, item_index):
        """Use an item from inventory"""
        try:
            item = self.inventory[item_index]
            if "Health Potion" in item:
                heal_amount = 30
                self.health = min(self.max_health, self.health + heal_amount)
                print(f"You used a Health Potion and recovered {heal_amount} HP!")
                self.inventory.pop(item_index)
            elif "Mana Potion" in item:
                print("You feel magical energy flowing through you!")
                self.inventory.pop(item_index)
            else:
                print(f"You examine the {item}, but cannot use it right now.")
        except IndexError:
            print("Invalid item selection.")

class CombatSystem:
    """Handle turn-based combat encounters"""
    
    def __init__(self, player):
        self.player = player
        self.enemies = []
        self.current_enemy = None
    
    def start_combat(self, enemy_name, enemy_health, enemy_damage):
        """Initialize combat with an enemy"""
        self.current_enemy = {
            "name": enemy_name,
            "health": enemy_health,
            "max_health": enemy_health,
            "damage": enemy_damage
        }
        
        print(f"\n⚔️ COMBAT STARTED! ⚔️")
        print(f"You encounter a {enemy_name}!")
        
        while self.current_enemy and self.current_enemy["health"] > 0 and self.player.health > 0:
            self.combat_turn()
        
        if self.player.health <= 0:
            print("\nYou have been defeated...")
            return False
        else:
            print(f"\nYou defeated the {enemy_name}!")
            return True
    
    def combat_turn(self):
        """Handle one turn of combat"""
        print(f"\n--- Your Turn ---")
        print(f"Your HP: {self.player.health}")
        print(f"{self.current_enemy['name']} HP: {self.current_enemy['health']}")
        
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Magic")
        print("4. Use Item")
        print("5. Flee")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            self.attack()
        elif choice == "2":
            self.defend()
        elif choice == "3":
            self.use_magic()
        elif choice == "4":
            self.use_item_combat()
        elif choice == "5":
            if self.flee():
                return
        else:
            print("Invalid choice! You hesitate and lose your turn.")
        
        # Enemy attack if still alive
        if self.current_enemy and self.current_enemy["health"] > 0:
            self.enemy_attack()
    
    def attack(self):
        """Player attacks the enemy"""
        base_damage = self.player.strength // 2
        damage = max(1, base_damage + random.randint(-2, 3))
        
        # Critical hit chance based on agility
        crit_chance = self.player.agility / 100
        if random.random() < crit_chance:
            damage *= 2
            print(f"Critical hit! You strike the {self.current_enemy['name']} for {damage} damage!")
        else:
            print(f"You attack the {self.current_enemy['name']} for {damage} damage!")
        
        self.current_enemy["health"] -= damage
    
    def defend(self):
        """Player defends, reducing incoming damage"""
        print("You take a defensive stance, preparing for the enemy's attack.")
        # Defense bonus will be applied in enemy_attack
    
    def use_magic(self):
        """Player uses magic if they have sufficient magic stat"""
        if self.player.magic < 8:
            print("Your magic ability is too weak to cast spells!")
            return
        
        print("\nChoose a spell:")
        print("1. Fireball (Cost: 5 Magic Power)")
        print("2. Heal (Cost: 8 Magic Power)")
        
        spell_choice = input("Enter your choice (1-2): ")
        
        if spell_choice == "1":
            if self.player.magic >= 5:
                damage = self.player.magic + random.randint(3, 8)
                self.current_enemy["health"] -= damage
                print(f"You cast Fireball on the {self.current_enemy['name']} for {damage} damage!")
            else:
                print("You don't have enough magic power!")
        elif spell_choice == "2":
            if self.player.magic >= 8:
                heal = self.player.magic // 2 + random.randint(5, 15)
                self.player.health = min(self.player.max_health, self.player.health + heal)
                print(f"You cast Heal and recover {heal} HP!")
            else:
                print("You don't have enough magic power!")
        else:
            print("Invalid spell choice!")
    
    def use_item_combat(self):
        """Use items during combat"""
        if not self.player.inventory:
            print("You have no items to use!")
            return
        
        self.player.display_inventory()
        try:
            item_choice = int(input("Enter item number to use (0 to cancel): ")) - 1
            if item_choice == -1:
                return
            self.player.use_item(item_choice)
        except (ValueError, IndexError):
            print("Invalid item selection!")
    
    def flee(self):
        """Attempt to flee from combat"""
        flee_chance = self.player.agility / 20  # Higher agility = better flee chance
        if random.random() < flee_chance:
            print("You successfully flee from combat!")
            self.current_enemy = None
            return True
        else:
            print("You failed to escape!")
            return False
    
    def enemy_attack(self):
        """Enemy attacks the player"""
        if not self.current_enemy:
            return
        
        damage = self.current_enemy["damage"] + random.randint(-2, 2)
        damage = max(1, damage)
        
        # Check if player was defending
        if random.random() < 0.3:  # 30% chance player was still defending
            damage = damage // 2
            print(f"The {self.current_enemy['name']} attacks, but your defense reduces the damage to {damage}!")
        else:
            print(f"The {self.current_enemy['name']} attacks you for {damage} damage!")
        
        self.player.health -= damage

class GameWorld:
    """Manage the game world, areas, and story progression"""
    
    def __init__(self, player):
        self.player = player
        self.areas = {
            "Village of Beginnings": {
                "description": "A quiet village where your journey begins. Smoke rises from chimneys and villagers go about their daily business.",
                "connections": ["Haunted Forest"],
                "completed": False
            },
            "Haunted Forest": {
                "description": "A dense, misty forest filled with ancient trees and eerie sounds. Strange creatures lurk in the shadows.",
                "connections": ["Village of Beginnings", "Enchanted Castle", "Bandit's Lair"],
                "completed": False
            },
            "Enchanted Castle": {
                "description": "A magnificent castle floating on clouds, home to powerful magic and ancient secrets.",
                "connections": ["Haunted Forest", "Crystal Sanctum"],
                "completed": False
            },
            "Bandit's Lair": {
                "description": "A hidden camp of ruthless bandits preying on travelers. Treasure and danger await.",
                "connections": ["Haunted Forest", "Dragon's Peak"],
                "completed": False
            },
            "Dragon's Peak": {
                "description": "A volcanic mountain where the ancient dragon Vermithrax guards his hoard. The air smells of sulfur and ash.",
                "connections": ["Bandit's Lair"],
                "completed": False
            },
            "Crystal Sanctum": {
                "description": "The final chamber where the Crystal of Souls pulses with unimaginable power. Your destiny awaits.",
                "connections": ["Enchanted Castle"],
                "completed": False
            }
        }
        self.combat_system = CombatSystem(player)
    
    def display_current_area(self):
        """Show description of current area"""
        area = self.areas[self.player.current_area]
        print(f"\n=== {self.player.current_area.upper()} ===")
        print(area["description"])
        
        if not area["completed"]:
            self.handle_area_encounter()
            area["completed"] = True
    
    def handle_area_encounter(self):
        """Handle unique encounters for each area"""
        area = self.player.current_area
        
        if area == "Village of Beginnings":
            self.village_encounter()
        elif area == "Haunted Forest":
            self.forest_encounter()
        elif area == "Enchanted Castle":
            self.castle_encounter()
        elif area == "Bandit's Lair":
            self.bandit_encounter()
        elif area == "Dragon's Peak":
            self.dragon_encounter()
        elif area == "Crystal Sanctum":
            self.sanctum_encounter()
    
    def village_encounter(self):
        """Village story encounter"""
        print("\nAn old sage approaches you:")
        print("'Traveler! The Crystal of Souls has been corrupted by dark forces. You must journey through the Haunted Forest and seek the Enchanted Castle or confront the Bandits in their lair. Choose your path wisely.'")
        
        # Give player a helpful item based on class
        if self.player.character_class == "Warrior":
            self.player.inventory.append("Sturdy Shield")
            print("The village blacksmith gives you a Sturdy Shield!")
        elif self.player.character_class == "Mage":
            self.player.inventory.append("Arcane Tome")
            print("The village elder gives you an Arcane Tome!")
        elif self.player.character_class == "Rogue":
            self.player.inventory.append("Smoke Bombs")
            print("The shady merchant gives you Smoke Bombs!")
    
    def forest_encounter(self):
        """Haunted Forest encounter"""
        print("\nAs you journey through the misty forest, a pack of Shadow Wolves emerges from the darkness!")
        
        if not self.combat_system.start_combat("Shadow Wolf Pack", 25, 8):
            return
        
        # Reward for winning
        print("After defeating the wolves, you find a hidden cache!")
        self.player.inventory.append("Forest Elixir")
        self.player.quest_progress += 1
        
        print("\nTwo paths lie before you: one leads to the shimmering Enchanted Castle, the other to the dangerous Bandit's Lair.")
        choice = input("Which path do you take? (1: Castle, 2: Lair): ")
        
        if choice == "1":
            self.move_to_area("Enchanted Castle")
        else:
            self.move_to_area("Bandit's Lair")
    
    def castle_encounter(self):
        """Enchanted Castle encounter"""
        print("\nYou approach the floating castle. A mystical guardian blocks your path.")
        print("'Who dares approach the Castle of Magic? State your business, mortal.'")
        
        print("\nHow do you respond?")
        print("1. 'I seek the Crystal of Souls to restore balance!'")
        print("2. 'I mean no harm, I only seek knowledge.'")
        print("3. 'Step aside or face my wrath!'")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("The guardian nods. 'Your heart is pure. You may pass and learn our secrets.'")
            self.player.magic += 2
            self.player.inventory.append("Amulet of Wisdom")
            print("You gain +2 Magic and receive an Amulet of Wisdom!")
            self.player.choices_made.append("diplomatic_castle")
        elif choice == "2":
            print("'Your curiosity is noted. Pass, but be warned - knowledge carries great responsibility.'")
            self.player.inventory.append("Ancient Scroll")
            print("You receive an Ancient Scroll!")
            self.player.choices_made.append("curious_castle")
        else:
            print("'Foolish mortal! You will learn respect!'")
            if not self.combat_system.start_combat("Mystic Guardian", 35, 12):
                return
            self.player.choices_made.append("aggressive_castle")
        
        self.player.quest_progress += 2
        self.move_to_area("Crystal Sanctum")
    
    def bandit_encounter(self):
        """Bandit's Lair encounter"""
        print("\nYou sneak into the bandit camp. The bandit leader confronts you!")
        print("'Well, well, what do we have here? Looking to join our merry band or looking for trouble?'")
        
        print("\nHow do you respond?")
        print("1. 'I'm here to put an end to your crimes!'")
        print("2. 'I seek passage to Dragon's Peak. Let me through and no one gets hurt.'")
        print("3. 'Actually, I was hoping to join your crew...'")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("'Then you'll die like all the other heroes!'")
            if not self.combat_system.start_combat("Bandit Leader", 40, 10):
                return
            self.player.choices_made.append("heroic_bandits")
            print("After defeating the bandits, you find a treasure chest!")
            self.player.inventory.append("Golden Locket")
        elif choice == "2":
            if self.player.strength >= 12:
                print("The bandit leader sizes you up. 'You look tough enough. Fine, pass through, but don't cause trouble.'")
                self.player.choices_made.append("intimidating_bandits")
            else:
                print("The bandit leader laughs. 'You think you can threaten me? Get him, boys!'")
                if not self.combat_system.start_combat("Bandit Leader", 40, 10):
                    return
                self.player.choices_made.append("failed_intimidate_bandits")
        else:
            print("'Is that so? Prove your worth by taking care of my... dragon problem at the peak.'")
            self.player.choices_made.append("joined_bandits")
            print("The bandits let you pass to Dragon's Peak.")
        
        self.player.quest_progress += 2
        self.move_to_area("Dragon's Peak")
    
    def dragon_encounter(self):
        """Dragon's Peak encounter - major branching point"""
        print("\nYou stand before Vermithrax, the ancient dragon. His scales shimmer like molten gold.")
        print("'MORTAL! WHY DO YOU DISTURB MY SLUMBER? DO YOU SEEK DEATH OR SOMETHING MORE?'")
        
        print("\nHow do you approach the dragon?")
        print("1. 'I'm here to claim your hoard, lizard!' (Attack)")
        print("2. 'Great Vermithrax, I seek the Crystal to save our world.' (Diplomacy)")
        print("3. 'The bandits sent me to deal with you.' (If you joined bandits)")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("'FOOLISH MORTAL! YOU WILL BURN!'")
            if not self.combat_system.start_combat("Ancient Dragon Vermithrax", 60, 15):
                return
            self.player.choices_made.append("killed_dragon")
            print("With the dragon defeated, you find a path to the Crystal Sanctum behind its hoard.")
            self.move_to_area("Crystal Sanctum")
        
        elif choice == "2":
            print("The dragon regards you curiously. 'A BRAVE SOUL... TELL ME, WHY SHOULD I TRUST YOU?'")
            
            if "Amulet of Wisdom" in self.player.inventory or "Ancient Scroll" in self.player.inventory:
                print("You show the dragon your magical artifact as proof of your wisdom.")
                print("'I SEE YOU HAVE EARNED THE TRUST OF THE MYSTICS. VERY WELL, I WILL ALLOW YOU PASSAGE.'")
                self.player.choices_made.append("befriended_dragon")
                print("Vermithrax creates a magical portal to the Crystal Sanctum for you.")
                self.move_to_area("Crystal Sanctum")
            else:
                print("The dragon senses uncertainty in you. 'YOUR WORDS ARE EMPTY! PROVE YOUR WORTH IN COMBAT!'")
                if not self.combat_system.start_combat("Ancient Dragon Vermithrax", 50, 12):
                    return
                self.player.choices_made.append("earned_dragon_respect")
                print("The dragon, impressed by your strength, allows you passage.")
                self.move_to_area("Crystal Sanctum")
        
        elif choice == "3" and "joined_bandits" in self.player.choices_made:
            print("'THE BANDITS DARE SEND AN ASSASSIN? THEY WILL PAY FOR THIS INSULT!'")
            if not self.combat_system.start_combat("Enraged Dragon Vermithrax", 55, 18):
                return
            self.player.choices_made.append("betrayed_bandits_dragon")
            print("With the dragon defeated, you return to the bandits...")
            self.bandit_betrayal_ending()
        else:
            print("Invalid choice! The dragon grows impatient.")
            self.dragon_encounter()
    
    def bandit_betrayal_ending(self):
        """Special ending if player betrays bandits"""
        print("\nYou return to the bandit camp with proof of the dragon's defeat.")
        print("The bandit leader celebrates: 'You did it! You're one of us now! Here's your share of the treasure.'")
        print("But as he turns his back, you see your opportunity...")
        
        choice = input("Do you: (1) Take the treasure and leave, (2) Betray the bandits and arrest them: ")
        
        if choice == "1":
            print("\n=== ENDING: BANDIT KING/QUEEN ===")
            print("You embrace the life of a bandit, becoming a legendary outlaw.")
            print("The Crystal of Souls remains corrupted, but you have gold and infamy.")
            self.game_over()
        else:
            print("\nYou reveal you're working with the royal guards and arrest the bandits!")
            print("=== ENDING: HERO OF THE REALM ===")
            print("You're celebrated as a hero who infiltrated and dismantled the bandit organization.")
            self.game_over()
    
    def sanctum_encounter(self):
        """Final area encounter - determines ending"""
        print("\nYou stand before the Crystal of Souls, pulsating with corrupted energy.")
        print("A dark figure emerges from the shadows - the Corruptor who poisoned the crystal!")
        
        if "befriended_dragon" in self.player.choices_made:
            print("Suddenly, Vermithrax appears behind you! 'I TOLD YOU I WOULD HELP, MORTAL!'")
            print("The dragon breathes fire on the Corruptor, weakening him significantly!")
            enemy_health = 40
        else:
            enemy_health = 60
        
        if not self.combat_system.start_combat("The Corruptor", enemy_health, 12):
            return
        
        print("\nWith the Corruptor defeated, the Crystal of Souls begins to stabilize.")
        self.determine_ending()
    
    def determine_ending(self):
        """Determine which ending the player gets based on choices"""
        print("\n=== THE CRYSTAL OF SOULS IS SAVED! ===")
        
        # Count different types of choices
        heroic_choices = sum(1 for choice in self.player.choices_made if "heroic" in choice or "diplomatic" in choice)
        neutral_choices = sum(1 for choice in self.player.choices_made if "curious" in choice or "intimidating" in choice)
        dark_choices = sum(1 for choice in self.player.choices_made if "aggressive" in choice or "joined" in choice or "killed" in choice)
        
        if heroic_choices > dark_choices and heroic_choices >= neutral_choices:
            self.hero_ending()
        elif dark_choices > heroic_choices and dark_choices > neutral_choices:
            self.dark_ending()
        else:
            self.neutral_ending()
    
    def hero_ending(self):
        """The heroic ending"""
        print("\n=== ENDING: TRUE HERO OF ELDORIA ===")
        print("Through compassion, bravery, and wisdom, you have saved Eldoria.")
        print("The Crystal of Souls shines brightly once more, and peace returns to the land.")
        print("Bards sing songs of your deeds for generations to come.")
        print("You are remembered as the hero who restored balance through courage and mercy.")
        self.game_over()
    
    def dark_ending(self):
        """The dark ending"""
        print("\n=== ENDING: THE NEW CORRUPTOR ===")
        print("You touch the Crystal of Souls, but the corruption seeks a new host...")
        print("Instead of purifying it, you absorb its power for yourself.")
        print("Eldoria now has a new master - one who rules through fear and power.")
        print("The cycle of corruption continues, but now you sit on the throne.")
        self.game_over()
    
    def neutral_ending(self):
        """The neutral ending"""
        print("\n=== ENDING: GUARDIAN OF THE CRYSTAL ===")
        print("You purify the Crystal of Souls but choose to remain as its guardian.")
        print("You watch over Eldoria from the shadows, intervening only when necessary.")
        print("The world knows peace, but few remember the adventurer who saved them.")
        print("You find contentment in knowing the world is safe, even if unknown.")
        self.game_over()
    
    def move_to_area(self, area_name):
        """Move player to a new area"""
        if area_name in self.areas:
            self.player.current_area = area_name
            print(f"\nYou travel to {area_name}...")
            time.sleep(1)
        else:
            print("You cannot travel to that area.")
    
    def game_over(self):
        """End the game"""
        print(f"\nThank you for playing Eldoria: The Crystal of Souls, {self.player.name}!")
        print(f"Your journey as a {self.player.character_class} has concluded.")
        sys.exit(0)

def main():
    """Main game function"""
    print("=" * 50)
    print("    ELDORIA: THE CRYSTAL OF SOULS")
    print("        A Text-Based RPG Adventure")
    print("=" * 50)
    
    player = Player()
    player.create_character()
    
    game_world = GameWorld(player)
    
    print("\nYour adventure begins now! Type 'help' for commands.")
    
    # Main game loop
    while player.health > 0:
        print(f"\nYou are in: {player.current_area}")
        command = input("\nWhat would you like to do? ").lower().strip()
        
        if command in ['quit', 'exit']:
            print("Thanks for playing!")
            break
        
        elif command == 'help':
            print("\n=== AVAILABLE COMMANDS ===")
            print("help - Show this help message")
            print("stats - Show your character stats")
            print("inventory - Show your inventory")
            print("use [item] - Use an item from inventory")
            print("explore - Explore current area")
            print("travel - Show available travel locations")
            print("quit - Exit the game")
        
        elif command == 'stats':
            player.display_stats()
        
        elif command == 'inventory':
            player.display_inventory()
        
        elif command.startswith('use'):
            try:
                item_num = int(command.split()[1]) - 1
                player.use_item(item_num)
            except (ValueError, IndexError):
                print("Usage: use [item number from inventory]")
        
        elif command == 'explore':
            game_world.display_current_area()
        
        elif command == 'travel':
            current_area_data = game_world.areas[player.current_area]
            print(f"\nFrom {player.current_area} you can travel to:")
            for area in current_area_data["connections"]:
                print(f"- {area}")
            
            destination = input("\nWhere would you like to go? (or 'cancel'): ")
            if destination in current_area_data["connections"]:
                game_world.move_to_area(destination)
                game_world.display_current_area()
            elif destination != 'cancel':
                print("You cannot travel to that location from here.")
        
        else:
            print("I don't understand that command. Type 'help' for available commands.")
    
    if player.health <= 0:
        print("\n=== GAME OVER ===")
        print("Your journey has ended...")

if __name__ == "__main__":
    main()