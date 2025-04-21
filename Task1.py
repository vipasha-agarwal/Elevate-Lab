import pandas as pd

data = pd.read_csv("KaggleV2-May-2016.csv")

df_cleaned = df.dropna()

# print(df.isnull()) 

df = pd.DataFrame(data)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# print(df_no_duplicates)

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], dayfirst=True)  # handle dd-mm-yyyy
df['ScheduledDay'] = df['ScheduledDay'].dt.strftime('%d-%m-%Y')

df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], dayfirst=True)  # handle dd-mm-yyyy
df['AppointmentDay'] = df['AppointmentDay'].dt.strftime('%d-%m-%Y')

# print(df)

df.columns = df.columns.str.strip() \
                       .str.lower() \
                       .str.replace(' ', '_') \
                       .str.replace(r'[^\w]', '', regex=True)  # remove any non-word characters

# print(df.columns)
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # handles invalid entries gracefully
df['scheduledday'] = pd.to_datetime(df['scheduledday'], dayfirst=False)
df['appointmentday'] = pd.to_datetime(df['appointmentday'], dayfirst=False)
