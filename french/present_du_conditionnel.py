from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'ais'

def tu_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'ais'

def il_elle_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'ait'

def nous_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'ions'

def vous_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'iez'

def ils_elles_conditionnel(infinitive): 
    return get_future_stem(infinitive) + 'aient'  

def make_present_du_conditionnel(infinitive): 
    return (je_conditionnel(infinitive),
            tu_conditionnel(infinitive),
            il_elle_conditionnel(infinitive),
            nous_conditionnel(infinitive),
            vous_conditionnel(infinitive),
            ils_elles_conditionnel(infinitive))