from avro.datafile import DataFileReader
from avro.io import DatumReader
import json
test = {}
reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
    test.update(user)

reader.close()
print(json.dumps(test))