from connexion.resolver import RestyResolver
import connexion

# items = {
#     0: {"name": "First item"}
# }
import avro_writer
import avro_reader

def add(user):
    avro_writer.write(user)

def search() -> list:
    return avro_reader.read()

if __name__ == '__main__':
    app = connexion.App(__name__, port=8080, specification_dir='swagger/')
    app.add_api('my_super_app.yaml')
    app.run()