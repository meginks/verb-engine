from fr_rule_exceptions import * 
from fr_helper_functions import *
from fr_verbs import *  

## NOTE: depending on the place in the sentence, the past participle may need to be modified to agree with the subject, but I have not handled that in this at this point. Verbs with être always have to agree, and I have also not handled this yet -- TODO 

def je_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'ai ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'suis ' + get_past_participle(infinitive)

def tu_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'as ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'es ' + get_past_participle(infinitive)

# TODO separate il and elle forms 
def il_elle_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'a ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'est ' + get_past_participle(infinitive)

def nous_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avons ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'sommes ' + get_past_participle(infinitive)


def vous_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'avez ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'êtes ' + get_past_participle(infinitive)


# TODO separate ils and elles forms, right now all ils 
def ils_elles_passe_compose(infinitive): 
    auxiliary = get_avoir_or_etre(infinitive) 
    if auxiliary == avoir: 
        return 'ont ' + get_past_participle(infinitive)
    elif auxiliary == etre: 
        return 'sont ' + get_past_participle(infinitive)


def make_passe_compose(infinitive): 
    return (je_passe_compose(infinitive),
            tu_passe_compose(infinitive),
            il_elle_passe_compose(infinitive),
            nous_passe_compose(infinitive),
            vous_passe_compose(infinitive),
            ils_elles_passe_compose(infinitive))