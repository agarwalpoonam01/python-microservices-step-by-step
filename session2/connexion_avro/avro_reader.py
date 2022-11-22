from avro.datafile import DataFileReader
from avro.io import DatumReader
import json
def read():
    test = {}
    reader = DataFileReader(open("users.avro", "rb"), DatumReader())
    for user in reader:
        print(user)
        test.update(user)

    reader.close()
    return(json.dumps(test))

