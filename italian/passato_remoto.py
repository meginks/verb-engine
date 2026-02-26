from it_helper_functions import * 


# NOTE I have not handled the case where -ere verbs (except -ttere and --ssere verbs) have 2 options for 1st and 3rd person singular and 3rd person plural, e.g. credere --> io credei / creddetti, lui credé / creddette, loro crederono / creddettero -- TODO  

## PASSATO REMOTO 

def io_passato_remoto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'ai' 
    elif ending == ere: 
        return stem + 'ei' 
    elif ending == ire: 
        return stem + 'ii' 
    elif ending == rre:  
        return stem + 'ssi'

def tu_passato_remoto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'asti' 
    elif ending == ere: 
        return stem + 'esti' 
    elif ending == ire: 
        return stem + 'isti' 
    elif ending == rre:  
        return get_third_person_plural_present_stem(infinitive)+ 'esti'

def lui_lei_passato_remoto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'ò' 
    elif ending == ere: 
        return stem + 'è' 
    elif ending == ire: 
        return stem + 'ì' 
    elif ending == rre:  
        return stem + 'sse'

def noi_passato_remoto(infinitive):
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'ammo' 
    elif ending == ere: 
        return stem + 'emmo' 
    elif ending == ire: 
        return stem + 'immo' 
    elif ending == rre:  
        return get_third_person_plural_present_stem(infinitive) + 'emmo'

def voi_passato_remoto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'aste' 
    elif ending == ere: 
        return stem + 'este' 
    elif ending == ire: 
        return stem + 'iste' 
    elif ending == rre:  
        return get_third_person_plural_present_stem(infinitive) + 'este'

def loro_passato_remoto(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    stem = get_infinitive_stem(infinitive) 
    if ending == are: 
        return stem + 'arono' 
    elif ending == ere: 
        return stem + 'erono' 
    elif ending == ire: 
        return stem + 'irono' 
    elif ending == rre:  
        return stem + 'ssero'

def make_passato_remoto(infinitive): 
    return (io_passato_remoto(infinitive),
            tu_passato_remoto(infinitive), 
            lui_lei_passato_remoto(infinitive), 
            noi_passato_remoto(infinitive), 
            voi_passato_remoto(infinitive), 
            loro_passato_remoto(infinitive))