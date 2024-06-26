from fastapi import FastAPI, Query
import uvicorn
from colorama import init
import pandas as pd
import os
from services.fonctions_ape import (
    code_ape_get_label,
    code_ape_get_all_label,
    BACH_R11,
    BACH_R28,
)

files_main = __file__
dossier_src = os.path.dirname(files_main)
dossier = os.path.dirname(dossier_src)
dossier_data = os.path.join(dossier, "data")
files_label = os.path.join(dossier_data, "int_courts_naf_rev_2.xls")
files_niv = os.path.join(dossier_data, "naf2008_5_niveaux.xls")
files_CodeAPE = os.path.join(dossier_data, "Code_APE.xlsx")
files_BACH = os.path.join(dossier_data, "BACH_data_merge.xlsx")

table_CodeAPE = pd.read_excel(files_CodeAPE)
table_CodeAPE = table_CodeAPE.set_index("NIV5")

table_BACH = pd.read_excel(files_BACH)
table_BACH = table_BACH.set_index("NIV5")

app = FastAPI()


@app.get("/Code_APE")
def Code_APE_Label(Code, NIV):
    return code_ape_get_label(Code, NIV, table_CodeAPE)


@app.get("/Code_APE_all")
def Code_APE_all_Label(Code):
    return code_ape_get_all_label(Code, table_CodeAPE)


@app.get("/R11")
def Ratio_11_solvabilite(
    Code=Query(..., description="Code APE de l'entreprise."),
    TB=Query(
        ..., description="Total Bilan, code EE sur liasse fiscale  2050."
    ),
    FP=Query(
        ..., description="Fonds Propres, code DL sur liasse fiscale 2050."
    ),
):
    return BACH_R11(Code, TB, FP, table_BACH)


@app.get("/R28")
def Ratio_28_dette(
    Code=Query(..., description="Code APE de l'entreprise."),
    DU=Query(
        ...,
        description="emprunts et dettes auprès des etablissements de crédit, code DU sur liasse fiscale 2050.",
    ),
    YQ=Query(
        ...,
        description="crédit-bail mobilier, code YQ sur liasse fiscale 2050.",
    ),
    YR=Query(
        ...,
        description="crédit-bail immobilier, code YR sur liasse fiscale 2050.",
    ),
    YS=Query(
        ...,
        description="effets portés a l'escompte et non échus, code YS sur liasse fiscale 2050.",
    ),
    CG=Query(
        ...,
        description="disponibilités, code CG net sur liasse fiscale 2050."
    ),
    EE=Query(
        ...,
        description="Total Bilan, code EE sur liasse fiscale 2050."
    ),
):
    return BACH_R28(Code, DU, YQ, YR, YS, CG, EE, table_BACH)


if __name__ == "__main__":
    init()
    uvicorn.run(app)
