from italian.it_present_tense import * 



####################### INDICATIVE #############################################################
# INFINITIVE -> PRESENT 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE: TUPLE in this order (io, tu, lui / lei, noi, voi, loro) 
def make_present(infinitive):  
    conjugated_verb = (io_present(infinitive), 
                       tu_present(infinitive), 
                       lui_lei_present(infinitive),
                       noi_present(infinitive), 
                       voi_present(infinitive), 
                       loro_present(infinitive)) 
    return conjugated_verb  


# TO DO HANDLE IMPERFECT 
def make_imperfect(infinitive): 
    return 'verbs' 


# TO DO HANDLE PAST PERFECT 


# TO DO HANDLE PASSATO REMOTO 


# TO DO HANDLE FUTURO 


# TO DO HANDLE CONDITIONAL 


#### CONGIUNTIVO ##### 

# TO DO HANDLE PRESENT SUBJUNCTIVE 


# TO DO HANDLE IMPERFECT SUBJUNCTIVE 


