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