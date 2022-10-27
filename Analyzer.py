import pandas as pd
import streamlit as st
from babylex_to_pd import read_lexicon_into_df
import os
from root_generator import segment
from lexicon import Lexicon
st.set_page_config(layout="wide")

langs = ['Babylonian (All Periods)', 'Assyrian (All Periods)', 'Neo-Assyrian',
         'Neo-Babylonian', 'Middle Assyrian', 'Middle Babylonian',
         'Old Assyrian', 'Old Babylonian', 'Old Akkadian',
         'Mari', 'Nuzi']

# st.sidebar.markdown("## About the Lexicon")

st.title("Akkadian Form Analyzer")
st.write("This analyzer is based on Aleksi Sahala's dictionary of roots found [here](http://www.ling.helsinki.fi/~asahala/parser2.html).")
st.write("This analyzer supports both normalized and non-normalized forms.")

option = st.selectbox(
    'Please select a dialect/period. The results of your selection appear in the upper table.',
     langs)

'You selected: ', option

input_verb = st.text_input('Conjugated Verb - can be normalized or raw')
babylex_lex = Lexicon('data/babylex.csv')
lang_dict = {'Babylonian (All Periods)': 'B', 'Assyrian (All Periods)': 'Ass', 'Neo-Assyrian': 'NA',
             'Neo-Babylonian': 'NB', 'Middle Assyrian': 'MA', 'Middle Babylonian': 'MB',
             'Old Assyrian': 'OAss', 'Old Babylonian': 'OB', 'Old Akkadian': 'OAkk',
             'Mari': 'Mari', 'Nuzi': 'Nuzi'}
babylex_lex.relevant_lang = lang_dict.get(option)

# Selecting the desired segmentation for prefix + verb + suffix
segmentations_list = [['illi', 'ku'], ['illik', 'ku'], ['illik', 'u']]

# verb_segment_tuple = st.selectbox(
#     'Please select the desired segmentation to stem and affixes.', ['+'.join(tups) for tups in segmentations_list])
# is_precative = st.checkbox('Precative? Tick the box')
# segment_result = segment(input_verb, is_precative)
# if segment_result == -1:
#     st.error('Error - Precative verbs start with \'l\'')
# elif isinstance(segment_result, list):
#     segmentations_list = []


# verb_segment_list = st.selectbox(
    # 'Please select the desired segmentation to stem and affixes.', segmentations_list)

# st.markdown('**Your selection**')
# 'Prefix: ', (verb_segment_list[0] if verb_segment_list[0] != '' else '`empty`')
# 'Stem: ', (verb_segment_list[1])
# 'Suffix(es): ', (verb_segment_list[2:])
# if len(verb_segment_list[2:]) != 0:
#     st.markdown('Suffix(es): ',([segment for segment in verb_segment_list[2:]]))
# else:
#     'Suffix(es): `empty`'
# 'Suffix(es): ', (verb_segment_list[2:] if len(verb_segment_list[2:]) != 0 else '`empty`')


# relevant_result, others_result = babylex_lex.lookup_roots_segmented(input_verb)
relevant_result, others_result = babylex_lex.lookup_roots(input_verb)
#old version
# if segment_result != -1:
    # relevant_result, others_result = babylex_lex.lookup_roots(input_verb)

    # relevant_result, others_result = babylex_lex.demo(["'lk", "'ll", "nl'", "nlk", "nll"])

st.write("Most relevant results based on your selection:")
st.dataframe(relevant_result)
st.write("Other possible results from all languages/periods, based on the dictionary")
st.dataframe(others_result)