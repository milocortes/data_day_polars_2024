import polars as pl
import time

start_time = time.time()

q = (
    pl.read_csv('../datos/flights.csv')
    .lazy()
    .select(['MONTH', 'ORIGIN_AIRPORT','DESTINATION_AIRPORT'])
    .filter(
        (pl.col('MONTH') == 5) & 
        (pl.col('ORIGIN_AIRPORT') == 'SFO') &
        (pl.col('DESTINATION_AIRPORT') == 'SEA'))
    )
df = q.collect()
print(df)
print(f"""\n\t *********************************\n\t
                 TIEMPO DE EJECUCION 
         --- {time.time() - start_time} segundos ---
        \n\t *********************************\n\t
        """)
