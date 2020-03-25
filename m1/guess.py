import random

if __name__ == '__main__':
    ub = 100
    secret = random.randint(1, ub)
    cnt = 0
    while True:
        cnt += 1
        print("Guess a number in 1 -", ub)
        val = input()
        val = int(val)

        if val == secret:
            print("You guessed it right!")
            break
        elif val < secret:
            print("\tYou guessed", val, ", which is too small!")
        else:
            print("\tYou guessed", val, ", which is too big!")

        print("\tYou have guessed", cnt, "times.")





