from spanish.es_verbs import * 
from spanish.es_helper_functions import * 

# el, ella, usted in present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def el_present(infinitive): 
    second_person_present = verbs[infinitive][1]  
    conjugated_form = second_person_present[:-1] # formed by removing the -S from the second person 
    return conjugated_form 

#  nosotros / nosotras in present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def nosotros_present(infinitive): 
    second_person_present = verbs[infinitive][1]  
    verb_ending = get_infinitive_ending(infinitive)
    if verb_ending == 'ar': 
        conjugated_form = second_person_present[:-2] + 'amos'  
    elif verb_ending == 'ir': 
        conjugated_form = second_person_present[:-2] + 'imos' 
    elif verb_ending == 'er':
        conjugated_form = second_person_present[:-2] + 'emos' 
    return conjugated_form 


# vosotros / vosotras in present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form    
def vosotros_present(infinitive): 
    second_person_present = verbs[infinitive][1]  
    verb_ending = get_infinitive_ending(infinitive)
    if verb_ending == 'ar': 
        conjugated_form = second_person_present[:-2] + 'áis'  
    elif verb_ending == 'ir': 
        conjugated_form = second_person_present[:-2] + 'ís' 
    elif verb_ending == 'er':
        conjugated_form = second_person_present[:-2] + 'éis' 
    return conjugated_form 


# ellos / ellas / ustedes in present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def ellos_present(infinitive): 
    conjugated_form = el_present(infinitive) + 'n' # third person in present + n 
    return conjugated_form


# SUBJUNTIVO / SUBJUNCTIVE 
## TO DO -- handle exceptions 

# yo, él, ella and usted in subjunctive present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def yo_el_subjuntivo_presente(infinitive): 
    yo_stem = get_yo_stem(infinitive) 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = yo_stem + 'e'
    elif verb_ending == 'er' or verb_ending == 'ir': 
        conjugated_form = yo_stem + 'a'
    return conjugated_form 

# tú in subjunctive present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def tu_subjuntivo_presente(infinitive): 
    conjugated_form = yo_el_subjuntivo_presente(infinitive) + 's'
    return conjugated_form


# nosotros / nosotras in subjunctive present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def nosotros_subjuntivo_presente(infinitive): 
    conjugated_form =  yo_el_subjuntivo_presente(infinitive) + 'mos'
    return conjugated_form

# vosotros / vosotras in subjunctive present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def vosotros_subjuntivo_presente(infinitive): 
    yo_stem = get_yo_stem(infinitive) 
    verb_ending = get_infinitive_ending(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = yo_stem + 'éis'
    elif verb_ending == 'er' or verb_ending == 'ir': 
        conjugated_form = yo_stem + 'áis'
    return conjugated_form 

# ellos / ellas / ustedes in subjunctive present 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def ellos_subjuntivo_presente(infinitive): 
    conjugated_form =  yo_el_subjuntivo_presente(infinitive) + 'n'
    return conjugated_form