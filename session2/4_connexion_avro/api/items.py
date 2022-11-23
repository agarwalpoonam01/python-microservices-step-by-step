from api import avro_writer
from api import avro_reader

def post(user):
    avro_writer.write(user)

def search() -> list:
    return avro_reader.read()