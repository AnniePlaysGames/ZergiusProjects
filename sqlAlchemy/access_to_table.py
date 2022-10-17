# Ниже представлены способы доступа к возвращаемым объектам запроса к бд.
# Допустим, что у нас есть таблица person с полями name и age.
# ТК таблицы не существует, код завершится с ошибкой.

from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as connection:
    result = connection.execute(text("select * from person"))

    # Распаковываем tuple.
    for name, age in result:
        print(name, age)

    for row in result:
        print(row[0], row[1])

    # ТК tuple именованный...
    for row in result:
        print(row.name, row.age)

    # Или как к словарю.
    for row in result.mappings():
        print(row["name"], row["age"])

