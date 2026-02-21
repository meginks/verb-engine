
from condicional_composto import *
from condicional_imperfeito import * 
from futuro_composto_do_conjuntivo import *
from futuro_do_conjuntivo import *
from futuro_imperfeito import * 
from futuro_perfeito_composto import *  
from imperativo import * 
from presente import * 
from presente_do_conjuntivo import *
from preterito_imperfeito_do_conjuntivo import *
from preterito_imperfeito import *
from preterito_mqp_composto import *
from preterito_mais_que_perfeito import *    
from preterito_mqp_do_conjuntivo import *     
from preterito_perfeito_do_conjuntivo import *
from preterito_perfeito import *


# add conditional tenses and other tenses as needed.

def portuguese_conjugator():

    verb_selection = input('Enter the verb you wish to conjugate:') 
    
    tense_selection = input('Enter the tense you wish to conjugate in. Options are: \n 1. condicional composto \n 2. condicional imperfeito \n 3. futuro composto do conjuntivo \n 4. futuro do conjuntivo \n 5. futuro imperfeito \n 6. futuro perfeito composto \n 7. imperativo \n 8. presente \n 9. presente do conjuntivo \n 10. pretérito imperfeito do conjuntivo \n 11. pretérito imperfeito \n 12. pretérito mais que perfeito \n 13. pretérito mais que perfeito composto \n 14. pretérito mais que perfeito do conjuntivo \n 15. pretérito perfeito do conjuntivo \n 16. pretérito perfeito. \n You can also enter the number corresponding to the tense.')
    
    if tense_selection == 'condicional composto' or tense_selection == '1':         
        print(make_condicional_composto(verb_selection))
    elif tense_selection == 'condicional imperfeito' or tense_selection == '2': 
        print(make_condicional_imperfeito(verb_selection))                   
    elif tense_selection == 'futuro composto do conjuntivo' or tense_selection == '3': 
        print(make_futuro_composto_do_conjuntivo(verb_selection))
    elif tense_selection == 'futuro do conjuntivo' or tense_selection == '4': 
        print(make_futuro_do_conjuntivo(verb_selection))
    elif tense_selection == 'futuro imperfeito' or tense_selection == '5': 
        print(make_futuro_imperfeito(verb_selection))
    elif tense_selection == 'futuro perfeito composto' or tense_selection == '6': 
        print(make_futuro_perfeito_composto(verb_selection))
    elif tense_selection == 'imperativo' or tense_selection == '7': 
        print(make_imperativo(verb_selection))
    elif tense_selection == 'presente' or tense_selection == '8': 
        print(make_presente(verb_selection))
    elif tense_selection == 'presente do conjuntivo' or tense_selection == '9': 
        print(make_presente_do_conjuntivo(verb_selection))
    elif tense_selection == 'pretérito imperfeito do conjuntivo' or tense_selection == '10': 
        print(make_preterito_imperfeito_do_conjuntivo(verb_selection))
    elif tense_selection == 'pretérito imperfeito' or tense_selection == '11': 
        print(make_preterito_imperfeito(verb_selection))
    elif tense_selection == 'pretérito mais que perfeito' or tense_selection == '12':     
        print(make_preterito_mais_que_perfeito(verb_selection))
    elif tense_selection == 'pretérito mais que perfeito composto' or tense_selection == '13': 
        print(make_preterito_mqp_composto(verb_selection))   
    elif tense_selection == 'pretérito mais que perfeito do conjuntivo' or tense_selection == '14': 
        print(make_preterito_mqp_do_conjuntivo(verb_selection))
    elif tense_selection == 'pretérito perfeito do conjuntivo' or tense_selection == '15': 
        print(make_preterito_perfeito_do_conjuntivo(verb_selection))
    elif tense_selection == 'pretérito perfeito' or tense_selection == '16': 
        print(make_preterito_perfeito(verb_selection))
    else: 
        print('Sorry. We do not have this tense in the system.') 


portuguese_conjugator()