from es_verbs import * 
from es_helper_functions import * 
from es_subjunctive_helper import *
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



