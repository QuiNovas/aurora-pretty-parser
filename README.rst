============================
aurora_response_parser
============================

Parses aurora serverless API responses into a more usable format. Results are returned as a list of dictionaries with the column names being the key.
Nulls (returned by Aurora as isNull) are returned as None types. Any value that can be parsed as json is cast from a string to a list/dictionary.
Responses are returned formated as:

.. code-block:: JSON

  [
    {"columnOneName": "value", "columnTwoName": "value"},
    {"columnOneName": "value", "columnTwoName": "value"}
  ]

Where each item in the top level array is a separate row.

Methods
----------------------------

parseResults(records) -> list
Arguments:
records -- The records from the API query (execute_statement()["records"])

Example
----------------------------

.. code-block:: python

  from auroraPrettyParser import parseResults

  response = client.execute_statement(
      secretArn=environ["PG_SECRET"],
      database=environ["DB_NAME"],
      parameters=parameters,
      resourceArn=environ["DB_ARN"],
      includeResultMetadata=True,
      sql=sql
  )

  print(parseResults(response))
