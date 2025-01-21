import pandas as pd

df = pd.read_excel("C:\\Users\\marco\\Downloads\\employee-breakdown-2025-01.xlsx")
df2 = pd.read_excel("C:\\Users\\marco\\Downloads\\attendance-report-2024-10-01_2024-12-31.xlsx")


nome = df.loc[0, 'employee_name']
id = df.loc[0, 'employee_id']
data_str = str(df.loc[0, 'date'])[:-9]

col_expected_scheduled = df['expected_scheduled']

print(col_expected_scheduled[1])
print(data_str)
print(id)
print(nome)

