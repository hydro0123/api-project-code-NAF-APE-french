def code_ape_get_label(code,niv,df):
    niv="Label NIV"+str(niv)
    return(df.loc[code,niv])

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
        Q_S="Q1 solvabilité"
    elif (ratio_de_solvabilite_en_eu>=Q1_solvabilite)&(ratio_de_solvabilite_en_eu<Q2_solvabilite):
        Q_S_phrase=("Q2: Entreprise fait partie du deuxieme quartile du ratio de solvabilité.")
        Q_S="Q2 solvabilité"
    elif (ratio_de_solvabilite_en_eu>=Q2_solvabilite)&(ratio_de_solvabilite_en_eu<Q3_solvabilite):
        Q_S_phrase=("Q3: Entreprise fait partie du troisieme quartile du ratio de solvabilité.")
        Q_S="Q3 solvabilité"
    elif ratio_de_solvabilite_en_eu>=Q3_solvabilite:
        Q_S_phrase=("Q4: Entreprise fait partie du quatrieme quartile du ratio de solvabilité.")
        Q_S="Q4 solvabilité"
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
    print(" ||| " +Q_S_phrase+" (avec Ratio EU)"+ " ||| " +Q_S_phrase_FR+" ||| "+str(Label))
    return Q_S
    