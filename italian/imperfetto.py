from it_helper_functions import *
from it_verbs import * 

## IMPERFETTO  

def io_imperfetto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'avo' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'evo' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'ivo' 

def tu_imperfetto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'avi' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'evi' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'ivi' 

def lui_lei_imperfetto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'ava' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'eva' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'iva' 

def noi_imperfetto(infinitive):
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'avamo' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'evamo' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'ivamo' 

def voi_imperfetto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'avate' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'evate' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'ivate' 

def loro_imperfetto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are: 
        return get_infinitive_stem(infinitive) + 'avano' 
    elif ending == ere or ending == rre: 
        return get_infinitive_stem(infinitive) + 'evano' 
    elif ending == ire:
        return get_infinitive_stem(infinitive) + 'ivano' 

# TO DO HANDLE IMPERFECT / imperfetto 
def make_imperfetto(infinitive): 
    conjugated_verb = (io_imperfetto(infinitive), 
                       tu_imperfetto(infinitive), 
                       lui_lei_imperfetto(infinitive),
                       noi_imperfetto(infinitive), 
                       voi_imperfetto(infinitive), 
                       loro_imperfetto(infinitive)) 
    return conjugated_verb   
