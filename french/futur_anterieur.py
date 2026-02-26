from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurai ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serai ' + get_past_participle(infinitive)

def tu_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'auras ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'seras ' + get_past_participle(infinitive)

# TODO separate il and elle forms 
def il_elle_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aura ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'sera ' + get_past_participle(infinitive)

def nous_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurons ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serons ' + get_past_participle(infinitive)


def vous_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aurez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'serez ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_futur_anterieur(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'auront ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'seront ' + get_past_participle(infinitive)


def make_futur_anterieur(infinitive): 
    return (je_futur_anterieur(infinitive),
            tu_futur_anterieur(infinitive),
            il_elle_futur_anterieur(infinitive),
            nous_futur_anterieur(infinitive),
            vous_futur_anterieur(infinitive),
            ils_elles_futur_anterieur(infinitive))