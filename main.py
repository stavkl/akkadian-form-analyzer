from babylex import read_lexicon_into_df
import os
from lexicon import Lexicon


def lang_menu():
    strs = ('1 - Babylonian (All Periods)\n'
            '2 - Assyrian (All Periods)\n'
            '3 - Neo-Assyrian\n'
            '4 - Neo-Babylonian\n'
            '5 - Middle Assyrian\n'
            '6 - Middle Babylonian\n'
            '7 - Old Assyrian\n'
            '8 - Old Babylonian\n'
            '9 - Old Akkadian\n'
            '10 - Mari\n'
            '11 - Nuzi\n'
            )

    lang_choice = input(strs)
    return int(lang_choice)


def menu():
    strs = ('1 - Enter conjugated verb\n'
            '2 - Exit\n')
    choice = input(strs)
    return int(choice)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if not os.path.exists('./babylex.csv'):
        lexicon_df = read_lexicon_into_df('babylex.txt')

    babylex_lex = Lexicon('./babylex.csv')
    # print((babylex_lex.head(10)).to_string())

    while True:
        choice = menu()
        if choice == 1:
            babylex_lex.relevant_lang = lang_menu()
            input_verb = input("Enter a conjugated verb: ")
            relevant_result, others_result = babylex_lex.lookup_roots(input_verb)
            result = relevant_result.to_string() +'\n\n' + others_result.to_string() + '\n'
            print(result)

        elif choice == 2:
            break


