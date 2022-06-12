#importing random module
import random

#Move class 
class Move:
    def __init__(self, name, type, power, accuracy, contact):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.contact = contact

#randomizing multi hit moves
multihitrandomizer = [25, 50, 50, 75, 75, 75, 100, 100, 125]

#list of moves
Moves = {

    #grass
    "Energy Ball" : Move("Energy Ball", "grass", 80, 100, "special"),
    "Leaf Blade" : Move("Leaf Blade", "grass", 90, 100, "physical"),
    "Bullet Seed" : Move("Bullet Seed", "grass", random.choice(multihitrandomizer), 90, "special"),
    "Seed Bomb" : Move("Seed Bomb", "grass", 80, 100, "physical"),
    "Leaf Storm" : Move("Leaf Storm", "grass", 130, 90, "special"),
    "Absorb" : Move("Absorb", "grass", 40, 100, "special"),
    "Razor Leaf" : Move("Razor Leaf", "grass", 55, 95, "physical"),
    "Giga Drain" : Move("Giga Drain", "grass", 75, 100, "special"),

    #fire
    "Flamethrower" : Move("Flamethrower", "fire", 90, 100, "special"),
    "Ember" : Move("Ember", "fire", 40, 100, "special"),
    "Heat Wave" : Move("Heat Wave", "fire", 95, 90, "special"),
    "Fire Punch" : Move("Fire Punch", "fire", 75, 100, "physical"),
    "Fire Fang" : Move("Fire Fang", "fire", 65, 95, "physical"),
    "Flare Blitz" : Move("Flare Blitz", "fire", 120, 100, "physical"),
    "Fire Blast" : Move("Fire Blast", "fire", 110, 85, "special"),
    "Lava Plume" : Move("Lava Plume", "fire", 80, 100, "special"),

    #water
    "Surf" : Move("Surf", "water", 90, 100, "special"),
    "Muddy Water" : Move("Muddy Water", "water", 90, 85, "special"),
    "Scald" : Move("Scald", "water", 80, 100, "special"),
    "Crabhammer" : Move("Crabhammer", "water", 100, 90, "physical"),
    "Hydro Pump" : Move("Hydro Pump", "water", 110, 85, "special"),
    "Aqua Jet" : Move("Aqua Jet", "water", 40, 100, "physical"),
    "Waterfall" : Move("Waterfall", "water", 80, 100, "physical"),
    "Liquidation" : Move("Liquidation", "water", 85, 100, "physical"),

    #bug
    "Bug Buzz" : Move("Bug Buzz", "bug", 90, 100, "special"),
    "Megahorn" : Move("Megahorn", "bug", 120, 85, "physical"),
    "X Scissor" : Move("X Scissor", "bug", 80, 100, "physical"),
    "Leech Life" : Move("Leech Life", "bug", 75, 100, "physical"),
    "Pin Missile" : Move("Pin Missile", "bug", random.choice(multihitrandomizer), 90, "physical"),
    "Lunge" : Move("Lunge", "bug", 90, 100, "special"),
    "Bug Bite" : Move("Bug Bite", "bug", 60, 100, "physical"),
    "Pollen Puff" : Move("Pollen Puff", "bug", 90, 100, "special"),

    #fairy
    "Moonblast" : Move("Moonblast", "fairy", 95, 100, "special"),
    "Play Rough" : Move("Play Rough", "fairy", 90, 90, "physical"),
    "Spirit Break" : Move("Spirit Break", "fairy", 75, 100, "physical"),
    "Dazzling Gleam" : Move("Dazzling Gleam", "fairy", 80, 100, "special"),
    "Fairy Wind" : Move("Fairy Wind", "fairy", 40, 100, "special"),
    "Misty Explosion" : Move("Misty Explosion", "fairy", 100, 90, "special"),
    "Draining Kiss" : Move("Draining Kiss", "fairy", 50, 95, "physical"),

    #ground
    "Earthquake" : Move("Earthquake", "ground", 100, 100, "physical"),
    "Stomping Tantrum" : Move("Stomping Tantrum", "ground", 75, 100, "physical"),
    "Earth Power" : Move("Earth Power", "ground", 80, 100, "special"),
    "Mud Bomb" : Move("Mud Bomb", "ground", 65, 90, "special"),
    "Bulldoze" : Move("Bulldoze", "ground", 60, 100, "physical"),
    "Sand Tomb" : Move("Sand Tomb", "ground", 35, 85, "special"),
    "Dig" : Move("Dig", "ground", 80, 100, "physical"),
    "Drill Run" : Move("Drill Run", "ground", 85, 90, "physical"),

    #flying
    "Brave Bird" : Move("Brave Bird", "flying", 120, 100, "physical"),
    "Air Slash" : Move("Air Slash", "flying", 75, 95, "special"),
    "Hurricane" : Move("Hurricane", "flying", 120, 70, "special"),
    "Aerial Ace" : Move("Aerial Ace", "flying", 60, 100, "physical"),
    "Gust" : Move("Gust", "flying", 40, 100, "special"),
    "Drill Peck" : Move("Drill Peck", "flying", 80, 100, "physical"),
    "Fly" : Move("Fly", "flying", 95, 85, "physical"),
    "Air Cutter" : Move("Air Cutter", "flying", 55, 95, "special"),

    #dark
    "Dark Pulse" : Move("Dark Pulse", "dark", 80, 100, "special"),
    "Crunch" : Move("Crunch", "dark", 80, 100, "physical"),
    "Bite" : Move("Bite", "dark", 60, 100, "physical"),
    "Night Slash" : Move("Night Slash", "dark", 70, 100, "physical"),
    "Snarl" : Move("Snarl", "dark", 60, 95, "special"),
    "Sucker Punch" : Move("Sucker Punch", "dark", 70, 100, "physical"),
    "Throat Chop" : Move("Throat Chop", "dark", 90, 100, "physical"),
    "Night Daze" : Move("Night Daze", "dark", 95, 85, "physical"),

    #electric
    "Thunderbolt" : Move("Thunderbolt", "electric", 90, 100, "special"),
    "Thundershock" : Move("Thundershock", "electric", 40, 100, "special"),
    "Wild Charge" : Move("Wild Charge", "electric", 90, 95, "physical"),
    "Thunder Punch" : Move("Thunder Punch", "electric", 75, 100, "physical"),
    "Thunder Fang" : Move("Thunder Fang", "electric", 65, 95, "physical"),
    "Thunder" : Move("Thunder", "electric", 120, 70, "special"),
    "Discharge" : Move("Discharge", "electric", 80, 100, "special"),
    "Spark" : Move("Spark", "electric", 65, 100, "physical"),

    #ice
    "Ice Beam" : Move("Ice Beam", "ice", 90, 100, "special"),
    "Blizzard" : Move("Blizzard", "ice", 120, 70, "special"),
    "Icicle Crash" : Move("Icicle Crash", "ice", 80, 90, "physical"),
    "Ice Punch" : Move("Ice Punch", "ice", 75, 100, "physical"),
    "Ice Fang" : Move("Ice Fang", "ice", 65, 95, "physical"),
    "Ice Shard" : Move("Ice Shard", "ice", 40, 100, "physical"),
    "Icy Wind" : Move("Icy Wind", "ice", 55, 100, "special"),
    "Powder Snow" : Move("Powder Snow", "ice", 40, 100, "special"),

    #normal
    "Tackle" : Move("Tackle", "normal", 40, 100, "physical"),
    "Body Slam" : Move("Body Slam", "normal", 80, 100, "physical"),
    "Explosion" : Move("Explosion", "normal", 250, 90, "physical"),
    "Hyper Beam" : Move("Hyper Beam", "normal", 150, 90, "special"),
    "Hyper Voice" : Move("Hydro Voice", "normal", 90, 100, "special"),
    "Headbutt" : Move("Headbutt", "normal", 70, 100, "physical"),
    "Tail Slap" : Move("Tail Slap", "normal", random.choice(multihitrandomizer), 90, "physical"),
    "Boomburst" : Move("Boomburst", "normal", 140, 100, "special"),
}
