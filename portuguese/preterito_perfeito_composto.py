from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import * 


def eu_futuro_perfeito_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenho' + form + '\n'
    return conjugated_forms

def tu_preterito_perfeito_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tens' + form + '\n'
    return conjugated_forms

def voce_ele_ela_preterito_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tem' + form + '\n'
    return conjugated_forms

def nos_preterito_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'temos' + form + '\n'
    return conjugated_forms

def vos_preterito_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tendes' + form + '\n'
    return conjugated_forms

def voces_eles_elas_preterito_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'têm' + form + '\n'
    return conjugated_forms

def make_preterito_perfeito_composto(infinitive): 
    return (eu_futuro_perfeito_composto(infinitive),
            tu_preterito_perfeito_composto(infinitive),
            voce_ele_ela_preterito_perfeito_composto(infinitive),
            nos_preterito_perfeito_composto(infinitive),
            vos_preterito_perfeito_composto(infinitive),
            voces_eles_elas_preterito_perfeito_composto(infinitive))