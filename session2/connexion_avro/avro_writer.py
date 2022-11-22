import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

def write(user):
	schema = avro.schema.parse(open("user.avsc", "rb").read())

	writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
	writer.append(user)
	#writer.append({"name": "First Item", "id": 0})
	#writer.append({"name": "Second Item"})
	writer.close()



