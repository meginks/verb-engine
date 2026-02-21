from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import *   


def eu_futuro_composto_congiuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tiver ' + form + '\n'
    return conjugated_forms

def tu_futuro_composto_congiuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tiveres ' + form + '\n'
    return conjugated_forms

def voce_ele_ela_futuro_composto_congiuntivo(infinitive): 
    return eu_futuro_composto_congiuntivo(infinitive)

def nos_futuro_composto_congiuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivermos ' + form + '\n'
    return conjugated_forms
def vos_futuro_composto_congiuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tiverdes ' + form + '\n'
    return conjugated_forms

def voces_eles_elas_futuro_composto_congiuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tiverem ' + form + '\n'
    return conjugated_forms

def make_futuro_composto_do_conjuntivo(infinitive): 
    return (eu_futuro_composto_congiuntivo(infinitive),
            tu_futuro_composto_congiuntivo(infinitive),
            voce_ele_ela_futuro_composto_congiuntivo(infinitive),
            nos_futuro_composto_congiuntivo(infinitive),
            vos_futuro_composto_congiuntivo(infinitive),
            voces_eles_elas_futuro_composto_congiuntivo(infinitive))