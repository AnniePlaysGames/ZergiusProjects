from sqlalchemy import create_engine, text

# Запросы к бд ленивые. Поэтому, чтобы зафиксировать изменения, используем commit.

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as connection:
    connection.execute(text("CREATE TABLE some_table (x int, y int)"))
    connection.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    connection.commit()

    result = connection.execute(text("select * from some_table"))
    print(result.all())
