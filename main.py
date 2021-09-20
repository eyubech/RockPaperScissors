import random
def game():
    list = ['r', 'p', 's']
    while True:
        print("*" * 25)
        user = input("Choose (rps)? : ")
        laptop = random.choice(list)
        print(f">>>YOU    : {user}")
        print(f">>>Laptop : {laptop}")
        if (user == 'r' and laptop == 'p') or (user == 's' and laptop == 'p') or (user == 'p' and laptop == 's'):
            print("[!]- WIN!")
        elif user == laptop:
            print("--Try Again--")
        else:
            print("[!]- LOSS :(")
if __name__ == '__main__':
    game()
