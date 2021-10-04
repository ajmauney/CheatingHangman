new_dict = {}
new_list = []
# test_dict = {}
# test_dict[5] = ['segyf', 'asdfg', 'soeof', 'qweer', 'treew']
# test_dict[4] = ['toot', 'teet', 'toge', 'togf']

# WE NEED TO MAKE IT SO THE DICTIONARY HAS THE KEY AS EACH OF THE VALUES
# AND THE VALUE AS THE LIST OF WORDS WITH THAT VALUE


def play_game(new_dict):
    letters_guessed = []
    word_length = input("Enter a word length: ")
    word_length = int(word_length)

    if word_length in new_dict:
        num_guesses = input('Enter how many guesses you want: ')
    else:
        print('Please enter a different length.')
        exit()

    if int(num_guesses) <= 0:
        print('Please enter a valid number of guesses.')
        exit()

    word = ''
    for x in range(0, word_length):
        word += '-'

    cheats = input('Would you like to see a total number of words remaining? y/n \n')
    game_started = True
    while game_started:

        print('Your word so far: ',  word)
        letter = input('Enter a letter: ')
        print(letter)
        if letter not in letters_guessed:
            if len(letter) == 1 and letter.isalpha():
                letters_guessed.append(letter)
                print('Letters guessed: ', letters_guessed)
            else:
                print("Please enter a valid letter.\n")
                break
        else:
            letter = input('Please enter a letter you have not guessed.')
    # we have to store in a dictionary with the key being the indices that the letter occurs at
        word_family = {}
        for x in new_dict[word_length]:
            # going through each word that has the desired length
            key = []
            # print('This is x: ', x)
            if letter in x:
                # if the guessed letter is in the word we are looking at
                for y in range(0, len(x)):  # loop from 0 to the length of the word to check each character
                    if x[y] == letter:  # find each spot where the match is
                        key.append(y)  # append to list

                if len(key) > 1:
                    if tuple(key) not in word_family:
                        word_family[tuple(key)] = []
                        word_family[tuple(key)].append(x)
                    else:
                        word_family[tuple(key)].append(x)
                else:
                    if key[0] not in word_family:
                        word_family[key[0]] = []
                        word_family[key[0]].append(x)
                    else:
                        word_family[key[0]].append(x)

            else:
                if 'none' not in word_family:
                    word_family['none'] = []
                    word_family['none'].append(x)
                else:
                    word_family['none'].append(x)
        maxy = 0
        for key in word_family:
            if len(word_family[key]) > maxy:
                max_family = word_family[key]
                maxy = len(word_family[key])
        new_dict = {} # clear the dictionary to add new word families
        new_dict[word_length] = max_family
        # print('new word family', new_dict)
        # print('max family ', max_family)
        if cheats == 'y':
            print('number of words left: ', len(new_dict[word_length]))

        if letter in max_family[0]:
            j = 0
            for letters in max_family[0]:
                if letters == letter:
                    word = word[:j] + letter + word[j + 1:]
                j += 1

        if '-' not in word:
            print('Congratulations, you won')
            play_again()
            game_started = False
        else:
            num_guesses = int(num_guesses) - 1
            print('You have ', num_guesses, ' guesses left!')

        if num_guesses == 0:
            print('Sorry you lost! The word was: ', max_family[0])
            # if theres no guesses left, end game after the next guess
            play_again()


def play_again():
    play_again = input('Would you like to play again? y/n\n')
    if play_again == 'y':
        game_started = True
        play_game(new_dict)
    else:
        game_started = False
        end_game()


def end_game():
    print('Thanks for playing!')
    exit()


def main():
    with open('dictionary.txt') as file:
        for line in file:
            line = line.rstrip("\n")
            if len(line) not in new_dict:
                new_dict[len(line)] = [line]
            else:
                new_dict[len(line)].append(line)

    play_game(new_dict)


if __name__ == "__main__":
    main()