import pandas as pd
import time

start_time = time.time()

df = pd.read_csv('../datos/flights.csv')
df = df[(df['MONTH'] == 5) & 
        (df['ORIGIN_AIRPORT'] == 'SFO') &
        (df['DESTINATION_AIRPORT'] == 'SEA')][['MONTH', 'ORIGIN_AIRPORT','DESTINATION_AIRPORT']]

print(df)
print(f"""\n\t *********************************\n\t
                 TIEMPO DE EJECUCION 
         --- {time.time() - start_time} segundos ---
        \n\t *********************************\n\t
        """)
