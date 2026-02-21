from pt_helper_functions import * 
from pt_verbs import * 
from pt_rule_exceptions import * 

def eu_futuro_congiuntivo(infinitive):
    return get_third_person_plural_preterite_stem(infinitive) + 'r'

def tu_futuro_congiuntivo(infinitive):
    return get_third_person_plural_preterite_stem(infinitive) + 'res'

def voce_ele_ela_futuro_congiuntivo(infinitive): 
    return get_third_person_plural_preterite_stem(infinitive) + 'r'

def nos_futuro_congiuntivo(infinitive): 
    return get_third_person_plural_preterite_stem(infinitive) + 'rmos'

def vos_futuro_congiuntivo(infinitive): 
    return get_third_person_plural_preterite_stem(infinitive) + 'rdes'

def voces_eles_elas_futuro_congiuntivo(infinitive): 
    return  get_third_person_plural_preterite_stem(infinitive) + 'rem'

def make_futuro_do_conjuntivo(infinitive): 
    return (eu_futuro_congiuntivo(infinitive),
            tu_futuro_congiuntivo(infinitive),
            voce_ele_ela_futuro_congiuntivo(infinitive),
            nos_futuro_congiuntivo(infinitive),
            vos_futuro_congiuntivo(infinitive),
            voces_eles_elas_futuro_congiuntivo(infinitive))  