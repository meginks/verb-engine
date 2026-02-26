from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aie ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'sois ' + get_past_participle(infinitive)

def tu_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aies ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'sois ' + get_past_participle(infinitive)

# TODO separate il and elle forms 
def il_elle_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'ait ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'soit ' + get_past_participle(infinitive)

def nous_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'ayons ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'soyons ' + get_past_participle(infinitive)


def vous_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'ayez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'soyez ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_passe_du_subjonctif(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aient ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'soient ' + get_past_participle(infinitive)

def make_passe_du_subjonctif(infinitive): 
    return (je_passe_du_subjonctif(infinitive),
            tu_passe_du_subjonctif(infinitive),
            il_elle_passe_du_subjonctif(infinitive),
            nous_passe_du_subjonctif(infinitive),
            vous_passe_du_subjonctif(infinitive),
            ils_elles_passe_du_subjonctif(infinitive))