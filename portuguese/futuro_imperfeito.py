from pt_verbs import * 
from pt_helper_functions import * 
from pt_rule_exceptions import * 

def eu_futuro_imperfeito(infinitive):
    return infinitive + 'ei'

def tu_futuro_imperfeito(infinitive):
    return infinitive + 'ás'

def voce_ele_ela_futuro_imperfeito(infinitive): 
    return infinitive + 'á'

def nos_futuro_imperfeito(infinitive): 
    return infinitive + 'emos'

def vos_futuro_imperfeito(infinitive): 
    return infinitive + 'eis'

def voces_eles_elas_futuro_imperfeito(infinitive): 
    return infinitive + 'ão'

def make_futuro_imperfeito(infinitive): 
    return (eu_futuro_imperfeito(infinitive),
            tu_futuro_imperfeito(infinitive),
            voce_ele_ela_futuro_imperfeito(infinitive),
            nos_futuro_imperfeito(infinitive),
            vos_futuro_imperfeito(infinitive),
            voces_eles_elas_futuro_imperfeito(infinitive))