from italian.it_verbs import * 
from italian.it_helper_functions import *


## PRESENTE 

def io_present(infinitive): 
    return verbs[infinitive][0]  

def tu_present(infinitive): 
    return verbs[infinitive][1] 


# TO DO HANDLE EXCEPTIONS -- really should take from io stem not from infinitive stem
def lui_lei_present(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    conjugated_form = get_tu_stem(infinitive) 
    if verb_ending == 'are': 
        conjugated_form += 'a' 
    elif verb_ending == 'ere' or verb_ending == 'ire': 
        conjugated_form += 'e'
    return conjugated_form

# TO DO HANDLE NOI
def noi_present(infinitive): 
    return verbs[infinitive][1] + 'amo' 

# TO DO HANDLE VOI 
def voi_present(infinitive): 
    return verbs[infinitive][1] + 'ete' 

# TO DO HANDLE LORO 
def loro_present(infinitive): 
    return verbs[infinitive][0] + 'no'


########### CONGIUNTIVO #########################
## TO DO ## 
## CONGIUNTIVO PRESENTE 

def io_tu_lui_lei_congiuntivo_presente(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    conjugated_form = get_tu_stem(infinitive) 
    if verb_ending == 'are': 
        conjugated_form += 'i' 
    elif verb_ending == 'ere' or verb_ending == 'ire': 
        conjugated_form += 'a'
    return conjugated_form

# TO DO HANDLE NOI
def noi_congiuntivo_presente(infinitive): 
    return 

# TO DO HANDLE VOI 
def voi_congiuntivo_presente(infinitive): 
    return 

# TO DO HANDLE LORO 
def loro_congiuntivo_presente(infinitive): 
    return 