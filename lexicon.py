import pandas as pd
from root_generator import extract_possible_roots_from_dict, extract_possible_roots, filter_roots


def split_df_by_relevant_lang(df, lang):
    if lang == -1:
        relevant_df = df
        others_df = df
    else:
        relevant_df = df[df['languages'].str.contains(lang)]
        others_df = df[~df['languages'].str.contains(lang)]

    return relevant_df, others_df


class Lexicon:
    def __init__(self, filepath):
        self.lexicon_df = pd.read_csv(filepath)
        if 'Unnamed: 0' in self.lexicon_df.columns:
            self.lexicon_df = self.lexicon_df.drop(['Unnamed: 0'], axis=1)

        self.relevant_lang = -1  # Default = all languages. Used for testing purposes

    def lookup_roots(self, conjugated_verb):
        roots_list = extract_possible_roots(conjugated_verb)
        root_df = self.lexicon_df.loc[self.lexicon_df['root'].isin(roots_list)]
        root_df = filter_roots(root_df, conjugated_verb)
        print(root_df)
        relevant_lang_root_df, other_roots_df = split_df_by_relevant_lang(root_df, self.relevant_lang)
        return relevant_lang_root_df, other_roots_df

    def head(self, num_of_lines):
        return self.lexicon_df.head(num_of_lines)

    def demo(self, roots_list):
        root_df = self.lexicon_df.loc[self.lexicon_df['root'].isin(roots_list)]
        relevant_lang_root_df, other_roots_df = split_df_by_relevant_lang(root_df, self.relevant_lang)
        return relevant_lang_root_df, other_roots_df
