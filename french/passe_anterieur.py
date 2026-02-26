from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_passe_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eus ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fus ' + get_past_participle(infinitive)

def tu_passe_anterieur(infinitive): 
    return je_passe_anterieur(infinitive)

# TODO separate il and elle forms 
def il_elle_passe_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eut ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fut ' + get_past_participle(infinitive)

def nous_passe_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eûmes ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fûmes ' + get_past_participle(infinitive)


def vous_passe_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eûtes ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'fûtes ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_passe_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'eurent ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'furent ' + get_past_participle(infinitive)


def make_passe_anterieur(infinitive): 
    return (je_passe_anterieur(infinitive),
            tu_passe_anterieur(infinitive),
            il_elle_passe_anterieur(infinitive),
            nous_passe_anterieur(infinitive),
            vous_passe_anterieur(infinitive),
            ils_elles_passe_anterieur(infinitive))