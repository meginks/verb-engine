from spanish.es_helper_functions import * 
from spanish.es_verbs import * 

## TO DO across file -- incorporate exceptions 

#imperative gotchas 
# nosotros imperative doesn't change spelling unless it's an IR verb 
# stem changes and spelling changes in general 


# make tú form of imperative (positive)
# PARAMETER : STRING tu present form 
# RETURN TYPE: STRING conjugated form  
def make_tu_imperative(tu_present): 
    conjugated_form =  tu_present[:-1] # present tense tú form minus 's'
    return conjugated_form  


# TO DO -- handle irregular cases here (estoy --> este and c--> qu / g--> gu / z --> c spelling shifts)
# make tú form of imperative (negative)
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def make_tu_negative_imperative(infinitive): 
    yo_stem = get_yo_stem(infinitive)
    verb_ending = get_infinitive_ending(infinitive)
    if (verb_ending == 'er' or verb_ending == 'ir'):
        conjugated_form = yo_stem + 'as' 
    elif verb_ending == 'ar': 
        conjugated_form = yo_stem + 'es' 
    return 'no ' + conjugated_form


# make usted form of imperative 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
# TO DO -- handle irregular cases here (estoy --> este and c--> qu / g--> gu / z --> c spelling shifts)
def make_usted_imperative(infinitive): 
    yo_stem = get_yo_stem(infinitive)
    verb_ending = get_infinitive_ending(infinitive)
    if (verb_ending == 'er' or verb_ending == 'ir'):
        conjugated_form = yo_stem + 'a' 
    elif verb_ending == 'ar': 
        conjugated_form = yo_stem + 'e' 
    return 'no ' + conjugated_form 


# make ustedes form of imperative 
# PARAMETER : STRING usted imperative form 
# RETURN TYPE: STRING conjugated form  
def make_ustedes_imperative(usted_imperative_form): 
    return usted_imperative_form + 'n'  


# make vosotros form of imperative (positive & non-reflexive)
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def make_vosotros_imperative_positive(infinitive): 
    infinitive_minus_r = get_infinitive_minus_r(infinitive) 
    return infinitive_minus_r + 'd'

# make vosotros form of imperative (positive & reflexive)
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def make_vosotros_imperative_positive_reflexive(infinitive): 
    infinitive_minus_r = get_infinitive_minus_r(infinitive) 
    return infinitive_minus_r + 'os' 

def make_vosotros_imperative_negative(infinitive): 
    yo_stem = get_yo_stem(infinitive) 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = yo_stem + 'éis' 
    elif verb_ending == 'er' or verb_ending == 'ir': 
        conjugated_form = yo_stem + 'áis' 
    return 'no ' + conjugated_form 

def make_nosotros_imperative(infinitive): 
    yo_stem = get_yo_stem(infinitive) 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = yo_stem + 'emos'
    elif verb_ending == 'er' or verb_ending == 'ir': 
        conjugated_form = yo_stem + 'amos' 
    return conjugated_form 