# **What and How to do?**

## How to run the project

- you need to run **`main.py`** in the directory **`src`**
- it will create an api, you can open it with the local adress **(default one is: http://127.0.0.1:8000 )** and add /docs; http://127.0.0.1:8000/docs

## What does this project do?
At the moment, the project can do 3 things;
- Get the Label/Category of a buisness with the APE Code *(NAF code in english)* with the level of precision you want

**Ratio below work only for french buisness with 2022 Data;**
- Get the Ratio 11 BACH `(BANK FOR THE ACCOUNTS OF COMPANIES HARMONIZED / EUROPEAN DATA)` of a buisness in his own category with the code APE `(you need to enter the "Total Bilan"(EE in french documents or A in BACH Code) and "Fond propres"(DL in french or E in BACH Code))`
- Get the Ratio 28 BACH of a buisness in his own category with the APE code `(need to enter data by the code of french documents)`

# **INFORMATION**
### DISCLAMER: ***`french project, you can find untranslated words/code`***
## APE Code / NAF Code
 **APE Code** (NAF Code in English) is created by <u>*INSEE/IMSEE*</u> to classify buisness for financial purpose

## Notebook
you can find all NoteBook in the directory **`notebook`**

<u>/!\ </u>-> If you run the **`INSEE_code_APE`** notebook, it will create you excel files on your computer, I already give all excel files you need in the **`data`** directory

## Files in data directory
 **Files are open source**

most files are excel files and here is the link where which file is;
- **`naf2008_5_niveaux`** is from https://www.insee.fr/fr/information/2120875 ( last file (excel one) with the name of "*Liste des niveaux emboîtés"*)
- **`int_courts_naf_rev_2`** is from https://www.insee.fr/fr/information/2120875 ( first file with the name of "*Libellés longs, courts et abrégés de tous les postes*")
- **`Code_APE`** is a file created by the notebook **`INSEE_code_APE`** in the **`data`** directory
- **`export-bach`** is a file from https://www.bach.banque-france.fr/#/login (need an account)
- **`BACH_data_merge`** is a file created by the notebook **`Ratio_BACH`** in the **`data`** directory
