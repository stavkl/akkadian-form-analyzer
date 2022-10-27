import pandas as pd
from lexicon import Lexicon
import config
# This file includes basic tests for the root generation process
# The entries to the test are manually coded in test_df
# If an entry passed the test it means three things:
# a. The correct root is in the results
# b. The alternative root is also in the results
# c. There are at most 10 results in the output


def test(test_csv_path):

    test_df = pd.read_csv(test_csv_path)
    test_lexicon = Lexicon(config.csv_lex_path)
    test_results_summary_df = pd.DataFrame(columns=['verb', 'got true root', 'got alternative root',
                                                    'res len within range', 'relevant res len',
                                                    'pass/fail', 'pass/fail score'])
    for index in test_df.index:

        true_root = test_df.at[index, 'true_root']
        alter_root = test_df.at[index, 'alternative_root'] # The alternative root is the same for when there is only one root
        verb = test_df.at[index, 'conjugated_verb']
        res_row = [verb]
        pass_fail_count = 0

        relevant_result, others_result = test_lexicon.lookup_roots(verb)
        if true_root in relevant_result['root'].values:
            res_row.append(1) # Got true root
            pass_fail_count += 1
        else:
            res_row.append(0)

        if alter_root in relevant_result['root'].values:
            res_row.append(1) # Got alternative root
            pass_fail_count += 1
        else:
            res_row.append(0)

        if len(relevant_result['root'].unique()) <= 10:
            res_row.append(1) # res len within range
            pass_fail_count += 1
        else:
            res_row.append(0)

        res_row.append(len(relevant_result)) # relevant res len

        if pass_fail_count == 3:
            res_row.append(1)
        else:
            res_row.append(0)

        res_row.append(pass_fail_count * 33)

        # Append the results list as a row to the summary results df
        test_sum_len = len(test_results_summary_df)
        test_results_summary_df.loc[test_sum_len] = res_row
        print(res_row)

    return test_results_summary_df


def test_analysis(test_results_summary_df):

    mean = test_results_summary_df['pass/fail score'].mean()
    print("Mean accuracy of model on test set is: ", mean)






















