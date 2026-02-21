
def eu_condicional_imperfeito(infinitive):
    return infinitive + 'ia'

def tu_condicional_imperfeito(infinitive):
    return infinitive + 'ias'

def voce_ele_ela_condicional_imperfeito(infinitive): 
    return infinitive + 'ia'

def nos_condicional_imperfeito(infinitive): 
    return infinitive + 'íamos'

def vos_condicional_imperfeito(infinitive): 
    return infinitive + 'íeis'

def voces_eles_elas_condicional_imperfeito(infinitive): 
    return infinitive + 'iam'

def make_condicional_imperfeito(infinitive): 
    return (eu_condicional_imperfeito(infinitive),
            tu_condicional_imperfeito(infinitive),
            voce_ele_ela_condicional_imperfeito(infinitive),
            nos_condicional_imperfeito(infinitive),
            vos_condicional_imperfeito(infinitive),
            voces_eles_elas_condicional_imperfeito(infinitive))
