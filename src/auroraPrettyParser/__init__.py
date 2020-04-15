from json import loads
from json.decoder import JSONDecodeError

def _formatRecord(record, meta):
    r = {}
    i = 0
    values = [None if list(field.keys())[0] == 'isNull' and list(field.values())[0] else list(field.values())[0] for field in record]
    for value in values:
        try:
            value = loads(value)
        except (JSONDecodeError, TypeError):
            pass
        r[meta[i]["name"]] = value
        i += 1
    return r

# Formatting query returned Field
def parseResults(results):
    response = []
    if "columnMetadata" not in results:
        raise Exception("Query results must include columnMetada")
    for record in ("records" in results and results["records"]) or []:
        response.append(_formatRecord(record, results["columnMetadata"]))
    return response
