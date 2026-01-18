import random

#Gets the height of the tree
def get_height():
    while True:
        try: 
            rows = int(input("Enter tree height: "))
            if 0 < rows <= 35:
                return rows
            elif rows <= 0:
                print("Please don't be a grinch, we can't make this tree xD")
            else:
                print("Sorry, too big! (it wont fit on the screen) Max 35 lol")
        except ValueError:
            print("Please enter a positive integer")

#Randomizes Decorations
def get_decorations():
    ornaments = random.randint(1, 100)
    if 0 < ornaments < 21:
        return "\033[31mo\033[0m"
    elif 20 < ornaments < 41:
        return "\033[34m@\033[0m"
    elif ornaments == 100:
        return "\033[33m$\033[0m"
    else:
        return "\033[32m*\033[0m"

def get_snow(spaces):
        for _ in range(spaces):
            snow = random.randint(1, 6)
            if snow == 1:
                print (" ❄️", end="")
            else: 
                print ("  ", end="")
 
#Builds the tree
def get_tree(tree_height, star_counter, first_row):
    for _ in range(tree_height):
        spaces = ( (2 * tree_height - 1) - star_counter ) // 2 

        #Snow on left side
        get_snow(spaces)
        
        for _ in range(star_counter):
            if first_row == True:
                print(" ⭐", end="")
                first_row = False
            else:
                decorations = get_decorations()
                print(f" {decorations}", end="")

        star_counter += 2

        #Snow on right side
        get_snow(spaces)
        print("")
    return first_row, star_counter

def get_presents(spaces):
    for _ in range(spaces):
        presents = random.randint(1, 6)
        if presents == 1:
            print ("🎁", end="")
        else: 
            print ("  ", end="")

#Builds the trunk
def get_trunk(tree_height):
    bottom_width = 2 * tree_height - 1
    trunk_width = 1
    spaces = (bottom_width - trunk_width) // 2

    #Top part of trunk
    print(("  " * spaces) + "\033[90m|_|\033[0m" + ("  " * spaces) )

    #Bottom of tree with presents
    get_presents(spaces)
    print("\033[90m|_|\033[0m", end="")
    get_presents(spaces)

#Adds praise
def get_praise(tree_height):

    praise_list = [
        "Ooooooh pretty",
        "Gorgeous!",
        "Wow! Nice Christmas Tree",
        "Man I wish it was Christmas",
        "Perfect!",
        "Christmastacular!",
        "SANTAAAAAAA",
        "Duuuuuuude",
        "Tree Tree",
        "Frederick sucks"
    ]

    #Finds padding of the tree
    bottom_length = 4 * tree_height - 1
    bottom_padding = bottom_length // 2

    #Finds padding and length of the praise
    praise = random.choice(praise_list)
    praise_length = len(praise)
    praise_padding = praise_length // 2

    #Somewhat centers praise under the tree
    spaces = (bottom_padding - praise_padding) // 2

    #Checks if the praise is longer than the tree
    if praise_length < bottom_length - 2:
        print("\n")
        print("  " * spaces + praise)
    else:
        print("\n")
        print(praise)
    
#Replay button
def play_again():
    while True:
        print("\n")
        again = input("Wanna make another tree? Y/N: ").strip().lower()
        if again == "y":
            return True
        elif again == "n":
            return False
        else: 
            print("Please enter a valid input, Y/N")

def main():
    while True:
        tree_height = get_height()
        star_counter = 1
        first_row = True
        
        first_row, star_counter = get_tree(tree_height, star_counter, first_row)
        get_trunk(tree_height)
        get_praise(tree_height)

        if not play_again():
            print("Merry Christmas!!!")
            break
    
if __name__ == "__main__":
    main()