from it_verbs import * 
from it_helper_functions import *


# INFINITIVE -> PRESENT 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE: TUPLE in this order (io, tu, lui / lei, noi, voi, loro)  
# presente 
def make_present(infinitive):  
    conjugated_verb = (io_present(infinitive), 
                       tu_present(infinitive), 
                       lui_lei_present(infinitive),
                       noi_present(infinitive), 
                       voi_present(infinitive), 
                       loro_present(infinitive)) 
    return conjugated_verb  


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
