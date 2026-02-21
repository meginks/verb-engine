from pt_verbs import *
from preterito_imperfeito import * 
# verb endings 
er = 'er' 
ar = 'ar' 
ir = 'ir' 

def get_infinitive_ending(infinitive): 
    last_2_char = infinitive[-2:] 
    if (last_2_char == 'se'): # handle the case of reflexive infinitives remove '-se' and return the ar/er/ir ending
        return infinitive[-5:-3]; 
    else: 
        return last_2_char  
    
def get_verb_stem(infinitive): 
    if (infinitive[-3:] == '-se'): 
        verb_stem = infinitive[:-5] 
    else: 
        verb_stem = infinitive[:-2] 
    return verb_stem 

def get_first_person_singular_stem(infinitive): 
    return verbs[infinitive][0][:-1]

def get_third_person_plural_preterite_stem(infinitive): 
    return voces_eles_elas_preterito_imperfeito(infinitive)[:-3]
