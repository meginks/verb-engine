from presente import * 
from imperfetto import *
from passato_prossimo import *
from trapassato_prossimo import *
from futuro_semplice import *
from futuro_anteriore import *
from condizionale_passato import *
from condizionale_presente import *
from congiuntivo_presente import *
from congiuntivo_imperfetto import *
from congiuntivo_passato import *
from congiuntivo_trapassato import * 



verb_selection = input('Enter the verb you wish to conjugate:') 

tense_selection = input('Enter the tense you wish to conjugate in. Options are: \n 1. presente \n 2. imperfetto \n 3. passato prossimo \n 4. trapassato prossimo \n 5. futuro semplice \n 6. futuro anteriore \n 7. condizionale presente \n 8. condizionale passato \n 9. congiuntivo presente \n 10. congiuntivo imperfetto \n 11. congiuntivo passato \n 12. congiuntivo trapassato. \n You can also enter the number corresponding to the tense.') 

if tense_selection == 'presente' or tense_selection == '1':
    print(make_present(verb_selection))
elif tense_selection == 'imperfetto' or tense_selection == '2':
    print(make_imperfect(verb_selection))
elif tense_selection == 'passato prossimo' or tense_selection == '3':
    print(make_past_perfect(verb_selection))
elif tense_selection == 'trapassato prossimo' or tense_selection == '4':
    print(make_pluperfect(verb_selection))
elif tense_selection == 'futuro semplice' or tense_selection == '5':
    ## 
    print()
elif tense_selection == 'futuro anteriore' or tense_selection == '6': 
    ## 
    print()
elif tense_selection == 'condizionale presente' or tense_selection == '7': 
    ## 
    print()
elif tense_selection == 'condizionale passato' or tense_selection == '8': 
    ## 
    print()
elif tense_selection == 'congiuntivo presente' or tense_selection == '9': 
    ## 
    print()
elif tense_selection == 'congiuntivo imperfetto' or tense_selection == '10': 
    ## 
    print()
elif tense_selection == 'congiuntivo passato' or tense_selection == '11': 
    ## 
    print()
elif tense_selection == 'congiuntivo trapassato' or tense_selection == '12': 
    ## 
    print()
else: 
    print('Sorry. We do not have this tense in the system.')     