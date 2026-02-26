from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_futur(infinitive): 
    return get_future_stem(infinitive) + 'ai'

def tu_futur(infinitive): 
    return get_future_stem(infinitive) + 'as'

def il_elle_futur(infinitive): 
    return get_future_stem(infinitive) + 'a'

def nous_futur(infinitive): 
    return get_future_stem(infinitive) + 'ons'


def vous_futur(infinitive): 
    return get_future_stem(infinitive) + 'ez'


def ils_elles_futur(infinitive): 
    return get_future_stem(infinitive) + 'ont'  


def make_futur_indicatif(infinitive): 
    return (je_futur(infinitive),
            tu_futur(infinitive),
            il_elle_futur(infinitive),
            nous_futur(infinitive),
            vous_futur(infinitive),
            ils_elles_futur(infinitive))