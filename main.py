from babylex_to_pd import read_lexicon_into_df
import os
import config
import tests

if __name__ == '__main__':

    # Checking if the csv file exists and if not - creates it and saves in data dir
    if not os.path.exists(config.csv_lex_path):
        read_lexicon_into_df(config.txt_lex_path).to_csv(config.csv_lex_path)

    test_res = tests.test(config.test_file_path)
    print(tests.test_analysis(test_res))


