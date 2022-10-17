from sqlalchemy import create_engine, text

# Создаём объект движка для взаимодействия с бд.
# Параметры соединения передаём ввиде строки.
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Устанавливаем соединение с бд и выполняем к ней запрос.
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
