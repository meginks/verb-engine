from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  
from passe_simple import *

def je_imparfait_du_subjonctif(infinitive): 
    return je_passe_simple(infinitive) + 'sse'

def tu_imparfait_du_subjonctif(infinitive): 
    return je_passe_simple(infinitive) + 'sses'

def il_elle_imparfait_du_subjonctif(infinitive): 
    passe_simple = je_passe_simple(infinitive) 
    ending = get_infinitive_ending(infinitive)
    if ending == er: 
        return passe_simple[:-1] + 'ât'
    elif ending == ir or ending == re: 
        return passe_simple[:-1] + 'ît' 

def nous_imparfait_du_subjonctif(infinitive): 
     return je_passe_simple(infinitive) + 'ssions'

def vous_imparfait_du_subjonctif(infinitive): 
    return je_passe_simple(infinitive) + 'ssiez'

def ils_elles_imparfait_du_subjonctif(infinitive): 
    return je_passe_simple(infinitive) + 'ssent' 


def make_imparfait_du_subjonctif(infinitive): 
    return (je_imparfait_du_subjonctif(infinitive),
            tu_imparfait_du_subjonctif(infinitive), 
            il_elle_imparfait_du_subjonctif(infinitive),
            nous_imparfait_du_subjonctif(infinitive), 
            vous_imparfait_du_subjonctif(infinitive),
            ils_elles_imparfait_du_subjonctif(infinitive))