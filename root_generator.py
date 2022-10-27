import pandas as pd
import itertools
from config import *


def segment(input_verb, is_precative):
    if is_precative:
        if not input_verb.startswith('l'):
            return -1


def generate_stem_suffix_dic(conjugated_verb):
    all_substrings = [conjugated_verb[i: j] for i in range(len(conjugated_verb))
           for j in range(i + 1, len(conjugated_verb) + 1)]

    stem_suffix_dic = {}
    # Step 0: insert conjugated verb to dictionary with no suffix
    stem_suffix_dic[conjugated_verb] = []

    # Case 1: two suffixes, the last one is 'ma'
    if conjugated_verb.endswith('ma'):
        ma_verb_dict = generate_stem_suffix_dic(conjugated_verb[:-2])
        for value in ma_verb_dict.values():
            value.append('ma')
        stem_suffix_dic.update(ma_verb_dict)

    # Case 2 : one suffix
    else:
        for sub in all_substrings:
            sublen = len(sub)
            suffixes_l = []
            if conjugated_verb.endswith(sub):
                stem = conjugated_verb[:-(sublen)]
                suff = conjugated_verb[-(sublen):]
                if suff in suffixes:
                    suffixes_l.append(suff)
                    stem_suffix_dic[stem] = suffixes_l

    # print(stem_suffix_dic)
    return stem_suffix_dic


def generate_combinations(radicals_str):
    list_of_combinations = []
    if len(radicals_str) == 3:
        list_of_combinations.append(radicals_str)
    if len(radicals_str) == 4:
        roots_combinations = [''.join(x) for x in itertools.combinations_with_replacement(radicals_str, 3)]
        list_of_combinations.extend(roots_combinations)
        list_of_combinations.append(radicals_str)
    else:
        roots_combinations4 = [''.join(x) for x in itertools.combinations_with_replacement(radicals_str, 4)]
        list_of_combinations.extend(roots_combinations4)
        roots_combinations3 = [''.join(x) for x in itertools.combinations_with_replacement(radicals_str, 3)]
        list_of_combinations.extend(roots_combinations3)

    return list_of_combinations


def extract_possible_roots_from_dict(conjugated_verb):
    root_list = []
    if '-' in conjugated_verb:
        conjugated_verb = conjugated_verb.replace('-', '')

    stem_suff_dict = generate_stem_suffix_dic(conjugated_verb)
    print(stem_suff_dict)
    for key in stem_suff_dict:
        suffix = stem_suff_dict[key]
        tmp_root_list = extract_possible_roots(key)
        # filtered_roots_list = filter_roots_list(tmp_root_list, key, suffix)
        root_list.extend(tmp_root_list)
        # print(key, suffix)

    root_set = set(root_list)
    unique_root_list = list(root_set)
    # print(unique_root_list)
    return unique_root_list


def extract_possible_roots(conjugated_verb):

    roots_list = []
    if len(conjugated_verb) == 0:
        return roots_list

    if '-' in conjugated_verb:
        conjugated_verb = conjugated_verb.replace('-', '')

    # Step 1: Split stem from longest possible suffix
    # generate_stem_suffix_dic(conjugated_verb)
    # possible_stem, longest_possible_suffix = strip_suffixes(conjugated_verb)

    # Step 2: remove remaining vowels
    consonantal_verb_str = conjugated_verb.translate({ord(vowel): None for vowel in vowels})
    # print("HI!", consonantal_verb_str)
    if len(consonantal_verb_str) == 3:
        roots_list.append(consonantal_verb_str)
    # print(consonantal_verb_str)
    # Step 3: "Abusing" the consonantal_verb_str
    # Step 3.1: Generating all the possible roots from a unique set of radicals (no radical appears twice, e.g.
    # for 'ustapris' root_no_duplicates = ['s', 't', 'p', 'r']

    sep = ''

    root_no_duplicates = list(dict.fromkeys(consonantal_verb_str))
    # print(root_no_duplicates)
    undup_root = sep.join(root_no_duplicates)
    roots_list.extend(generate_combinations(undup_root))

    # Step 3.2: Transform the first two consecutive characters XX into nX, and then generate all the possible roots
    # from the unique set of characters including 'n'
    # if consonantal_verb_str[0] == consonantal_verb_str[1]:
    consonantal_verb_adds = "nw'" + consonantal_verb_str + "nw'"
    # print(consonantal_verb_adds)
        # root_no_duplicates_In = list(dict.fromkeys(consonantal_verb_In))
        # undup_root_In = sep.join(root_no_duplicates_In)
    roots_list.extend(generate_combinations(consonantal_verb_adds))

    # Step 4: check if the first consonant is indifferent, if so proceed to extract all remaining
    tmp_root = ''
    if consonantal_verb_str[0] in indifferent_consonants:
        tmp_root += consonantal_verb_str[0]
        # print("first letter of root = ", tmp_root)
        for letter in consonantal_verb_str[1:]:
            if letter in (indifferent_consonants + participating_consonants):
                tmp_root += letter
                # print("another root letter = ", tmp_root)

    roots_list.extend(generate_combinations(tmp_root))

    # Step 5.1: use complete consonantal_verb_str with the duplicates, add I-n I-w I-aleph
    radicals_with_dups_list = []
    consonantal_verb_n_str = 'n' + consonantal_verb_str
    consonantal_verb_w_str = 'w' + consonantal_verb_str
    consonantal_verb_aleph_str = "'" + consonantal_verb_str
    # print(consonantal_verb_aleph_str)

    # Addition: insert ' inside consonantal verb
    aleph_insterted_roots = []
    for i in range(0, len(consonantal_verb_str)):
        consonantal_verb_str_with_aleph = consonantal_verb_str[i] + "'" + consonantal_verb_str[i+1:]
        aleph_insterted_roots.append(consonantal_verb_str_with_aleph)

    roots_combinations_n = [''.join(x) for x in itertools.combinations_with_replacement(consonantal_verb_n_str, 5)]
    roots_combinations_w = [''.join(x) for x in itertools.combinations_with_replacement(consonantal_verb_w_str, 5)]
    roots_combinations_aleph = [''.join(x) for x in itertools.combinations_with_replacement(consonantal_verb_aleph_str, 5)]
    roots_combinations = roots_combinations_n + roots_combinations_w + roots_combinations_aleph + aleph_insterted_roots

    for root in roots_combinations:
        radicals_with_dups_list.extend(generate_combinations(root))
        # print(radicals_with_dups_list)
    roots_list.extend(radicals_with_dups_list)
    # print(roots_list)
    # Step 6: strip consonantal_verb_str of all participating characters and add weak consonants
    # Note that consonantal_verb_no_participating_list can contain duplicates

    # Step 6.1 : no duplicates scenario:
    weak_no_dup_root_list = []
    consonantal_verb_no_participating_list = [i for i in list(consonantal_verb_str) if i not in participating_consonants]
    consonantal_verb_no_participating_str = sep.join(consonantal_verb_no_participating_list)
    root_no_duplicates_noparticip_list = list(dict.fromkeys(consonantal_verb_no_participating_str))
    root_no_duplicates_noparticip_str = sep.join(root_no_duplicates_noparticip_list)
    if len(root_no_duplicates_noparticip_list) == 1:
        doubleweak_aleph1 = "''" + root_no_duplicates_noparticip_str
        doubleweak_aleph2 = "'" + root_no_duplicates_noparticip_str + "'"
        doubleweak_aleph3 = root_no_duplicates_noparticip_str + "''"

        doubleweak_na1 = "n'" + root_no_duplicates_noparticip_str
        doubleweak_na11 = "'n" + root_no_duplicates_noparticip_str
        doubleweak_na2 = "n" + root_no_duplicates_noparticip_str + "'"
        doubleweak_na22 = "'" + root_no_duplicates_noparticip_str + "n"
        doubleweak_na3 = root_no_duplicates_noparticip_str + "n'"
        doubleweak_na33 = root_no_duplicates_noparticip_str + "'n"
        weak_no_dup_root_list.extend([doubleweak_aleph1, doubleweak_aleph2, doubleweak_aleph3,
                                      doubleweak_na1, doubleweak_na11, doubleweak_na2,
                                      doubleweak_na22, doubleweak_na3, doubleweak_na33])

    else:
        weak_aleph1 = "'" + root_no_duplicates_noparticip_str
        weak_aleph2 = root_no_duplicates_noparticip_str + "'"

        weak_n1 = "n" + root_no_duplicates_noparticip_str
        weak_w1 = "w" + root_no_duplicates_noparticip_str

        weak_no_dup_root_list.extend([weak_aleph1, weak_aleph2, weak_n1, weak_w1])

    weak_roots = []
    for root in weak_no_dup_root_list:
        weak_roots.extend(generate_combinations(root))

    roots_list.extend(weak_roots)

    # Step 7: handling alternations
    potentially_problematic_suffixes = ('su', 'si', 'sum', 'sim', 'sunūti', 'sināti', 'sunūšim', 'sināšim')

    dental_cons_adds = []
    if conjugated_verb.endswith(potentially_problematic_suffixes):
        for dental in dentals:
            dental_cons_adds.append((consonantal_verb_str + dental))

    assimilated_roots = []
    for root in dental_cons_adds:
        assimilated_roots.extend(generate_combinations(root))
    roots_list.extend(assimilated_roots)

    # print(roots_list)
    return roots_list


def filter_roots_list(roots_list, stem, suffix):
    stem_cons = [char for char in stem if char in indifferent_consonants]
    for root in roots_list:
        for char in stem_cons:
            if char not in list(root):
                roots_list.remove(root)

    return roots_list


# New version for filter_roots
def filter_roots(roots_df, conj_verb):
    # consonantal_verb_list is just the consonants by relative order, including duplicates
    consonantal_verb_list = list(conj_verb.translate({ord(vowel): None for vowel in vowels}))
    if "'" not in conj_verb:
        filtered_roots_df = roots_df[~roots_df['root'].str.contains("'")]

    return filtered_roots_df

# def filter_roots(roots_df, conj_verb):
#
#     conj_verbs_cons = [char for char in conj_verb if char in indifferent_consonants]
#     # print(conj_verbs_cons)
#     ixs_to_remove = []
#     # print(conj_verbs_cons[1:])
#     for ix in roots_df.index:
#         root = roots_df.at[ix, 'root']
#         for char in conj_verbs_cons:
#             if char not in list(root):
#                 ixs_to_remove.append(ix)
#                 # print(root)
#         if ('š' in conj_verb[1:]) and ('š' not in list(root)):
#             ixs_to_remove.append(ix)
#
#         if conj_verb.endswith('n') and ('n' != list(root)[-1]):
#             ixs_to_remove.append(ix)
#
#         if conj_verb.endswith('s') and ('s' != list(root)[-1]):
#             ixs_to_remove.append(ix)
#
#     filtered_roots_df = roots_df.drop(ixs_to_remove)
#     return filtered_roots_df
