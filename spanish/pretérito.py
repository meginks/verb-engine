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
