from portuguese.pt_verbs import * 
from portuguese.pt_helper_functions import *  

# verb endings 
er = 'er' 
ar = 'ar' 
ir = 'ir' 

def present_eu(infinitive): 
    return verbs[infinitive][0]

def present_tu(infinitive): 
    return verbs[infinitive][1] 


def present_ele_ela_voce(infinitive):
    conjugated_form = verbs[infinitive][1][:-1] 
    return conjugated_form 

def present_nos(infinitive): 
    conjugated_form = infinitive[:-1] + 'mos' 
    return conjugated_form 

def present_vos(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    if (verb_ending == ar or verb_ending == er):  
        conjugated_form =  infinitive[:-1] + 'is' 
    elif(verb_ending == ir): 
        conjugated_form =  infinitive[:-1] + 's'
    return conjugated_form 

def present_eles_elas_voces(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    verb_stem = get_verb_stem(infinitive) 
    if (verb_ending == ir or verb_ending == er):  
        conjugated_form =  verb_stem + 'em' 
    elif(verb_ending == ar): 
        conjugated_form =  verb_stem + 'm'
    return conjugated_form 