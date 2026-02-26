from spanish.es_rule_exceptions import * 
from spanish.es_verbs import *  
import ellos_preterito 
# from past_tense import ellos_preterito 

############################## HELPER METHODS ##################################
def get_infinitive_ending(infinitive): 
    last_2_char = infinitive[-2:] 
    if (last_2_char == 'se'): # handle the case of reflexive infinitives (e.g. sentarse)
        return infinitive[-4:-2]; 
    else: 
        return last_2_char  

def get_infinitive_stem(infinitive): 
    if (infinitive[-2:] == 'se'): 
        infinitive_stem = infinitive[:-4] 
    else: 
        infinitive_stem = infinitive[:-2] 
    return infinitive_stem 


def get_future_cond_stem(infinitive): 
    if infinitive in future_cond_exceptions: 
        return future_cond_exceptions[infinitive]
    else: 
        return get_infinitive_stem(infinitive) 

def get_preterite_stem(infinitive): 
    if infinitive in verbs: 
        preterite_form = verbs[infinitive][2] 
        return preterite_form[:-1]

# TO DO 
def get_infinitive_minus_r(infinitive): 
    return  

# TO DO 
# make sure to handle cases where yo present form ends in -oy (-oy should be removed to form yo stem)
def get_yo_stem(infinitive): 
    return  


def get_3_pers_pl_preterite_stem(infinitive): 
    third_pers_pl_preterite = ellos_preterito(infinitive) 
    return third_pers_pl_preterite[:-2] 