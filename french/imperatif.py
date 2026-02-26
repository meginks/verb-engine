from fr_verbs import * 
from fr_helper_functions import * 
from fr_rule_exceptions import * 
from present_indicatif import *  


def tu_imperatif(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == er: 
        return verbs[infinitive][1][:-1] # minus s at end of tu form 
    elif ending == ir or ending == re:
        return verbs[infinitive][1]

def nous_imperatif(infinitive): 
    return nous_present(infinitive) 

def vous_imperatif(infinitive): 
    return vous_present(infinitive) 


def make_imperatif(infinitive): 
    return (tu_imperatif(infinitive),
            nous_imperatif(infinitive), 
            vous_imperatif(infinitive))