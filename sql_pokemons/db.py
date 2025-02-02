from sqlalchemy import create_engine, text

def row_query(sql_query):
    """
    Метод для запросов в базу данных
    :param sql_query: SQL запрос
    """
    engine = create_engine(
        'postgresql://postgres_user:rkKMi4^6e7WK&J@158.160.90.47:5432/pokemon_stable'
    )

    with engine.connect() as connection:
        result = connection.execute(text(sql_query))
        data = [row._asdict() for row in result]
    return data