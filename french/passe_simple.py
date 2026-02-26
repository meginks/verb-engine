from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'ai' 
    elif ending == ir or ending == re: 
        return stem + 'is'

def tu_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'as' 
    elif ending == ir or ending == re: 
        return stem + 'is'

def il_elle_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'a' 
    elif ending == ir or ending == re: 
        return stem + 'it'

def nous_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'âmes' 
    elif ending == ir or ending == re: 
        return stem + 'îmes'

def vous_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'âtes' 
    elif ending == ir or ending == re: 
        return stem + 'îtes'

def ils_elles_passe_simple(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_verb_stem(infinitive) 
    if ending == er: 
        return stem + 'èrent' 
    elif ending == ir or ending == re: 
        return stem + 'irent' 
    
def make_passe_simple(infinitive): 
    return (je_passe_simple(infinitive),
            tu_passe_simple(infinitive),
            il_elle_passe_simple(infinitive),
            nous_passe_simple(infinitive),
            vous_passe_simple(infinitive),
            ils_elles_passe_simple(infinitive)) 