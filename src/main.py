from fastapi import FastAPI
import uvicorn
from colorama import init
import pandas as pd
import os
from services.fonctions_ape import code_ape_get_label
from services.fonctions_ape import BACH_R11

files_main=__file__
dossier_src = os.path.dirname(files_main)
dossier = os.path.dirname(dossier_src)
dossier_data=os.path.join(dossier,"data")
files_label=os.path.join(dossier_data,"int_courts_naf_rev_2.xls")
files_niv=os.path.join(dossier_data,"naf2008_5_niveaux.xls")
files_CodeAPE=os.path.join(dossier_data,"Code_APE.xlsx")
files_BACH=os.path.join(dossier_data,"BACH_data_merge.xlsx")

table_CodeAPE=pd.read_excel(files_CodeAPE)
table_CodeAPE=table_CodeAPE.set_index("NIV5")

table_BACH=pd.read_excel(files_BACH)
table_BACH=table_BACH.set_index("NIV5")

app = FastAPI()

@app.get("/Code_APE")
def Code_APE_Label(Code,NIV):
    return(code_ape_get_label(Code,NIV,table_CodeAPE))

@app.get("/R11")
def Ratio_11_solvabilite(Code,TB,FP):
    return(BACH_R11(Code,TB,FP,table_BACH))

if __name__ == "__main__":
    init()
    uvicorn.run(app)