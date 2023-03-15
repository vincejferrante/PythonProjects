import random as rand
import sys

#
def main():
    slot_one = ("sevens", "ace", "cherries", "king", "queen", "jack", "apples", "grapes")
    slot_two = ("sevens", "ace", "cherries", "king", "queen", "jack", "apples", "grapes")
    slot_three = ("sevens", "ace", "cherries", "king", "queen", "jack", "apples", "grapes")

    while True:
        screen_one = rand.choice(slot_one)
        screen_two = rand.choice(slot_two)
        screen_three = rand.choice(slot_three)

        if (screen_one == screen_two and screen_one == screen_three):
            print("{} - {} - {} | You Win!".format(screen_one, screen_two, screen_three))
        else:
            print("{} - {} - {}".format(screen_one, screen_two, screen_three))

        try_again = input("Another Pull at our slot machine? Press Enter or if you want to quit press q")
        if try_again.lower() == "q":
            break
        

    

main()
