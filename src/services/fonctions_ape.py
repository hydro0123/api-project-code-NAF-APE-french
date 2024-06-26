def code_ape_get_label(code,niv,df):
    niv=int(niv)
    niv_index="Label NIV"+str(niv)
    label=df.loc[code,niv_index]
    response={"niveau":niv,"label":label}
    return(response)

def BACH_R11(code,tb,fp,df):
    tb=float(tb)
    fp=float(fp)
    Q1_solvabilite=df.loc[code,"R11_Q1"]
    Q2_solvabilite=df.loc[code,"R11_Q2"]
    Q3_solvabilite=df.loc[code,"R11_Q3"]
    ratio_de_solvabilite_en_fr=(fp/tb)*100
    ratio_de_solvabilite_en_eu=(tb/fp)*100
    ratio_de_solvabilite_en_fr=round(ratio_de_solvabilite_en_fr,3)
    if ratio_de_solvabilite_en_eu<Q1_solvabilite:
        Q_S_phrase=("Q1: Entreprise fait partie du premier quartile du ratio de solvabilité.")
        Q_S="Q4 solvabilité"
    elif (ratio_de_solvabilite_en_eu>=Q1_solvabilite)&(ratio_de_solvabilite_en_eu<Q2_solvabilite):
        Q_S_phrase=("Q2: Entreprise fait partie du deuxieme quartile du ratio de solvabilité.")
        Q_S="Q3 solvabilité"
    elif (ratio_de_solvabilite_en_eu>=Q2_solvabilite)&(ratio_de_solvabilite_en_eu<Q3_solvabilite):
        Q_S_phrase=("Q3: Entreprise fait partie du troisieme quartile du ratio de solvabilité.")
        Q_S="Q2 solvabilité"
    elif ratio_de_solvabilite_en_eu>=Q3_solvabilite:
        Q_S_phrase=("Q4: Entreprise fait partie du quatrieme quartile du ratio de solvabilité.")
        Q_S="Q1 solvabilité"
    else:
        Q_S_phrase=("Manque de données")
        Q_S="Manque de données"
    Q_S_phrase_FR=("L'entreprise a un ratio de solvabilité (avec Ratio FR) de",str(ratio_de_solvabilite_en_fr),"%")
    #
    #Label:
    #
    LabelNIV2=df.loc[code,"Label NIV2"]
    LabelNIV1=df.loc[code,"Label NIV1"]
    Label=("L'entreprise fait partie de la section",LabelNIV1,"et l'entreprise est dans la sous-partie",LabelNIV2)
    return Q_S + " : " + str(ratio_de_solvabilite_en_fr) + "%"
    
#R28
def BACH_R28(CodeAPE,DU,YQ,YR,YS,CF,CG,EE,df):
    # DU=empruntd et dettes aupres des etablissements de credit
    # YQ= Engagement de credit bail mobilier
    # YR= engagement de credit bail immobilier
    # YS= efets portés a l escompte et non echus
    # CF= disponibilités, brut
    # CG= disponibilités, amortissement, provisions
    # EE= total bilan
    # R28= "Ratio d’endettement net des établissements de crédit"
    # Dettes nettes envers les établissements de crédit / Total bilan
    DU=float(DU)
    YQ=float(YQ)
    YR=float(YR)
    YS=float(YS)
    CF=float(CF)
    CG=float(CG)
    EE=float(EE)
    Q1_R28=df.loc[CodeAPE,"R28_Q1"]
    Q2_R28=df.loc[CodeAPE,"R28_Q2"]
    Q3_R28=df.loc[CodeAPE,"R28_Q3"]
    ratio_R28_eu=((DU+0.87*YQ+0.65*YR+YS)-(CF-CG))/EE
    ratio_R28_eu=round(ratio_R28_eu,3)
    if ratio_R28_eu<Q1_R28:
        print("Q1: Entreprise fait partie du premier quartile du ratio d'endettement net des établissements de crédit.")
        Q="Q1 endetement"
    elif (ratio_R28_eu>=Q1_R28)&(ratio_R28_eu<Q2_R28):
        print("Q2: Entreprise fait partie du deuxieme quartile du ratio d'endettement net des établissements de crédit.")
        Q="Q2 endetement"
    elif (ratio_R28_eu>=Q2_R28)&(ratio_R28_eu<Q3_R28):
        print("Q3: Entreprise fait partie du troisieme quartile du ratio d'endettement net des établissements de crédit.")
        Q="Q3 endetement"
    elif ratio_R28_eu>=Q3_R28:
        print("Q4: Entreprise fait partie du quatrieme quartile du ratio d'endettement net des établissements de crédit.")
        Q="Q4 endetement"
    else:
        print("Manque de données")
        Q="Manque de données"

    return Q+" ; "+str(ratio_R28_eu)