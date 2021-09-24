import random
def main():

    score = random()
    print(score)
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            print('Excellent')
        elif score >= 50:
            print("Passable")
        else:
            print('Bad')

def get_score():
    score =float(input("print your score:"))
    return score
def random():
    random_score=random.randint(0,100)
    return random_score
main()