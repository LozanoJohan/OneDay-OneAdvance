

COLORS = ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE",]

NUMBER_OF_COLORS_TO_GUESS = 4

TRIES = 10

DEBUG = True


def display_welcome():

    print(rf"""Welcome to the 'Guessing Color Game', there are {NUMBER_OF_COLORS_TO_GUESS} colors to guess and you have {TRIES} trIes till you do. 
          Each try just type {NUMBER_OF_COLORS_TO_GUESS} colors from the following options: {COLORS}""")



def set_game_colors():
    
    import random

    colors_to_guess = []
    
    for _ in range(NUMBER_OF_COLORS_TO_GUESS):

        color = COLORS[ random.randint(0, len(COLORS) - 1) ] # Gets a random index and use it to get a color
        colors_to_guess.append(color)

    return colors_to_guess



def preproccess_colors():

    _continue = True

    while _continue:

        _continue = False

        user_input =  input("Colors:").upper()
        input_colors = user_input.split()


        if user_input == 'Q':
            return 'Q'
        
        if len(input_colors) != NUMBER_OF_COLORS_TO_GUESS:

            print(f"""Woops, there should be exactly {NUMBER_OF_COLORS_TO_GUESS} colors in your input""")
            _continue = True

        for color in input_colors:
            if color.strip() not in COLORS:
    
                print(f"""Woops, '{color}' is still not avaiable in this wonderful game""")
                _continue = True


    return input_colors



def compute_feedback(input_colors: list , colors_to_guess: list):
    
    guessing_data = {
        'colors_right_in_position': 0,
        'colors_not_in_position': 0,
        'wrong_colors': 0
    }
    
    proccessed_input_colors = input_colors
    proccessed_colors_to_guess = colors_to_guess

    for i, color in enumerate(input_colors):

        if color not in colors_to_guess:
            guessing_data['wrong_colors'] += 1

        elif color == colors_to_guess[i]:

            guessing_data['colors_right_in_position'] += 1

            proccessed_input_colors.pop(i)
            proccessed_colors_to_guess.pop(i)
        

    for i, color in enumerate(proccessed_input_colors):

        if color not in proccessed_colors_to_guess:
            guessing_data['wrong_colors'] += 1

        else:
            guessing_data['colors_not_in_position'] += 1
    

    return guessing_data



def return_feedback(user_score):

    print(f"""Right colors: {user_score['colors_right_in_position']}
          Right but not in possition: {user_score['colors_not_in_position']}
          Wrong colors {user_score['wrong_colors']}""")
    


while True:
    tries_left = TRIES

    display_welcome()

    if DEBUG:   to_guess_colors = input().split()
    else: to_guess_colors = set_game_colors()
    print(to_guess_colors)

    while True:

        input_colors = preproccess_colors()

        if input_colors == 'Q':
            break

        user_score = compute_feedback(input_colors, to_guess_colors)

        if user_score['colors_right_in_position'] == NUMBER_OF_COLORS_TO_GUESS:
            print('You won')
            break

        return_feedback(user_score)

        tries_left -= 1
        print('Tries left:', tries_left)

        if tries_left == 0:
            print('You lost :(')
            break
    
    print('The answer was: ', to_guess_colors)

    user_input = input('Game ended. Play again? (Y/N) ').upper()
    if user_input != 'Y':

        print('Thanks for playing. Have a nice day.')
        break