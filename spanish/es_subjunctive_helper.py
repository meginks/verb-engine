from spanish.es_past_tense import ellos_preterito 

## SUBJUNCTIVE SPECIFIC HELPERS 

def get_3_pers_pl_preterite_stem(infinitive): 
    third_pers_pl_preterite = ellos_preterito(infinitive) 
    return third_pers_pl_preterite[:-2] 