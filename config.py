from peewee import *
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Загрузка стандартных настроек
app.config.from_object(__name__)

# Инициализация БД
db = PostgresqlDatabase(database=os.getenv('DB_NAME'), user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))

class BaseModel(Model):
    class Meta:
        database = db
