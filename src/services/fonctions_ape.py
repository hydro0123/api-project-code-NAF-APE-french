def code_ape_get_label(code, niv, df):
    niv = int(niv)
    niv_index = "Label NIV" + str(niv)
    label = df.loc[code, niv_index]
    response = {"niveau": niv, "label": label}
    return response


def code_ape_get_all_label(code, df):
    responses = []
    for niv in range(1, 6):
        response = code_ape_get_label(code, niv, df)
        responses.append(response)
    return responses


def BACH_R11(code, tb, fp, df):
    tb = float(tb)
    fp = float(fp)
    Q1_solvabilite = df.loc[code, "R11_Q1"]
    Q2_solvabilite = df.loc[code, "R11_Q2"]
    Q3_solvabilite = df.loc[code, "R11_Q3"]
    ratio_de_solvabilite_en_fr = (fp / tb) * 100
    ratio_de_solvabilite_en_eu = (tb / fp) * 100
    ratio_de_solvabilite_en_fr = round(ratio_de_solvabilite_en_fr, 3)
    if ratio_de_solvabilite_en_eu < Q1_solvabilite:
        Q_S = "Q4"
        score = 4
    elif (ratio_de_solvabilite_en_eu >= Q1_solvabilite) & (
        ratio_de_solvabilite_en_eu < Q2_solvabilite
    ):
        Q_S = "Q3"
        score = 3
    elif (ratio_de_solvabilite_en_eu >= Q2_solvabilite) & (
        ratio_de_solvabilite_en_eu < Q3_solvabilite
    ):
        Q_S = "Q2"
        score = 2
    elif ratio_de_solvabilite_en_eu >= Q3_solvabilite:
        Q_S = "Q1"
        score = 1
    else:
        Q_S = "Manque de données"
    #
    # Label:
    #
    LabelNIV2 = df.loc[code, "Label NIV2"]
    LabelNIV1 = df.loc[code, "Label NIV1"]
    Label = (
        "L'entreprise fait partie de la section",
        LabelNIV1,
        "et l'entreprise est dans la sous-partie",
        LabelNIV2,
    )
    print(Label)
    response = {
        "label": "ratio de solvabilité",
        "valeur": ratio_de_solvabilite_en_fr,
        "unit": "%",
        "quartile": Q_S,
        "score": score,
    }
    return response


# R28
def BACH_R28(CodeAPE, DU, YQ, YR, YS, CG, EE, df):
    # DU=empruntd et dettes aupres des etablissements de credit
    # YQ= Engagement de credit bail mobilier
    # YR= engagement de credit bail immobilier
    # YS= efets portés a l escompte et non echus
    # CG= disponibilités, amortissement, provisions
    # EE= total bilan
    # R28= "Ratio d’endettement net des établissements de crédit"
    # Dettes nettes envers les établissements de crédit / Total bilan
    DU = float(DU)
    YQ = float(YQ)
    YR = float(YR)
    YS = float(YS)
    CG = float(CG)
    EE = float(EE)
    Q1_R28 = df.loc[CodeAPE, "R28_Q1"]
    Q2_R28 = df.loc[CodeAPE, "R28_Q2"]
    Q3_R28 = df.loc[CodeAPE, "R28_Q3"]
    ratio_R28_eu = ((DU + 0.87 * YQ + 0.65 * YR + YS) - (CG)) / EE
    ratio_R28_eu = round(ratio_R28_eu, 3)
    if ratio_R28_eu < Q1_R28:
        print(
            "Q1: Entreprise fait partie du premier quartile du ratio d'endettement net des établissements de crédit."
        )
        Q = "Q1 endetement"
        score = 4
    elif (ratio_R28_eu >= Q1_R28) & (ratio_R28_eu < Q2_R28):
        print(
            "Q2: Entreprise fait partie du deuxieme quartile du ratio d'endettement net des établissements de crédit."
        )
        Q = "Q2 endetement"
        score = 3
    elif (ratio_R28_eu >= Q2_R28) & (ratio_R28_eu < Q3_R28):
        print(
            "Q3: Entreprise fait partie du troisieme quartile du ratio d'endettement net des établissements de crédit."
        )
        Q = "Q3 endetement"
        score = 2
    elif ratio_R28_eu >= Q3_R28:
        print(
            "Q4: Entreprise fait partie du quatrieme quartile du ratio d'endettement net des établissements de crédit."
        )
        Q = "Q4 endetement"
        score = 1
    else:
        print("Manque de données")
        Q = "Manque de données"
        score = "null"
    ratio_R28_eu_percent = ratio_R28_eu * 100
    response = {
        "label": "dette net sur total bilan'",
        "valeur": ratio_R28_eu_percent,
        "unit": "%",
        "quartile": Q,
        "score": score,
    }
    return response
