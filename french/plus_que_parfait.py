from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_plus_que_parfait(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avais ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'étais ' + get_past_participle(infinitive)

def tu_plus_que_parfait(infinitive): 
    return je_plus_que_parfait(infinitive)

# TODO separate il and elle forms 
def il_elle_plus_que_parfait(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avait ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'était ' + get_past_participle(infinitive)

def nous_plus_que_parfait(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avions ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'étions ' + get_past_participle(infinitive)


def vous_plus_que_parfait(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'aviez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'étiez ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_plus_que_parfait(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avaient ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'étaient ' + get_past_participle(infinitive)


def make_plus_que_parfait(infinitive): 
    return (je_plus_que_parfait(infinitive),
            tu_plus_que_parfait(infinitive),
            il_elle_plus_que_parfait(infinitive),
            nous_plus_que_parfait(infinitive),
            vous_plus_que_parfait(infinitive),
            ils_elles_plus_que_parfait(infinitive))