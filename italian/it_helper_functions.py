

############# HELPER METHODS ########### 
def get_infinitive_ending(infinitive): 
    last_3_char = infinitive[-3:] 
    if (last_3_char == 'si'): # handle the case of reflexive infinitives
        return infinitive[-4:-2] + 'e' # return 'are' / 'ire' / 'ere' 
    else: 
        return last_3_char  
    

def get_infinitive_stem(infinitive): 
    if (infinitive[-2:] == 'si'): 
        infinitive_stem = infinitive[:-4] 
    else: 
        infinitive_stem = infinitive[:-3] 
    return infinitive_stem 
