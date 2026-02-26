from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_conditionnel_passe(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurais ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serais ' + get_past_participle(infinitive)

def tu_conditionnel_passe(infinitive): 
    return je_conditionnel_passe(infinitive)

# TODO separate il and elle forms 
def il_elle_conditionnel_passe(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurait ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serait ' + get_past_participle(infinitive)

def nous_conditionnel_passe(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurions ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serions ' + get_past_participle(infinitive)


def vous_conditionnel_passe(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'auriez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'seriez ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_conditionnel_passe(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'auraient ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'seraient ' + get_past_participle(infinitive)

def make_conditionnel_passe(infinitive): 
    return (je_conditionnel_passe(infinitive),
            tu_conditionnel_passe(infinitive),
            il_elle_conditionnel_passe(infinitive),
            nous_conditionnel_passe(infinitive),
            vous_conditionnel_passe(infinitive),
            ils_elles_conditionnel_passe(infinitive))