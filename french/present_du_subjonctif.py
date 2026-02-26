from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_present_du_subjonctif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'e' 

def tu_present_du_subjonctif(infinitive): 
     return get_third_person_plural_present_stem(infinitive) + 'es' 

def il_elle_present_du_subjonctif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'e' 

def nous_present_du_subjonctif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'ions' 

def vous_present_du_subjonctif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'iez' 


def ils_elles_present_du_subjonctif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'ent' 

def make_present_du_subjonctif(infinitive): 
    return (je_present_du_subjonctif(infinitive),
            tu_present_du_subjonctif(infinitive), 
            il_elle_present_du_subjonctif(infinitive),
            nous_present_du_subjonctif(infinitive), 
            vous_present_du_subjonctif(infinitive),
            ils_elles_present_du_subjonctif(infinitive))