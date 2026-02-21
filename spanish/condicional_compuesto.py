from es_verbs import * 

# to do -- handle case of more than one past participle 

def yo_condicional_compuesto(infinitive): 
    return 'habría ' + verbs[infinitive][4][0] 

def tu_condicional_compuesto(infinitive): 
    return 'habrías ' + verbs[infinitive][4][0]

def el_ella_condicional_compuesto(infinitive): 
    return 'habría ' + verbs[infinitive][4][0]

def nosotros_condicional_compuesto(infinitive): 
    return 'habríamos ' + verbs[infinitive][4][0] 
  
def vosotros_condicional_compuesto(infinitive): 
    return 'habríais ' + verbs[infinitive][4][0] 

def ellos_condicional_compuesto(infinitive): 
    return 'habrían ' + verbs[infinitive][4][0]