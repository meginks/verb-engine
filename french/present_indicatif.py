from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_present(infinitive): 
    return verbs[infinitive][0] 

def tu_present(infinitive): 
    return verbs[infinitive][1] 

def il_elle_present(infinitive): 
    verb_stem = get_verb_stem(infinitive)
    ending = get_infinitive_ending(infinitive) 
    if  ending == er: 
        return verb_stem + 'e'
    elif ending == ir: 
        return verb_stem + 'it'
    elif ending == re:
        return verb_stem 

def nous_present(infinitive): 
    verb_stem = get_verb_stem(infinitive)
    ending = get_infinitive_ending(infinitive) 
    if  ending == er or ending == re: 
        return verb_stem + 'ons'
    elif ending == ir: 
        return verb_stem + 'issons'

def vous_present(infinitive): 
    verb_stem = get_verb_stem(infinitive)
    ending = get_infinitive_ending(infinitive) 
    if  ending == er or ending == re: 
        return verb_stem + 'ez'
    elif ending == ir: 
        return verb_stem + 'issez'


def ils_elles_present(infinitive): 
    verb_stem = get_verb_stem(infinitive)
    ending = get_infinitive_ending(infinitive) 
    if  ending == er or ending == re: 
        return verb_stem + 'ent'
    elif ending == ir: 
        return verb_stem + 'issent'
    
    
def make_present_indicatif(infinitive): 
    return (je_present(infinitive),
            tu_present(infinitive), 
            il_elle_present(infinitive),
            nous_present(infinitive), 
            vous_present(infinitive),
            ils_elles_present(infinitive))