import random
random.seed(0)

def menu():
    action = input("Rock, Paper, Scissors, Lizard, Spock? (type exit to quit):\n")
    return action
def main():
    while True:
        try:
            choise = menu()
        except:
            print("Invalid choise. Please try again.\n")
            continue

        rps = ['Rock', 'Paper','Scissors', 'Lizard', 'Spock']
        hit = random.choice(rps)
        
        if choise == 'Rock':
            if hit == 'Lizard':
                print('You won! Rock triumphs Lizard')
            else:
                print('You lost! Rock loses to {}'.format(hit))

        elif choise == 'Paper':
            if hit == 'Spock' or hit == 'Rock':
                print('You won! Paper triumphs {}'.format(hit))
            else:
                print('You lost! Paper loses to {}'.format(hit))

        elif choise == 'Scissors':
            if hit == 'Lizard' or hit == 'Paper':
                print('You won! Scissors triumphs {}'.format(hit))
            else:
                print('You lost! Scissors loses to {}'.format(hit))

        elif choise == 'Lizard':
            if hit == 'Spock' or hit == 'Paper':
                print('You won! Lizard triumphs {}'.format(hit))
            else:
                print('You lost! Lizard loses to {}'.format(hit))

        elif choise == 'Spock':
            if hit == 'Rock' or hit == 'Scissors':
                print('You won! Spock triumphs {}'.format(hit))
            else:
                print('You lost! Spock loses to {}'.format(hit))

        elif choise == 'exit':
            break

        else:
            print("It was a tie!")
            continue
main()
            
