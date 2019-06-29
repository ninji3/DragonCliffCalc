import argparse
import characters

description = "Program to calculate effective attack value. Currenty no items only passing the main stat and attack level."
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-v", "--version", help="Show program version", action="store_true")
parser.add_argument("-c", "--character", help="character class")
parser.add_argument("-l", "--level", type=int, help="character level")
parser.add_argument("-m", "--main_stat", type=int, help="characters main stat")
parser.add_argument("-a", "--attack_level", type=int, help="level of attack")
parser.add_argument("-crt", "--crit", type=float, help="crit chance")
parser.add_argument("-crd", "--crit_damage", type=float, help="crit damage")
parser.add_argument("-e", "--dmg_enhance", type=float, help="additional damage enhancement")

args = parser.parse_args()
#sanitize the inputs and pass standard values
if not args.character:
    raise TypeError("Missing character class.")
if not args.level:
    args.level=1
    print("No character level specified. Assume level 1.")
if not args.main_stat:
    raiseTypeError("Missing main stat.")
if not args.attack_level:
    args.attack_level = 1
    print("No attack level specified. Assume level 1.")
if not args.crit:
    args.crit = 0.05
    print("No crit chance specified. Assume 5%.")
if not args.crit_damage:
    args.crit_damage: 2
    print("No crit damage specified. Assume 200%.")
if not args.dmg_enhance:
    args.dem_enhance = 0
    print("No elemental damage enhancement specified. Assume 0%.")

character = characters.BaseCharacter()

if (args.character == "Street Man"):
    character = characters.StreetMan(args.level, args.attack_level, args.main_stat, args.crit, args.crit_damage, args.dmg_enhance)

def get_attk_value(args):
    """
    Get the actual attack damage for a given attack.
    
    The formula currently looks like this:

    ATK_DMG = (MAIN_STAT)*(ATK_CAPACITY)*(DMG_ENHANCE)

    """
    attk_value = character.attack.get_effective_capacity()*character.main_stat*(character.dmg_enhance+1)

    return attk_value


def get_crit_value(args):
    """
    Simple crit value calculation

    CRIT_DMG = ATTK_DMG*CRIT

    """
    attk = get_attk_value(args)

    crit = args.crit_damage*attk

    return crit

def get_avg_value(args):
    
    attk = get_attk_value(args)
    crit = get_crit_value(args)
    avg_value = args.crit*crit + (1-args.crit)*attk

    return avg_value


attk = get_attk_value(args)
crit = get_crit_value(args)
avg = get_avg_value(args)

a = "Stats for: "
b = "Attack Damage: "
c = "Critical Damage: "
d = "Average Damage: "

print(character.__dict__)

print(f"{b:20}{attk}\n")
print(f"{c:20}{crit}\n")
print(f"{d:20}{avg}\n")

if args.version:
    print("Program version v1.0")