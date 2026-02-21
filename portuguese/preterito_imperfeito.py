from pt_helper_functions import *
from pt_verbs import *
from pt_rule_exceptions import *

def eu_preterito_imperfeito(infinitive):
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'ei' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'i'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'i'
    return conjugated_form  

def tu_preterito_imperfeito(infinitive):
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'aste' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'este'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'iste'
    return conjugated_form  

def voce_ele_ela_preterito_imperfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'ou' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'eu'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'iu'
    return conjugated_form  

def nos_preterito_imperfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'amos' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'emos'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'imos'
    return conjugated_form   

def vos_preterito_imperfeito(infinitive): 
   conjugated_form = tu_preterito_imperfeito(infinitive) + 's'
   return conjugated_form  

def voces_eles_elas_preterito_imperfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'aram' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'eram'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'iram'
    return conjugated_form  

def make_preterito_imperfeito(infinitive): 
    return (eu_preterito_imperfeito(infinitive),
            tu_preterito_imperfeito(infinitive),
            voce_ele_ela_preterito_imperfeito(infinitive),
            nos_preterito_imperfeito(infinitive),
            vos_preterito_imperfeito(infinitive),
            voces_eles_elas_preterito_imperfeito(infinitive))