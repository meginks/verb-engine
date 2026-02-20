
## TRAPASSATO PROSSIMO 

def io_trapassato_prossimo(infinitive): 
    return 

def tu_trapassato_prossimo(infinitive): 
    return 

def lui_lei_trapassato_prossimo(infinitive): 
    return 

def noi_trapassato_prossimo(infinitive):
    return 

def voi_trapassato_prossimo(infinitive): 
    return 

def loro_trapassato_prossimo(infinitive): 
    return


# TO DO HANDLE PLUPERFECT / trapassato prossimo
def make_pluperfect(infinitive):
    conjugated_verb = (io_trapassato_prossimo(infinitive), 
                       tu_trapassato_prossimo(infinitive), 
                       lui_lei_trapassato_prossimo(infinitive),
                       noi_trapassato_prossimo(infinitive), 
                       voi_trapassato_prossimo(infinitive), 
                       loro_trapassato_prossimo(infinitive)) 
    return conjugated_verb