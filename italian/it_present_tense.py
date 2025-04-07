from italian.it_verbs import * 
from italian.it_helper_functions import *

def io_present(infinitive): 
    return verbs[infinitive][0]  

def tu_present(infinitive): 
    return verbs[infinitive][1] 


# TO DO HANDLE EXCEPTIONS -- really should take from io stem not from infinitive stem
def lui_lei_present(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    conjugated_form = get_infinitive_stem(infinitive) 
    if verb_ending == 'are': 
        conjugated_form += 'a' 
    elif verb_ending == 'ere' or verb_ending == 'ire': 
        conjugated_form += 'e'
    return conjugated_form

# TO DO HANDLE NOI
def noi_present(infinitive): 
    return '' 

# TO DO HANDLE VOI 
def voi_present(infinitive): 
    return '' 

# TO DO HANDLE LORO 
def loro_present(infinitive): 
    return '' 


########### CONGIUNTIVO #########################
## TO DO ## 
## congiuntivo presente 