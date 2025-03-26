import pdfplumber
import constants
import pandas as pd
import zipfile

pdf = constants.PDF

with pdfplumber.open(pdf) as pdf:
    tables = [page.extract_table() for page in pdf.pages if page.extract_table()]

full_data = []

for table in tables:
    for row in table:
        full_data.append(row)

df = pd.DataFrame(full_data)

df.columns = df.iloc[0]
df = df[1:]

df.replace(constants.CHANGES, inplace=True)

csv_filename = "Rol_Procedimentos.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

zip_filename = "Teste_Renato_Rocha_Ferreira.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename)

print(f'Zip file: {zip_filename}')


