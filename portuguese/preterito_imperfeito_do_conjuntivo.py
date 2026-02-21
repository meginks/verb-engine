from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import *

def eu_presente_do_conjuntivo(infinitive):
    return get_third_person_plural_preterite_stem(infinitive) + 'sse'

def tu_preterito_imperfeito_do_conjuntivo(infinitive):
    return get_third_person_plural_preterite_stem(infinitive) + 'sses'
 

def voce_ele_ela_preterito_imperfeito_do_conjuntivo(infinitive): 
    return get_third_person_plural_preterite_stem(infinitive) + 'sse'
 
def nos_preterito_imperfeito_do_conjuntivo(infinitive): # TODO FIX ACCENT MARK íssimos / ássimos / éssimos
    return get_third_person_plural_preterite_stem(infinitive) + 'ssemos'

def vos_preterito_imperfeito_do_conjuntivo(infinitive): # TODO FIX ACCENT MARK ísseis / ásseis / ésseis
    return get_third_person_plural_preterite_stem(infinitive) + 'sseis'

def voces_eles_elas_preterito_imperfeito_do_conjuntivo(infinitive): 
    return get_third_person_plural_preterite_stem(infinitive) + 'ssem'

def make_preterito_imperfeito_do_conjuntivo(infinitive): 
    return (eu_presente_do_conjuntivo(infinitive),
            tu_preterito_imperfeito_do_conjuntivo(infinitive),
            voce_ele_ela_preterito_imperfeito_do_conjuntivo(infinitive),
            nos_preterito_imperfeito_do_conjuntivo(infinitive),
            vos_preterito_imperfeito_do_conjuntivo(infinitive),
            voces_eles_elas_preterito_imperfeito_do_conjuntivo(infinitive))  