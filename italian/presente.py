from it_verbs import * 
from it_helper_functions import *

## PRESENTE 

# IO 
def io_present(infinitive): 
    return verbs[infinitive][0]  

# TU 
def tu_present(infinitive): 
    return verbs[infinitive][1] 


# TO DO HANDLE EXCEPTIONS -- really should take from io stem not from infinitive stem
# LUI / LEI 
def lui_lei_present(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    conjugated_form = get_tu_stem(infinitive) 
    if verb_ending == are: 
        conjugated_form += 'a' 
    elif verb_ending == ere or verb_ending == ire: 
        conjugated_form += 'e'
    return conjugated_form

# NOI
def noi_present(infinitive): 
    return  get_infinitive_stem(infinitive)  + 'iamo' 

# VOI 
def voi_present(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return  get_infinitive_stem(infinitive)  + 'ate' 
    elif ending == ere: 
        return  get_infinitive_stem(infinitive)  + 'ete' 
    elif ending == ire: 
        return  get_infinitive_stem(infinitive)  + 'ite' 

# TO LORO 
def loro_present(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return  get_infinitive_stem(infinitive)  + 'ano' 
    elif ending == ere or ending == ire: 
        return  get_infinitive_stem(infinitive)  + 'ono' 
 


# INFINITIVE -> PRESENT 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE: TUPLE in this order (io, tu, lui / lei, noi, voi, loro)  
# presente 
def make_presente(infinitive):  
    conjugated_verb = (io_present(infinitive), 
                       tu_present(infinitive), 
                       lui_lei_present(infinitive),
                       noi_present(infinitive), 
                       voi_present(infinitive), 
                       loro_present(infinitive)) 
    return conjugated_verb  
