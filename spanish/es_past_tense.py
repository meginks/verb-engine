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

################### PRETERITO ######################## 

# tú in preterite 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_preterito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = get_preterite_stem(infinitive) + 'aste' 
    elif verb_ending == 'ir' or verb_ending == 'er': 
         conjugated_form = get_preterite_stem(infinitive) + 'iste' 
    return conjugated_form 

# él / ella / usted in preterite 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def el_preterito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = get_preterite_stem(infinitive) + 'ó' 
    elif verb_ending == 'ir' or verb_ending == 'er': 
         conjugated_form = get_preterite_stem(infinitive) + 'ió' 
    return conjugated_form  

# nosotros / nosotras in preterite 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def nosotros_preterito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = get_preterite_stem(infinitive) + 'amos' 
    elif verb_ending == 'ir' or verb_ending == 'er': 
         conjugated_form = get_preterite_stem(infinitive) + 'imos' 
    return conjugated_form 

# vosotros / vosotras in preterite 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def vosotros_preterito(infinitive): 
    conjugated_form = tu_preterito(infinitive) + 'is' 
    return conjugated_form 

# ellos / ellas / ustedes in preterite 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_preterito(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = get_preterite_stem(infinitive) + 'aron' 
    elif verb_ending == 'ir' or verb_ending == 'er': 
         conjugated_form = get_preterite_stem(infinitive) + 'ieron' 
    return conjugated_form 

################# SUBJUNTIVO ########################## 

# yo, el, ella, usted in imperfect subjunctive 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def yo_el_subjuntivo_pasado(infinitive): 
    conjugated_form = get_3_pers_pl_preterite_stem(infinitive) + 'a'
    return conjugated_form 

# tú in imperfect subjunctive 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_subjuntivo_pasado(infinitive): 
    conjugated_form = yo_el_subjuntivo_pasado(infinitive) + 's'
    return conjugated_form 

# nosotros / nosotras in imperfect subjunctive 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def nosotros_subjuntivo_pasado(infinitive):  
    # MIGHT NEED TO ADJUST THIS FOR ACCENT MARK PURPOSES 
    conjugated_form = yo_el_subjuntivo_pasado(infinitive) + 'amos'
    return conjugated_form 

# vosotros / vosotras in imperfect subjunctive 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def vosotros_subjuntivo_pasado(infinitive): 
    conjugated_form = yo_el_subjuntivo_pasado(infinitive) + 'n' 
    return conjugated_form 

# ellos / ellas / ustedes in imperfect subjunctive 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_subjuntivo_pasado(infinitive): 
    conjugated_form = '' 
    return conjugated_form  



