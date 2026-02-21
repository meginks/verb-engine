from spanish.es_verbs import * 
from spanish.es_helper_functions import * 
from spanish.es_subjunctive_helper import * 

################ IMPERFECTO ##############################

# yo, el, ella, usted in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def yo_el_imperfecto(infinitive):
    verb_ending = get_infinitive_ending(infinitive) 
    verb_stem = get_infinitive_stem(infinitive) 
    if infinitive in imperfect_exceptions: 
        conjugated_form = imperfect_exceptions[infinitive] 
    else: 
        if verb_ending == 'ar': 
            conjugated_form = verb_stem + 'aba' 
        elif verb_ending == 'er' or 'ir': 
            conjugated_form = verb_stem + 'ía' 
    return conjugated_form  


# tú in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 's'  

# nosotros, nosotras in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def nosotros_imperfecto(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    if infinitive in imperfect_exceptions: 
        conjugated_form = imperfect_exceptions_nos[infinitive] 
    else: 
        verb_stem = get_infinitive_stem(infinitive)
        if verb_ending == 'ar': 
            conjugated_form = verb_stem + 'ábamos' 
        elif verb_ending == 'er' or 'ir': 
            conjugated_form = verb_stem + 'íamos' 
    return conjugated_form 

# vosotros / vosotras in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def vosotros_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 'is' 

# ellos / ellas / ustedes in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 'n' 