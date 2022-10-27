# akkadian-form-analyzer

This program takes the vocabulary from http://www.ling.helsinki.fi/~asahala/parser2.html , converts it to a csv file and then analyzes a conjugated form of a verb 
in Babylonian (and other related languages, see details below). The output of the analysis is a table of ALL the possible roots for the conjugated verb, along with their 
meaning, the relevant languages for that meaning, the infinitive form (if exists) and the class as specified in the dictionary. 
The analyzer supports both normalized and non-normalized writings.

The analysis is done top-down, so that many options are generated and then filtered, thus supporting quadrical, weak and double-weak roots that are generally 
harder to analyze in a bottom-up way.

Future Plans:
Suggest analysis by stem + suffix
Support for nouns and adjectives
Add morphological features (gender, number, person) to the output
