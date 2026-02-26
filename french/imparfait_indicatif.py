from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import * 

def je_imparfait_indicatif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'ais' 

def tu_imparfait_indicatif(infinitive): 
     return je_imparfait_indicatif(infinitive)

def il_elle_imparfait_indicatif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'ait' 

def nous_imparfait_indicatif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'ions' 

def vous_imparfait_indicatif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'iez' 

def ils_elles_imparfait_indicatif(infinitive): 
    return get_third_person_plural_present_stem(infinitive) + 'aient' 

def make_imparfait_indicatif(infinitive): 
    return (je_imparfait_indicatif(infinitive),
            tu_imparfait_indicatif(infinitive), 
            il_elle_imparfait_indicatif(infinitive),
            nous_imparfait_indicatif(infinitive), 
            vous_imparfait_indicatif(infinitive),
            ils_elles_imparfait_indicatif(infinitive))