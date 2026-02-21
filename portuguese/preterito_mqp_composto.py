from pt_helper_functions import *
from pt_verbs import *
from pt_rule_exceptions import *

# PRETERITO MAIS QUE PERFEITO COMPOSTO

def eu_preterito_mqp_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tinha ' + form + '\n'
    return conjugated_forms 

def tu_preterito_mqp_composto(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tinhas ' + form + '\n'
    return conjugated_forms 

def voce_ele_ela_preterito_mqp_composto(infinitive): 
    return eu_preterito_mqp_composto(infinitive)

def nos_preterito_mqp_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tínhamos ' + form + '\n'
    return conjugated_forms

def vos_preterito_mqp_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tínheis ' + form + '\n'
    return conjugated_forms

def voces_eles_elas_preterito_mqp_composto(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tinham ' + form + '\n'
    return conjugated_forms

def make_preterito_mqp_composto(infinitive): 
    return (eu_preterito_mqp_composto(infinitive),
            tu_preterito_mqp_composto(infinitive),
            voce_ele_ela_preterito_mqp_composto(infinitive),
            nos_preterito_mqp_composto(infinitive),
            vos_preterito_mqp_composto(infinitive),
            voces_eles_elas_preterito_mqp_composto(infinitive))