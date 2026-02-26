from present_indicatif import * 
from imparfait_indicatif import *
from passe_compose import *
from futur_indicatif import *
from imperatif import * 
from passe_compose import *
from passe_anterieur import *
from plus_que_parfait import *
from futur_anterieur import *
from passe_simple import * 
from present_du_conditionnel import *
from conditionnel_passe import *
from plus_que_parfait_du_subjonctif import *
from imparfait_du_subjonctif import *
from plus_que_parfait_du_subjonctif import *    

def french_conjugator(infinitive): 
    verb_selection = input('Enter the verb you wish to conjugate in infinitive form: ') 
    tense_selection = input('Enter the tense you wish to conjugate in: \n 1. present indicatif \n 2. imparfait indicatif \n 3. passé composé \n 4. passé anterieur \n 5. futur indicatif \n 6. imperatif \n 7. passé anterieur \n 8. plus que parfait \n 9. futur anterieur \n 10. passe simple \n 11. present du conditionnel \n 12. conditionnel passé \n 13. plus que parfait du subjonctif \n 14. imparfait du subjonctif \n 15. plus que parfait du subjonctif. You can also enter the number corresponding to the tense.') 
    
    if tense_selection == 'present indicatif' or tense_selection == '1':
        print(make_present_indicatif(verb_selection))
    elif tense_selection == 'imparfait indicatif' or tense_selection == '2':
        print(make_imparfait_indicatif(verb_selection))
    elif tense_selection == 'passé composé' or tense_selection == '3':
        print(make_passe_compose(verb_selection))
    elif tense_selection == 'passé anterieur' or tense_selection == '4':
        print(make_passe_anterieur(verb_selection))
    elif tense_selection == 'futur indicatif' or tense_selection == '5':
        print(make_futur_indicatif(verb_selection))
    elif tense_selection == 'imperatif' or tense_selection == '6':
        print(make_imperatif(verb_selection))
    elif tense_selection == 'plus que parfait' or tense_selection == '8':
        print(make_plus_que_parfait(verb_selection))
    elif tense_selection == 'futur anterieur' or tense_selection == '9':
        print(make_futur_anterieur(verb_selection))
    elif tense_selection == 'passe simple' or tense_selection == '10':
        print(make_passe_simple(verb_selection))
    elif tense_selection == 'present du conditionnel' or tense_selection == '11':
        print(make_present_du_conditionnel(verb_selection))
    elif tense_selection == 'conditionnel passé' or tense_selection == '12':
        print(make_conditionnel_passe(verb_selection))
    elif tense_selection == 'plus que parfait du subjonctif' or tense_selection == '13':
        print(make_plus_que_parfait_du_subjonctif(verb_selection))
    elif tense_selection == 'imparfait du subjonctif' or tense_selection == '14':
        print(make_imparfait_du_subjonctif(verb_selection))
    elif tense_selection == 'plus que parfait du subjonctif' or tense_selection == '15':
        print(make_plus_que_parfait_du_subjonctif(verb_selection))
    else: 
        print('Sorry. We do not have this tense in the system.')