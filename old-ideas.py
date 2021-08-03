def strip_suffixes(conjugated_verb):
    suggested_suffix = ''

    if conjugated_verb.endswith(('ka', 'ki', 'šu', 'ši', 'am', 'im', 'ma')):
        suggested_suffix = conjugated_verb[-2:]
        conjugated_verb = conjugated_verb[:-2]

    elif conjugated_verb.endswith(('kum', 'kim', 'šum', 'šim', 'nim')):
        suggested_suffix = conjugated_verb[-3:]
        conjugated_verb = conjugated_verb[:-3]

    elif conjugated_verb.endswith(('anni', 'īnni', 'inni')):
        suggested_suffix = conjugated_verb[-4:]
        conjugated_verb = conjugated_verb[:-4]

    elif conjugated_verb.endswith(('niāti', 'ninni', 'niati')):
        suggested_suffix = conjugated_verb[-5:]
        conjugated_verb = conjugated_verb[:-5]

    elif conjugated_verb.endswith(('kunūti', 'kināti', 'šunūti', 'šināti', 'niāšim',
                                   'kunuti', 'kinati', 'šunuti', 'šinati', 'niašim')):
        suggested_suffix = conjugated_verb[-6:]
        conjugated_verb = conjugated_verb[:-6]

    elif conjugated_verb.endswith(('kunūšim', 'kināšim', 'šunūšim', 'šināšim',
                                   'kunušim', 'kinašim', 'šunušim', 'šinašim')):
        suggested_suffix = conjugated_verb[-7:]
        conjugated_verb = conjugated_verb[:-7]

    return conjugated_verb, suggested_suffix