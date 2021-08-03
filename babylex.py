import pandas as pd
import re

# This is a utility module that only deals with transforming Aleksi Sahala's lexicon
# (see "Old Babylonian finite verb analyser v2.3" in http://www.ling.helsinki.fi/~asahala/parser2.html )
# into a pandas-readable csv file, with the standard transcript for akkadian
# if a file named babylex.csv exists in the working directory the main program will not run this utility
# and will work directly with that file


def utify_chars(babylex_df):
    """
    converts non standard akkadian into standard UTF characters. Note that the root column
    does not and cannot contain contracted or long vowels, hence the a-symmetry in
    the number of replacements needed
    :param babylex_df: dataframe that was built according to Sahala's lexicon
    :return: same dataframe with transformed characters
    """
    babylex_df['root'] = babylex_df['root'].str.replace("T", "ṭ")
    babylex_df['root'] = babylex_df['root'].str.replace("c", "š")
    babylex_df['root'] = babylex_df['root'].str.replace("S", "ṣ")
    babylex_df['root'] = babylex_df['root'].str.replace("x", "'")

    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("T", "ṭ")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("c", "š")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("S", "ṣ")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("X", "'")

    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("aa", "ā")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("ee", "ē")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("ii", "ī")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("uu", "ū")

    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("A", "â")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("E", "ê")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("I", "î")
    babylex_df['infinitive'] = babylex_df['infinitive'].str.replace("U", "û")

    return babylex_df


def read_lexicon_into_df(lex_txt_file):
    """
    Reads a lexicon text file from Sahala's website into a pandas dataframe with
    standard transcription, saves the transformed lexicon under 'babylex.csv' and returns
    the dataframe (usually for testing purposes, all the lexical searched should be performed
    on the csv file).

    :param lex_txt_file: a txt file that  should only contain lines of the following form
    <verb root='0nxd' class='a-a' type='' inf='' lang='B, Ass' gloss='praise, extol' />
    :return: pandas dataframe
    """
    data = []
    with open(lex_txt_file) as txtf:
        lines = txtf.readlines()
        for line in lines:
            root = re.search(r"root='(.*?)'", line).group(1)
            if root.startswith('0'):
                num_radicals = 3
            else:
                num_radicals = 4
            verb_class = re.search(r"class='(.*?)'", line).group(1)
            verb_type = re.search(r"type='(.*?)'", line).group(1)
            infinitive = re.search(r"inf='(.*?)'", line).group(1)
            languages = re.search(r"lang='(.*?)'", line).group(1)
            gloss = re.search(r"gloss='(.*?)'", line).group(1)

            data.append([root, num_radicals, verb_class, verb_type, infinitive, languages, gloss])

    lexicon_df = pd.DataFrame(data, columns=['root', 'num_radicals', 'class', 'type', 'infinitive', 'languages', 'gloss'])

    lexicon_df['root'] = lexicon_df['root'].str.replace("0", "")
    lexicon_df = utify_chars(lexicon_df)
    lexicon_df.to_csv('babylex.csv')
    return lexicon_df
