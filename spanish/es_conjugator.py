from spanish.es_verbs import * 
from spanish.es_helper_functions import *  
from spanish.es_present_tense import * 
from spanish.es_past_tense import * 
from spanish.es_future_tense import * 
from spanish.es_conditional_tense import * 
### Methods for manipulating verb data to conjugate 


####################### INDICATIVE ################################################################
# INFINITIVE -> PRESENT 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE: TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_present(infinitive):  
    # form tuple: 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][0], 
                                 verbs[infinitive][1],
                                el_present(infinitive),
                                nosotros_present(infinitive),
                                vosotros_present(infinitive),
                                ellos_present(infinitive))); 
        return conjugated_verb
    else: 
       print('Lo siento. No tenemos este verbo en el sistema.') 

print('PRESENT TEST')
print(make_present('tener')) 
print(make_present('comprar')) 
print(make_present('sentarse'))
print(make_present('abrir'))
print(make_present('alquilar'))

# INFINITIVE -> IMPERFECT PAST 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_imperfect(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((yo_el_imperfecto(infinitive), 
                                tu_imperfecto(infinitive),
                                yo_el_imperfecto(infinitive),
                                nosotros_imperfecto(infinitive),
                                vosotros_imperfecto(infinitive),
                                ellos_imperfecto(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')

print('IMPERFECT TEST')
print(make_imperfect('tener')) 
print(make_imperfect('comprar')) 
print(make_imperfect('sentarse'))
print(make_imperfect('abrir'))

# INFINITIVE -> PRETERITE PAST 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_preterite(infinitive):  ## TODO -- handle irregular stem endings like tener and dar 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][2], 
                                 tu_preterito(infinitive),
                                el_preterito(infinitive),
                                nosotros_preterito(infinitive),
                                vosotros_preterito(infinitive),
                                ellos_preterito(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')
    
print('PRETERITE TEST')
print(make_preterite('tener')) 
print(make_preterite('comprar')) 
print(make_preterite('sentarse'))
print(make_preterite('abrir'))

# INFINITIVE -> FUTURE 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_future(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((yo_futuro(infinitive), 
                                 tu_futuro(infinitive),
                                el_futuro(infinitive),
                                nosotros_futuro(infinitive),
                                vosotros_futuro(infinitive),
                                ellos_futuro(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')
print('FUTURE TEST')
print(make_future('tener')) 
print(make_future('comprar')) 
print(make_future('sentarse'))
print(make_future('abrir'))
# INFINITIVE -> CONDITIONAL  
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_conditional(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((yo_el_condicional(infinitive), 
                                 tu_condicional(infinitive),
                                yo_el_condicional(infinitive),
                                nosotros_condicional(infinitive),
                                vosotros_condicional(infinitive),
                                ellos_condicional(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.') 
print('CONDITIONAL TEST')
print(make_conditional('tener')) 
print(make_conditional('comprar')) 
print(make_conditional('sentarse'))
print(make_conditional('abrir'))

####################### SUBJUNCTIVE ################################################################
# INFINITIVE -> PRESENT SUBJUNCTIVE 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_present_subjunctive(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((yo_el_subjuntivo_presente(infinitive), 
                                 tu_subjuntivo_presente(infinitive),
                                yo_el_subjuntivo_presente(infinitive),
                                nosotros_subjuntivo_presente(infinitive),
                                vosotros_subjuntivo_presente(infinitive),
                                ellos_subjuntivo_presente(infinitive))); 
        return conjugated_verb
    else: 
       print('Lo siento. No tenemos este verbo en el sistema.') 

# INFINITIVE -> IMPERFECT SUBJUNCTIVE  
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_imperfect_subjunctive(infinitive):
    if verbs[infinitive]:    
        conjugated_verb = tuple((yo_el_subjuntivo_pasado(infinitive), 
                                 tu_subjuntivo_pasado(infinitive),
                                yo_el_subjuntivo_pasado(infinitive),
                                nosotros_subjuntivo_pasado(infinitive),
                                vosotros_subjuntivo_pasado(infinitive),
                                ellos_subjuntivo_pasado(infinitive))); 
        return conjugated_verb
    else: 
       print('Lo siento. No tenemos este verbo en el sistema.') 
 
    
## COMPOUND TENSES 




# GET SPECIFIC FORM GENERIC METHOD 
def getSpecificForm(): 
    return 



print(get_infinitive_ending('abrir'))
print(get_infinitive_ending('comprar'))
print(get_infinitive_ending('sentarse'))


print(get_infinitive_stem('abrir'))
print(get_infinitive_stem('comprar'))
print(get_infinitive_stem('sentarse'))
