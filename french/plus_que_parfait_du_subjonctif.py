from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eusse ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fusse ' + get_past_participle(infinitive)

def tu_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eusses ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fusses ' + get_past_participle(infinitive)

# TODO separate il and elle forms 
def il_elle_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eût ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fût ' + get_past_participle(infinitive)

def nous_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eussions ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fussions ' + get_past_participle(infinitive)


def vous_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eussiez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fussiez ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_plus_que_parfait_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eussent ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fussent ' + get_past_participle(infinitive)
    
    
def make_plus_que_parfait_du_subjonctif(infinitive):
        return (je_plus_que_parfait_du_subjonctif(infinitive),
                tu_plus_que_parfait_du_subjonctif(infinitive),
                il_elle_plus_que_parfait_du_subjonctif(infinitive),
                nous_plus_que_parfait_du_subjonctif(infinitive),
                vous_plus_que_parfait_du_subjonctif(infinitive),
                ils_elles_plus_que_parfait_du_subjonctif(infinitive)) 