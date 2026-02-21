from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import * 

def eu_preterito_perfeito_conjuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenha ' + form + '\n'
    return conjugated_forms

def tu_preterito_perfeito_conjuntivo(infinitive):
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenhas ' + form + '\n'
    return conjugated_forms

def voce_ele_ela_preterito_perfeito_conjuntivo(infinitive): 
    return eu_preterito_perfeito_conjuntivo(infinitive) 

def nos_preterito_perfeito_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenhamos ' + form + '\n'
    return conjugated_forms

def vos_preterito_perfeito_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenhais ' + form + '\n'
    return conjugated_forms

def voces_eles_elas_preterito_perfeito_conjuntivo(infinitive): 
    conjugated_forms = ''
    for form in verbs[infinitive][4]: 
        conjugated_forms += 'tenham ' + form + '\n'
    return conjugated_forms

def make_preterito_perfeito_do_conjuntivo(infinitive): 
    return (eu_preterito_perfeito_conjuntivo(infinitive),
            tu_preterito_perfeito_conjuntivo(infinitive),
            voce_ele_ela_preterito_perfeito_conjuntivo(infinitive),
            nos_preterito_perfeito_conjuntivo(infinitive),
            vos_preterito_perfeito_conjuntivo(infinitive),
            voces_eles_elas_preterito_perfeito_conjuntivo(infinitive))  