from spanish.es_helper_functions import * 


# yo, el, ella, usted in conditional 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def yo_el_condicional(infinitive): 
    return get_future_cond_stem(infinitive) + 'ía' 

# tú in conditional 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_condicional(infinitive): 
   return yo_el_condicional(infinitive) + 's'

# nosotros / nosotras in conditional 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def nosotros_condicional(infinitive): 
    return yo_el_condicional(infinitive) + 'mos'

# vosotros / vosotras in conditional 
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def vosotros_condicional(infinitive): 
    return yo_el_condicional(infinitive) + 'is'

# ellos / ellas / ustedes in conditional  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_condicional(infinitive): 
      return yo_el_condicional(infinitive) + 'n'
