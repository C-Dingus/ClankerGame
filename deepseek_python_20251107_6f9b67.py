"""
Coral Kingdom: The Pearl of Tides
A text-based RPG adventure set in an underwater world
Generated entirely by AI
"""

import random
import time
import sys

class MarineCreature:
    """Player class as a marine creature with aquatic abilities"""
    
    def __init__(self):
        self.name = ""
        self.species = ""
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.current_location = "Kelp Forest Village"
        self.quest_progress = 0
        self.choices_made = []
        self.ocean_knowledge = 0  # New stat for reef wisdom
    
    def create_character(self):
        """Handle character creation process for marine species"""
        print("\n" + "="*40)
        print("    CORAL KINGDOM: THE PEARL OF TIDES")
        print("="*40)
        self.name = input("\nWhat is your name, young sea creature? ")
        
        print(f"\nWelcome to the reef, {self.name}! Choose your species:")
        print("1. Hammerhead Warrior - Powerful predator with high Strength")
        print("2. Octopus Mage - Intelligent shape-shifter with high Magic") 
        print("3. Dolphin Rogue - Agile swimmer with high Agility and sonar")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice == "1":
                self.species = "Hammerhead Warrior"
                self.strength = 15
                self.agility = 8
                self.magic = 5
                self.inventory = ["Razor-Sharp Fin", "Seaweed Bandage", "Coral Knife"]
                break
            elif choice == "2":
                self.species = "Octopus Mage"
                self.strength = 5
                self.agility = 8
                self.magic = 15
                self.inventory = ["Ink Sac", "Glowing Pearl", "Seaweed Bandage"]
                break
            elif choice == "3":
                self.species = "Dolphin Rogue"
                self.strength = 8
                self.agility = 15
                self.magic = 5
                self.inventory = ["Sonar Blast", "Shell Lockpicks", "Seaweed Bandage"]
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        print(f"\nExcellent! You are now a {self.species}!")
        self.display_stats()
    
    def display_stats(self):
        """Display current marine creature stats"""
        print(f"\n=== {self.name.upper()} THE {self.species.upper()} ===")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Magic: {self.magic}")
        print(f"Ocean Knowledge: {self.ocean_knowledge}")
    
    def display_inventory(self):
        """Show creature's inventory"""
        if not self.inventory:
            print("\nYour treasure pouch is empty.")
            return
        
        print("\n=== OCEAN TREASURES ===")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item}")
    
    def use_item(self, item_index):
        """Use an item from inventory"""
        try:
            item = self.inventory[item_index]
            if "Seaweed Bandage" in item:
                heal_amount = 30
                self.health = min(self.max_health, self.health + heal_amount)
                print(f"You used a Seaweed Bandage and recovered {heal_amount} HP!")
                self.inventory.pop(item_index)
            elif "Glowing Pearl" in item:
                self.magic += 2
                print("The Glowing Pearl enhances your magical abilities temporarily!")
                self.inventory.pop(item_index)
            elif "Coral Elixir" in item:
                self.health = self.max_health
                print("The Coral Elixir fully restores your health!")
                self.inventory.pop(item_index)
            else:
                print(f"You examine the {item}, but cannot use it right now.")
        except IndexError:
            print("Invalid item selection.")

class AquaticCombat:
    """Handle turn-based aquatic combat encounters"""
    
    def __init__(self, player):
        self.player = player
        self.current_predator = None
    
    def start_combat(self, predator_name, predator_health, predator_damage, special_ability=None):
        """Initialize combat with an aquatic predator"""
        self.current_predator = {
            "name": predator_name,
            "health": predator_health,
            "max_health": predator_health,
            "damage": predator_damage,
            "special": special_ability
        }
        
        print(f"\n🌊 AQUATIC COMBAT! 🌊")
        print(f"You face a {predator_name}!")
        
        while self.current_predator and self.current_predator["health"] > 0 and self.player.health > 0:
            self.combat_turn()
        
        if self.player.health <= 0:
            print("\nYou have been defeated by the ocean's dangers...")
            return False
        else:
            print(f"\nYou defeated the {predator_name}!")
            return True
    
    def combat_turn(self):
        """Handle one turn of aquatic combat"""
        print(f"\n--- Your Turn ---")
        print(f"Your HP: {self.player.health}")
        print(f"{self.current_predator['name']} HP: {self.current_predator['health']}")
        
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Aquatic Magic")
        print("4. Use Ocean Item")
        print("5. Flee to Safety")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            self.aquatic_attack()
        elif choice == "2":
            self.defend()
        elif choice == "3":
            self.use_aquatic_magic()
        elif choice == "4":
            self.use_item_combat()
        elif choice == "5":
            if self.flee():
                return
        else:
            print("Invalid choice! You hesitate in the currents.")
        
        # Predator attack if still alive
        if self.current_predator and self.current_predator["health"] > 0:
            self.predator_attack()
    
    def aquatic_attack(self):
        """Player attacks the predator"""
        base_damage = self.player.strength // 2
        damage = max(1, base_damage + random.randint(-2, 3))
        
        # Critical hit chance based on agility
        crit_chance = self.player.agility / 100
        if random.random() < crit_chance:
            damage *= 2
            print(f"Critical strike! You attack the {self.current_predator['name']} for {damage} damage!")
        else:
            print(f"You attack the {self.current_predator['name']} for {damage} damage!")
        
        self.current_predator["health"] -= damage
    
    def defend(self):
        """Player defends, reducing incoming damage"""
        print("You take a defensive position among the coral, preparing for the predator's attack.")
    
    def use_aquatic_magic(self):
        """Player uses aquatic magic if they have sufficient magic stat"""
        if self.player.magic < 8:
            print("Your magical connection to the ocean is too weak!")
            return
        
        print("\nChoose an aquatic spell:")
        print("1. Electric Shock (Cost: 5 Magic Power)")
        print("2. Healing Currents (Cost: 8 Magic Power)")
        print("3. Ink Cloud (Cost: 3 Magic Power) - Octopus only")
        
        spell_choice = input("Enter your choice (1-3): ")
        
        if spell_choice == "1":
            if self.player.magic >= 5:
                damage = self.player.magic + random.randint(3, 8)
                self.current_predator["health"] -= damage
                print(f"You zap the {self.current_predator['name']} with an Electric Shock for {damage} damage!")
            else:
                print("You don't have enough magic power!")
        elif spell_choice == "2":
            if self.player.magic >= 8:
                heal = self.player.magic // 2 + random.randint(5, 15)
                self.player.health = min(self.player.max_health, self.player.health + heal)
                print(f"You summon Healing Currents and recover {heal} HP!")
            else:
                print("You don't have enough magic power!")
        elif spell_choice == "3" and self.player.species == "Octopus Mage":
            if self.player.magic >= 3:
                print("You release an Ink Cloud, confusing the predator and reducing their next attack!")
                # Special effect would be implemented here
            else:
                print("You don't have enough magic power!")
        else:
            print("Invalid spell choice or species restriction!")
    
    def use_item_combat(self):
        """Use items during combat"""
        if not self.player.inventory:
            print("You have no ocean treasures to use!")
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
        flee_chance = self.player.agility / 20
        if random.random() < flee_chance:
            print("You successfully swim to safety!")
            self.current_predator = None
            return True
        else:
            print("The predator blocks your escape route!")
            return False
    
    def predator_attack(self):
        """Predator attacks the player"""
        if not self.current_predator:
            return
        
        damage = self.current_predator["damage"] + random.randint(-2, 2)
        damage = max(1, damage)
        
        # Special abilities
        if self.current_predator["special"] == "venom" and random.random() < 0.3:
            damage += 3
            print(f"The {self.current_predator['name']} uses venomous strike for {damage} damage!")
        elif self.current_predator["special"] == "constrict" and random.random() < 0.25:
            damage += 2
            print(f"The {self.current_predator['name']} constricts you for {damage} damage!")
        else:
            print(f"The {self.current_predator['name']} attacks you for {damage} damage!")
        
        self.player.health -= damage

class ReefWorld:
    """Manage the coral reef world, locations, and story progression"""
    
    def __init__(self, player):
        self.player = player
        self.locations = {
            "Kelp Forest Village": {
                "description": "A vibrant village built among towering kelp forests. Colorful fish dart between the fronds as ancient sea turtles watch over the community.",
                "connections": ["Coral Maze", "Sunken Galleon"],
                "completed": False
            },
            "Coral Maze": {
                "description": "A labyrinth of breathtaking coral formations in every color imaginable. The twisting paths are easy to get lost in, and predators lurk in the shadows.",
                "connections": ["Kelp Forest Village", "Abyssal Trench", "Volcanic Vents"],
                "completed": False
            },
            "Sunken Galleon": {
                "description": "The wreck of an ancient surface-dweller ship, now home to curious fish and hidden treasures. Barnacles and coral encrust the wooden hull.",
                "connections": ["Kelp Forest Village", "Giant Clam Gardens"],
                "completed": False
            },
            "Abyssal Trench": {
                "description": "A dark, deep trench where sunlight barely reaches. Glowing creatures provide the only illumination in this mysterious depth.",
                "connections": ["Coral Maze", "Kraken's Lair"],
                "completed": False
            },
            "Volcanic Vents": {
                "description": "Hydrothermal vents spew mineral-rich water, creating an oasis of strange lifeforms. The water is warm and tinged with sulfur.",
                "connections": ["Coral Maze", "Leviathan's Domain"],
                "completed": False
            },
            "Giant Clam Gardens": {
                "description": "A field of enormous clams, some large enough to swallow a dolphin whole. Pearls of incredible size gleam within.",
                "connections": ["Sunken Galleon"],
                "completed": False
            },
            "Kraken's Lair": {
                "description": "A cave formed from ancient coral and rock, filled with the bones of the Kraken's prey. The water feels heavy with ancient power.",
                "connections": ["Abyssal Trench"],
                "completed": False
            },
            "Leviathan's Domain": {
                "description": "The territory of the ancient Leviathan, where the Pearl of Tides rests. The water hums with primordial energy.",
                "connections": ["Volcanic Vents"],
                "completed": False
            }
        }
        self.combat_system = AquaticCombat(player)
    
    def display_current_location(self):
        """Show description of current location"""
        location = self.locations[self.player.current_location]
        print(f"\n=== {self.player.current_location.upper()} ===")
        print(location["description"])
        
        if not location["completed"]:
            self.handle_location_encounter()
            location["completed"] = True
    
    def handle_location_encounter(self):
        """Handle unique encounters for each location"""
        location = self.player.current_location
        
        if location == "Kelp Forest Village":
            self.kelp_forest_encounter()
        elif location == "Coral Maze":
            self.coral_maze_encounter()
        elif location == "Sunken Galleon":
            self.sunken_galleon_encounter()
        elif location == "Abyssal Trench":
            self.abyssal_trench_encounter()
        elif location == "Volcanic Vents":
            self.volcanic_vents_encounter()
        elif location == "Giant Clam Gardens":
            self.clam_gardens_encounter()
        elif location == "Kraken's Lair":
            self.kraken_encounter()
        elif location == "Leviathan's Domain":
            self.leviathan_encounter()
    
    def kelp_forest_encounter(self):
        """Starting village encounter"""
        print("\nAn elderly Sea Turtle approaches you slowly:")
        print("'Young one, the Pearl of Tides has been disturbed from its resting place. The ocean's balance is shifting. You must journey through the Coral Maze and seek either the Sunken Galleon or the deeper territories. Choose your current wisely.'")
        
        # Give player a helpful item based on species
        if self.player.species == "Hammerhead Warrior":
            self.player.inventory.append("Reinforced Scales")
            print("The village blacksmith gives you Reinforced Scales for protection!")
        elif self.player.species == "Octopus Mage":
            self.player.inventory.append("Ancient Conch")
            print("The village elder gives you an Ancient Conch that whispers ocean secrets!")
        elif self.player.species == "Dolphin Rogue":
            self.player.inventory.append("Echolocation Charm")
            print("The swift messenger gives you an Echolocation Charm!")
        
        self.player.ocean_knowledge += 1
    
    def coral_maze_encounter(self):
        """Coral Maze encounter"""
        print("\nAs you navigate the beautiful but confusing coral formations, a school of aggressive Barracuda surrounds you!")
        
        if not self.combat_system.start_combat("Barracuda School", 25, 8, "swarm"):
            return
        
        # Reward for winning
        print("After defeating the barracuda, you find a hidden alcove with ocean treasures!")
        self.player.inventory.append("Coral Elixir")
        self.player.quest_progress += 1
        
        print("\nTwo paths branch before you: one leads downward to the dark Abyssal Trench, the other toward the warm Volcanic Vents.")
        choice = input("Which current do you follow? (1: Trench, 2: Vents): ")
        
        if choice == "1":
            self.move_to_location("Abyssal Trench")
        else:
            self.move_to_location("Volcanic Vents")
    
    def sunken_galleon_encounter(self):
        """Sunken ship encounter"""
        print("\nYou approach the ancient wreck. A massive Giant Moray Eel guards the entrance.")
        print("'This is my territory, little fish! What business do you have here?'")
        
        print("\nHow do you respond?")
        print("1. 'I seek the Pearl of Tides to restore ocean balance!'")
        print("2. 'I mean no harm, I'm just exploring these ancient ruins.'")
        print("3. 'This territory belongs to the ocean, not you! Move aside!'")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("The moray eel studies you. 'The Pearl... I haven't heard that name in ages. If you truly seek to restore balance, you may pass.'")
            self.player.ocean_knowledge += 2
            self.player.inventory.append("Navigator's Sextant")
            print("The eel gives you a Navigator's Sextant from the wreck!")
            self.player.choices_made.append("diplomatic_galleon")
        elif choice == "2":
            print("'Curiosity is natural, but dangerous. Very well, explore - but touch nothing that belongs to me.'")
            self.player.inventory.append("Ancient Gold Coin")
            print("You find an Ancient Gold Coin in the sand!")
            self.player.choices_made.append("curious_galleon")
        else:
            print("'You dare challenge me in my own home? You will make a fine meal!'")
            if not self.combat_system.start_combat("Giant Moray Eel", 35, 12, "venom"):
                return
            self.player.choices_made.append("aggressive_galleon")
        
        self.player.quest_progress += 2
        self.move_to_location("Giant Clam Gardens")
    
    def abyssal_trench_encounter(self):
        """Deep trench encounter"""
        print("\nYou descend into the darkness. Strange, glowing anglerfish appear, their lights bobbing in the gloom.")
        
        if not self.combat_system.start_combat("Anglerfish Pack", 30, 10, "lure"):
            return
        
        print("After defeating the anglerfish, you notice a deep cave entrance glowing with faint blue light.")
        self.player.inventory.append("Bioluminescent Fungus")
        self.player.choices_made.append("explored_trench")
        self.player.quest_progress += 2
        self.move_to_location("Kraken's Lair")
    
    def volcanic_vents_encounter(self):
        """Volcanic vents encounter"""
        print("\nThe warm, mineral-rich waters feel strange. Suddenly, a pack of vicious Vent Crabs scuttle from the rocks!")
        
        if not self.combat_system.start_combat("Vent Crab Colony", 28, 9, "constrict"):
            return
        
        print("The defeated crabs retreat, revealing a path to an even hotter area where immense creatures dwell.")
        self.player.inventory.append("Volcanic Shard")
        self.player.choices_made.append("explored_vents")
        self.player.quest_progress += 2
        self.move_to_location("Leviathan's Domain")
    
    def clam_gardens_encounter(self):
        """Giant clam gardens encounter"""
        print("\nYou arrive at the magnificent clam gardens. The largest clam you've ever seen opens slowly.")
        print("A soft voice echoes in your mind: 'I am the Ancient Clam, guardian of pearls and wisdom. Why do you disturb my meditation?'")
        
        print("\nHow do you respond?")
        print("1. 'I seek knowledge about the Pearl of Tides and the ocean's imbalance.'")
        print("2. 'I've heard tales of your incredible pearls. I wish to see them.'")
        print("3. 'Your pearls would make me powerful. Give them to me!'")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("'The Pearl of Tides... yes, I remember when the Leviathan guarded it. The Kraken grew jealous and stole it, corrupting its power.'")
            self.player.ocean_knowledge += 3
            self.player.inventory.append("Pearl of Wisdom")
            print("The Ancient Clam gives you a Pearl of Wisdom!")
            self.player.choices_made.append("wise_clam")
        elif choice == "2":
            print("'Beauty calls to beauty, I see. Very well, behold...' The clam reveals a magnificent pearl.")
            self.player.inventory.append("Iridescent Pearl")
            print("The clam lets you take a beautiful Iridescent Pearl!")
            self.player.choices_made.append("appreciative_clam")
        else:
            print("'Greed consumes you as it consumed the Kraken. I cannot help one so blind.'")
            print("The clam closes abruptly, and you must find your own way forward.")
            self.player.choices_made.append("greedy_clam")
        
        # From here, the player learns they must confront either Kraken or Leviathan
        print("\nThe Ancient Clam's wisdom reveals two paths: confront the Kraken who stole the Pearl, or seek the Leviathan who once guarded it.")
        final_choice = input("Which ancient being will you seek? (1: Kraken, 2: Leviathan): ")
        
        if final_choice == "1":
            self.move_to_location("Kraken's Lair")
        else:
            self.move_to_location("Leviathan's Domain")
    
    def kraken_encounter(self):
        """Kraken encounter - major branching point"""
        print("\nYou enter the Kraken's Lair. The massive cephalopod towers before you, the corrupted Pearl of Tides glowing angrily in one tentacle.")
        print("'INTERLOPER! YOU DARE CHALLENGE ME IN MY DOMAIN? THE PEARL IS MINE NOW!'")
        
        print("\nHow do you approach the Kraken?")
        print("1. 'I'm here to take back what you stole, monster!' (Attack)")
        print("2. 'Great Kraken, the Pearl corrupts you. Let me help restore balance.' (Diplomacy)")
        print("3. 'I can help you master the Pearl's power instead of fighting it.' (Corruption)")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("'FOOLISH CREATURE! YOU WILL JOIN THE BONES THAT DECORATE MY LAIR!'")
            if not self.combat_system.start_combat("The Kraken", 60, 15, "tentacles"):
                return
            self.player.choices_made.append("defeated_kraken")
            print("With the Kraken defeated, you claim the Pearl of Tides!")
            self.move_to_location("Leviathan's Domain")
        
        elif choice == "2":
            print("The Kraken's tentacles twitch nervously. 'BALANCE? THE OCEAN HAS NEVER BEEN BALANCED! WHY SHOULD I LISTEN TO YOU?'")
            
            if "Pearl of Wisdom" in self.player.inventory or self.player.ocean_knowledge >= 5:
                print("You share the wisdom you've gained from your journey.")
                print("'YOU... UNDERSTAND. PERHAPS... PERHAPS THE PEARL HAS BEEN BURNING ME.'")
                self.player.choices_made.append("redeemed_kraken")
                print("The Kraken reluctantly gives you the Pearl of Tides.")
                self.move_to_location("Leviathan's Domain")
            else:
                print("The Kraken senses your uncertainty. 'YOUR WORDS ARE EMPTY! YOU KNOW NOTHING OF TRUE POWER!'")
                if not self.combat_system.start_combat("Enraged Kraken", 50, 12, "ink_cloud"):
                    return
                self.player.choices_made.append("forced_kraken")
                print("The Kraken, beaten but not broken, surrenders the Pearl.")
                self.move_to_location("Leviathan's Domain")
        
        elif choice == "3":
            print("'YOU OFFER PARTNERSHIP? INTERESTING... TOGETHER WE COULD RULE ALL CURRENTS.'")
            self.player.choices_made.append("joined_kraken")
            self.kraken_alliance_ending()
        else:
            print("Invalid choice! The Kraken grows impatient.")
            self.kraken_encounter()
    
    def leviathan_encounter(self):
        """Final area encounter - determines ending"""
        print("\nYou enter the Leviathan's Domain. The ancient whale-like being floats majestically, its size unimaginable.")
        
        if "defeated_kraken" in self.player.choices_made or "redeemed_kraken" in self.player.choices_made or "forced_kraken" in self.player.choices_made:
            print("You hold the Pearl of Tides before the Leviathan.")
            print("'YOU HAVE RETURNED WHAT WAS LOST. BUT THE CORRUPTION LINGERS... WHO WILL BEAR THE BURDEN OF PROTECTION NOW?'")
        else:
            print("The Leviathan regards you with ancient eyes.")
            print("'YOU SEEK THE PEARL, YET IT REMAINS WITH THE KRAKEN. HAVE YOU COME TO SEEK MY HELP OR MY JUDGMENT?'")
        
        self.determine_ending()
    
    def kraken_alliance_ending(self):
        """Special ending if player allies with Kraken"""
        print("\nYou and the Kraken plot to dominate the ocean currents.")
        print("With the Pearl's corrupted power, you begin your campaign...")
        
        choice = input("Do you: (1) Rule together as equals, (2) Betray the Kraken and take all power: ")
        
        if choice == "1":
            print("\n=== ENDING: OCEAN TYRANTS ===")
            print("You and the Kraken establish a ruthless regime, controlling all ocean currents.")
            print("The Coral Kingdom lives in fear, but the seas are orderly under your iron fins.")
            self.game_over()
        else:
            print("\nYou wait for the perfect moment, then turn on the Kraken when it least expects it!")
            print("=== ENDING: SOLE MONARCH OF THE DEEP ===")
            print("With the Kraken defeated and the Pearl in your possession, you rule the entire ocean alone.")
            print("Your name is whispered in fear from the shallowest reef to the deepest trench.")
            self.game_over()
    
    def determine_ending(self):
        """Determine which ending the player gets based on choices"""
        print("\n=== THE PEARL OF TIDES GLOWS BEFORE YOU ===")
        
        # Count different types of choices
        wise_choices = sum(1 for choice in self.player.choices_made if "diplomatic" in choice or "wise" in choice or "redeemed" in choice)
        neutral_choices = sum(1 for choice in self.player.choices_made if "curious" in choice or "appreciative" in choice or "explored" in choice)
        corrupt_choices = sum(1 for choice in self.player.choices_made if "aggressive" in choice or "greedy" in choice or "joined" in choice or "forced" in choice)
        
        if wise_choices > corrupt_choices and wise_choices >= neutral_choices:
            self.wisdom_ending()
        elif corrupt_choices > wise_choices and corrupt_choices > neutral_choices:
            self.corruption_ending()
        else:
            self.balance_ending()
    
    def wisdom_ending(self):
        """The wisdom ending"""
        print("\n=== ENDING: OCEAN SAGE ===")
        print("Through wisdom, patience, and understanding, you restore the Pearl of Tides to its rightful purpose.")
        print("The ocean currents flow true once more, and all marine life celebrates your wisdom.")
        print("You become a legendary sage whose counsel is sought by creatures great and small.")
        print("The Coral Kingdom enters a new age of prosperity and harmony.")
        self.game_over()
    
    def corruption_ending(self):
        """The corruption ending"""
        print("\n=== ENDING: ABYSSAL MONARCH ===")
        print("You touch the Pearl of Tides, but its corruption seeks a new host...")
        print("Instead of purifying it, you embrace its power and make it your own.")
        print("The ocean now has a new master - one who rules through might and fear.")
        print("The currents obey your will, but the sea has lost its natural balance.")
        self.game_over()
    
    def balance_ending(self):
        """The balance ending"""
        print("\n=== ENDING: GUARDIAN OF CURRENTS ===")
        print("You purify the Pearl of Tides and establish a new order of guardians.")
        print("Representatives from all ocean species work together to protect the Pearl.")
        print("The ocean finds a new balance between freedom and order, might and wisdom.")
        print("You fade into legend, known only as the one who taught the sea to protect itself.")
        self.game_over()
    
    def move_to_location(self, location_name):
        """Move player to a new location"""
        if location_name in self.locations:
            self.player.current_location = location_name
            print(f"\nYou swim to {location_name}...")
            time.sleep(1)
        else:
            print("You cannot travel to that location.")
    
    def game_over(self):
        """End the game"""
        print(f"\nThank you for playing Coral Kingdom: The Pearl of Tides, {self.player.name}!")
        print(f"Your journey as a {self.player.species} has concluded.")
        sys.exit(0)

def main():
    """Main game function"""
    
    player = MarineCreature()
    player.create_character()
    
    reef_world = ReefWorld(player)
    
    print("\nYour aquatic adventure begins now! Type 'help' for commands.")
    
    # Main game loop
    while player.health > 0:
        print(f"\nCurrent Location: {player.current_location}")
        command = input("\nWhat would you like to do? ").lower().strip()
        
        if command in ['quit', 'exit']:
            print("Thanks for exploring the Coral Kingdom!")
            break
        
        elif command == 'help':
            print("\n=== OCEAN COMMANDS ===")
            print("help - Show this help message")
            print("stats - Show your creature stats")
            print("inventory - Show your ocean treasures")
            print("use [item] - Use an item from inventory")
            print("explore - Explore current location")
            print("travel - Show available swim paths")
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
            reef_world.display_current_location()
        
        elif command == 'travel':
            current_location_data = reef_world.locations[player.current_location]
            print(f"\nFrom {player.current_location} you can swim to:")
            for location in current_location_data["connections"]:
                print(f"- {location}")
            
            destination = input("\nWhere would you like to swim? (or 'cancel'): ")
            if destination in current_location_data["connections"]:
                reef_world.move_to_location(destination)
                reef_world.display_current_location()
            elif destination != 'cancel':
                print("You cannot swim to that location from here.")
        
        else:
            print("I don't understand that command. Type 'help' for available commands.")
    
    if player.health <= 0:
        print("\n=== OCEAN'S EMBRACE ===")
        print("Your journey ends in the deep...")

if __name__ == "__main__":
    main()
