from spanish.es_helper_functions import * 

##################### FUTURE ############################
# yo in future   
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def yo_futuro(infinitive): 
    return get_future_cond_stem(infinitive) + 'é'

# tú in future 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_futuro(infinitive): 
   return el_futuro(infinitive) + 's'

# el, ella, usted in future 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def el_futuro(infinitive): 
    return get_future_cond_stem(infinitive) + 'á'

# nosotros / nosotras in future 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def nosotros_futuro(infinitive): 
    return get_future_cond_stem(infinitive) + 'emos'

# vosotros / vosotras in future 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def vosotros_futuro(infinitive): 
    return yo_futuro(infinitive) + 'is'

# ellos / ellas / ustedes in future 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_futuro(infinitive): 
    return el_futuro(infinitive) + 'n'

##################### FUTURE PERFECT ########################