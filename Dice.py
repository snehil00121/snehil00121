import random 

def roll_dice():
    dice_drawing = {
        1:(
            " __________",
            "|          |",
            "|     1    |",
            "|     .    |",
            "|          |",
            " __________",
        ),

        2:(
            " __________",
            "|          |",
            "|   .      |",
            "|     2    |",
            "|      .   |",
            " __________",
        ),

        3:(
            " __________",
            "|          |",
            "|   . 3    |",
            "|     .    |",
            "|       .  |",
            " __________",
        ),

        4:(
            " __________",
            "|          |",
            "|  .     . |",
            "|     4    |",
            "|  .     . |",
            " __________",
        ),

        5:(
            " __________",
            "|          |",
            "| .   5  . |",
            "|     .    |",
            "| .      . |",
            " __________",
        ),

        6:(
            " __________",
            "|          |",
            "|  .     . |",
            "|  .  6  . |",
            "|  .     . |",
            " __________",
        )
    }

    roll = input("Roll the dice? (yes/no) : ")

    while roll.lower() == "yes":
        dice = random.randint(1, 6)

        print("Dice rolled : {}".format(dice))
        print("\n".join(dice_drawing[dice]))

        roll = input("Roll again? (yes/no) : ")

    while roll.lower() == "no":
        print("Ok Bro!")
        break

roll_dice()