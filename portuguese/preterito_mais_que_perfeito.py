from pt_verbs import * 
from pt_helper_functions import * 
from pt_rule_exceptions import * 

def eu_simple_preterito_mais_que_perfeito(infinitive):
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'ara' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'era'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'ira'
    return conjugated_form  

def tu_simple_preterito_mais_que_perfeito(infinitive):
    conjugated_form = eu_simple_preterito_mais_que_perfeito(infinitive) + 's'
    return conjugated_form 

def voce_ele_ela_simple_preterito_mais_que_perfeito(infinitive): 
    return eu_simple_preterito_mais_que_perfeito(infinitive)

def nos_simple_preterito_mais_que_perfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'áramos' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'éramos'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'íramos'
    return conjugated_form 

def vos_simple_preterito_mais_que_perfeito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive)  
    verb_stem = get_verb_stem(infinitive)
    conjugated_form = ''
    if (verb_ending == ar):  
        conjugated_form =  verb_stem + 'áreis' 
    elif(verb_ending == er):
        conjugated_form =  verb_stem + 'éreis'
    elif(verb_ending == ir):
        conjugated_form =  verb_stem + 'íreis'
    return conjugated_form  

def voces_eles_elas_simple_preterito_mais_que_perfeito(infinitive): 
    conjugated_form = eu_simple_preterito_mais_que_perfeito(infinitive) + 'm'  

def make_preterito_mais_que_perfeito(infinitive): 
     return (eu_simple_preterito_mais_que_perfeito(infinitive),
             tu_simple_preterito_mais_que_perfeito(infinitive),
             voce_ele_ela_simple_preterito_mais_que_perfeito(infinitive),
             nos_simple_preterito_mais_que_perfeito(infinitive),
             vos_simple_preterito_mais_que_perfeito(infinitive),
             voces_eles_elas_simple_preterito_mais_que_perfeito(infinitive))