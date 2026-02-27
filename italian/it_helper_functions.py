from it_verbs import *
from presente import * 

are = 'are' 
ire = 'ire' 
ere = 'ere' 
rre = 'rre'
avere = 'avere' 
essere = 'essere' 


############# HELPER METHODS ###########  

def get_infinitive_ending(infinitive): 
    last_3_char = infinitive[-3:] 
    if (last_3_char == 'rsi'): # handle the case of reflexive infinitives
        return infinitive[-4:-2] + 'e' # return 'are' / 'ire' / 'ere' 
    else: 
        return last_3_char  
    

def get_infinitive_stem(infinitive): 
    if (infinitive[-2:] == 'si'): 
        infinitive_stem = infinitive[:-4] 
    else: 
        infinitive_stem = infinitive[:-3] 
    return infinitive_stem 

def get_io_stem(infinitive): 
    return verbs[infinitive][0][:-1]  

def get_tu_stem(infinitive): 
    return verbs[infinitive][1][:-1]  


def get_third_person_plural_present_stem(infinitive): 
   return loro_present(infinitive)[:-3] 
    

def get_infinitive_minus_last_letter(infinitive): 
    return infinitive[:-1] 