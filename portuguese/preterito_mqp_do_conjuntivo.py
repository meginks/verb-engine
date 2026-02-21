from pt_helper_functions import *
from pt_verbs import *
from pt_rule_exceptions import *

# PRETERITO MAIS QUE PERFEITO COMPOSTO

def eu_preterito_mqp_conjuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivesse' + form + '\n'
    return conjugated_forms

def tu_preterito_mqp_conjuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivesses' + form + '\n'
    return conjugated_forms

def voce_ele_ela_preterito_mqp_conjuntivo(infinitive): 
    return eu_preterito_mqp_conjuntivo(infinitive) 

def nos_preterito_mqp_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivéssemos ' + form + '\n'
    return conjugated_forms

def vos_preterito_mqp_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivésseis ' + form + '\n'
    return conjugated_forms

def voces_eles_elas_preterito_mqp_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tivessem ' + form + '\n'
    return conjugated_forms

def make_preterito_mqp_do_conjuntivo(infinitive): 
    return (eu_preterito_mqp_conjuntivo(infinitive),
            tu_preterito_mqp_conjuntivo(infinitive),
            voce_ele_ela_preterito_mqp_conjuntivo(infinitive),
            nos_preterito_mqp_conjuntivo(infinitive),
            vos_preterito_mqp_conjuntivo(infinitive),
            voces_eles_elas_preterito_mqp_conjuntivo(infinitive))