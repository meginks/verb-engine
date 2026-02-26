# verb endings 
from french.present_indicatif import ils_elles_present
from fr_verbs import * 

er = 'er' 
re = 're' 
ir = 'ir' 

avoir = 'avoir' 
etre = 'être'

def get_infinitive_ending(infinitive): 
    return infinitive[-2:]   

def get_verb_stem(infinitive): 
    return infinitive[:-2]   

def get_third_person_plural_present_stem(infinitive): 
    return ils_elles_present(infinitive)[:-3] 

def get_future_stem(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == er or ending == ir: 
        return infinitive
    elif ending == re: 
        return infinitive[:-1] 
    
def get_avoir_or_etre(infinitive): 
    return verbs[infinitive][5] 

def get_past_participle(infinitive): 
    return verbs[infinitive][4]  