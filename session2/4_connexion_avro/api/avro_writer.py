import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

def write(user):
	schema = avro.schema.parse(open("api/user.avsc", "rb").read())

	writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
	writer.append(user)
	writer.close()



