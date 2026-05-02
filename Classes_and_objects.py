# 1. THE CLASS (The Blueprint)
# Think of this as the "Hero Factory"
class Hero:
    # The __init__ method is like the "Birth Certificate"
    # It sets up the character's basic info the moment they are created
    # This is the class attribute that shared by everyone 
    def __init__(self, name, power_level, weapon):
        self.name = name            # Attribute: The Hero's name
        self.power = power_level    # Attribute: How strong they are
        self.weapon = weapon        # Attribute: What they carry
        self.health = 100           # Attribute: Everyone starts with 100 HP

    # 2. THE METHODS (The Actions)
    # These are things the Hero can DO
    def introduce(self):
        print(f"I am {self.name}, and I fight with a {self.weapon}!")

    def train(self):
        self.power += 10            # Improving the hero's strength
        print(f"{self.name} trained hard! Power is now {self.power}.")

    def take_damage(self, amount):
        self.health -= amount       # Lowering health
        print(f"{self.name} was hit! Health: {self.health}")

# ---------------------------------------------------------
# 3. THE OBJECTS (The Real Characters)
# We use the same blueprint to make TWO different heroes
# ---------------------------------------------------------

# Create Player 1 (An Instance of Hero)
# This is the attribute (Store data)
player1 = Hero("Iron Knight", 50, "Sword")

# Create Player 2 (Another Instance of Hero)
player2 = Hero("Shadow Archer", 45, "Longbow")

# 4. USING THE OBJECTS
# We tell the specific objects to perform actions
player1.introduce()    # Output: I am Iron Knight, and I fight with a Sword!
player2.introduce()    # Output: I am Shadow Archer, and I fight with a Longbow!

player1.train()        # Iron Knight gets stronger
player2.take_damage(20) # Shadow Archer gets hurt