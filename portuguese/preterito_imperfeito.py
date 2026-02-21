from pt_helper_functions import *
from pt_verbs import *
from pt_rule_exceptions import *

def eu_preterito_imperfeito(infinitive):
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'ava' 
    elif(verb_ending == er or verb_ending == ir):
        conjugated_form =  verb_stem + 'ia'
    return conjugated_form  

def tu_preterito_imperfeito(infinitive):
    return eu_preterito_imperfeito(infinitive) + 's'   

def voce_ele_ela_preterito_imperfeito(infinitive): 
    return eu_preterito_imperfeito(infinitive) 

def nos_preterito_imperfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'ávamos' 
    elif(verb_ending == er or verb_ending == ir):
        conjugated_form =  verb_stem + 'íamos'
    return conjugated_form   

def vos_preterito_imperfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'áveis' 
    elif(verb_ending == er or verb_ending == ir):
        conjugated_form =  verb_stem + 'íeis'
    return conjugated_form 

def voces_eles_elas_preterito_imperfeito(infinitive): 
    return eu_preterito_imperfeito(infinitive) + 'm'  

def make_preterito_imperfeito(infinitive): 
    return (eu_preterito_imperfeito(infinitive),
            tu_preterito_imperfeito(infinitive),
            voce_ele_ela_preterito_imperfeito(infinitive),
            nos_preterito_imperfeito(infinitive),
            vos_preterito_imperfeito(infinitive),
            voces_eles_elas_preterito_imperfeito(infinitive))