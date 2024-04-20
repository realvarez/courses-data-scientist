import pandas as pd
from typing import List
from sqlalchemy import Engine

def leer_tabla(nombre_tabla, engine):
    return pd.read_sql_table(nombre_tabla, engine)

def filter_by_date(
    df: pd.DataFrame,
    column:str,
    init_date:str,
    end_date:str
) -> pd.DataFrame:
    if pd.core.dtypes.common.is_datetime64_ns_dtype(df[column]):
        return df[df[column].between(init_date, end_date)]
    else:
        print('No se puede filtrar, columna no es tipo datetime')
        return df

def generate_report(
    df: pd.DataFrame,
    filas: str|List[str]|None,
    columnas: str|List[str]|None,
    valores: str|List[str],
    agg_funct: str
) -> pd.DataFrame:
    return df.pivot_table(index=filas, columns=columnas, values=valores, aggfunc=agg_funct, fill_value=0)

def save_in_database(
    df: pd.DataFrame,
    table:str,
    engine: Engine,
    if_exist: str
) -> int:
    return df.to_sql(name=table, con=engine, if_exists=if_exist)