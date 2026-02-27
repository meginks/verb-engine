from it_helper_functions import * 


def io_futuro_semplice(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'erò' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'irò' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'ò'

def tu_futuro_semplice(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'erai' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'irai' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'ai'

def lui_lei_futuro_semplice(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'erà' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'irà' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'à'

def noi_futuro_semplice(infinitive):
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'eremo' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'iremo' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'emo'

def voi_futuro_semplice(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'erete' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'irete' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'ete'

def loro_futuro_semplice(infinitive): 
    ending = get_infinitive_ending(infinitive) 
    if ending == are or ending == ere: 
         return get_infinitive_stem(infinitive) + 'eranno' 
    elif ending == ire: 
        return get_infinitive_stem(infinitive) + 'iranno' 
    elif ending == rre: 
        return get_infinitive_minus_last_letter(infinitive) + 'anno'

def make_futuro_semplice(infinitive): 
    return (io_futuro_semplice(infinitive),
            tu_futuro_semplice(infinitive), 
            lui_lei_futuro_semplice(infinitive), 
            noi_futuro_semplice(infinitive), 
            voi_futuro_semplice(infinitive), 
            loro_futuro_semplice(infinitive))