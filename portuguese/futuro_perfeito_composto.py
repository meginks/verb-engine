from pt_helper_functions import *
from pt_verbs import *
from pt_rule_exceptions import *

def eu_futuro_perfeito_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'terei ' + form + '\n'
    return conjugated_forms


def tu_futuro_perfeito_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'terás ' + form + '\n'
    return conjugated_forms

def voce_ele_ela_futuro_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'terá ' + form + '\n'
    return conjugated_forms

def nos_futuro_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'teremos ' + form + '\n'
    return conjugated_forms 

def vos_futuro_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tereis ' + form + '\n'
    return conjugated_forms

def voces_eles_elas_futuro_perfeito_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'terão ' + form + '\n'
    return conjugated_forms

def make_futuro_perfeito_composto(infinitive): 
    return (eu_futuro_perfeito_composto(infinitive),
            tu_futuro_perfeito_composto(infinitive),
            voce_ele_ela_futuro_perfeito_composto(infinitive),
            nos_futuro_perfeito_composto(infinitive),
            vos_futuro_perfeito_composto(infinitive),
            voces_eles_elas_futuro_perfeito_composto(infinitive))