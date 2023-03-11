import random
import sys

def main():
    first = ("Blondie", "Nugget", "Teacup","Oldie", "Shortie", "Kiddo", "Smarty", "Boomer", "Scout", "Ace", "Buddy", "King", "Champ", "Bro", "Amigo", "Bubba Gump", "Tank", "Tiny", 
    "Goon", "Punk", "Rambo", "Bond", "Giggles", "Speedy", "Squirt", "Smiley", "Cheeseball", "Captain", "Sugar", "Teeny", "Clumsy Wumsy",  "Sport", "Giggles", 
    "Jokester", "Boo", "Mouse", "Munchkin", "Bee", "Dolly", "Precious", "Bug", "Chipmunk", "Dottie", "Cutie Pie", "Bonny Lass", "Sweetums", 
    "Toots", "Buttercup", "Lovey", "Slim", "Chief", "Buck", "Hot Stuff", "Burps", "Junior", "Senior", "Doc", "Dude", "Pal", "Buster", "Bud", "Soul Sister", "Sis", "Chica", "Missy", "Homegirl", "Lovey Dovey", "Handsome", "Prince Charming", "Gorgeous", 
    )

    last = ("O’Problem", "Derhover", "Gurgen Hoffe", "Gurgen Hoffe", "Hardcok", "Fartinghouse", "Dump", "Dump", "Feltherbush", "Cornholder", "Cornholder", "Cornholder", "Hugginkiss",  "Hugginkiss", "PoopyPants", "Cox", "Ulick", "Dickfit", "Yurinator"
    )

    while True:
        frist_name = random.choice(first)
        last_name = random.choice(last)

        print("{} {}".format(frist_name, last_name))
        print("\n\n")

        try_again = input("Try again? Press Enter else q to quit: \n")


        if try_again.lower() == "q":
            break

        input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
