from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import *

def eu_presente_do_conjuntivo(infinitive):
    if infinitive in verbs: 
        ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive) 
        conjugated_form = ''
        if (ending == ar): 
            conjugated_form = stem + 'e' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'a' 
        return conjugated_form

def tu_presente_do_conjuntivo(infinitive):
    if infinitive in verbs: 
    ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive)
        conjugated_form = '' 
        if (ending == ar): 
            conjugated_form = stem + 'es' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'as' 
        return conjugated_form

def voce_ele_ela_presente_do_conjuntivo(infinitive): 
    if infinitive in verbs: 
    ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive)
        conjugated_form = '' 
        if (ending == ar): 
            conjugated_form = stem + 'e' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'a' 
        return conjugated_form 

def nos_presente_do_conjuntivo(infinitive): 
    if infinitive in verbs: 
    ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive)
        conjugated_form = '' 
        if (ending == ar): 
            conjugated_form = stem + 'emos' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'amos' 
        return conjugated_form 

def vos_presente_do_conjuntivo(infinitive): 
    if infinitive in verbs: 
    ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive)
        conjugated_form = '' 
        if (ending == ar): 
            conjugated_form = stem + 'eis' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'ais' 
        return conjugated_form 

def voces_eles_elas_presente_do_conjuntivo(infinitive): 
    if infinitive in verbs: 
    ## get conjugation 
        stem = get_first_person_singular_stem(infinitive) 
        ending = get_infinitive_ending(infinitive)
        conjugated_form = '' 
        if (ending == ar): 
            conjugated_form = stem + 'em' 
        elif (ending == er or ending == ir): 
            conjugated_form = stem + 'am' 
        return conjugated_form 


def make_presente_do_conjuntivo(infinitive): 
    if infinitive not in verbs: 
        print('Sorry this verb is not in our dictionary')
    elif infinitive in presente_do_conjuntivo_exceptions: # TO DO SUPPORT EXCEPTIONS 
        print('Sorry this verb is an exception and is not currently supported') 
    else: 
        return (eu_presente_do_conjuntivo(infinitive), 
            tu_presente_do_conjuntivo(infinitive), 
            voce_ele_ela_presente_do_conjuntivo(infinitive), 
            nos_presente_do_conjuntivo(infinitive), 
            vos_presente_do_conjuntivo(infinitive), 
            voces_eles_elas_presente_do_conjuntivo(infinitive))