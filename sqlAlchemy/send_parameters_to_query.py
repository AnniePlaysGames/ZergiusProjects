from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Выполним запрос insert, вставляя данные в несуществующую таблицу.

with engine.connect() as connection:
    connection.execute(
        text(
            "insert into person (name, age) values (:name,:age)"
        ),
        {"name": "Test", "age": 0}
    )

    # Если Нужно создать сразу несколько строк, то передаём словари с параметрами одним списком.

    connection.execute(
        text(
            "insert into person (name, age) values (:name, :age)"
        ),
        {
            {"name": "test1", "age": 01},
            {"name": "test2", "age": 02}
        }
    )
