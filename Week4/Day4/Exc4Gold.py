import random


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    count = 0
    while True:
        first_dice = throw_dice()
        second_dice = throw_dice()
        if (first_dice == second_dice):
            count += 1
            return count
            break
        else:
            count += 1
            continue

def main():
    count_store=[]
    for n in range(1,100):
        count_store.append(throw_until_doubles())
    print(f"Total count it took is {sum(count_store)}")
    print(f"Average count it took is {sum(count_store)/100}")

main()