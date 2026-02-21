from pt_helper_functions import * 
from pt_verbs import *
from pt_rule_exceptions import * 

def eu_condicional_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'teria' + form + '\n'
    return conjugated_forms

def tu_condicional_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'terias' + form + '\n'
    return conjugated_forms

def voce_ele_ela_condicional_composto(infinitive): 
    return eu_condicional_composto(infinitive)

def nos_condicional_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'teríamos' + form + '\n'
    return conjugated_forms

def vos_condicional_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'teríeis' + form + '\n'
    return conjugated_forms

def voces_eles_elas_condicional_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'teriam' + form + '\n'
    return conjugated_forms

def make_condicional_composto(infinitive): 
    return (eu_condicional_composto(infinitive),
            tu_condicional_composto(infinitive),
            voce_ele_ela_condicional_composto(infinitive),
            nos_condicional_composto(infinitive),
            vos_condicional_composto(infinitive),
            voces_eles_elas_condicional_composto(infinitive))