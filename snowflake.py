# https://pypi.org/project/snowflake-snowpark-python/

# set up
# pip install "snowflake-snowpark-python[pandas]"

# source code: https://github.com/snowflakedb/snowpark-python/tree/main/src/snowflake/snowpark

from snowflake.snowpark import Session

connection_parameters = {
    "account": "se01634.central-india.azure",
    "user": "",
    "password": "",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "TESTDB",
    "schema": "PUBLIC"
}

# def bin_age(age):
#     if age > 60:
#         return 'OLD'
#     elif age > 30:
#         return 'YOUNG'
#     else:
#         return 'TEEN'
#

session = Session.builder.configs(connection_parameters).create()
df = session.table('test_t')
df.write.saveAsTable('dup_t')
df.show()

# df = session.create_dataframe([[1, 2], [3, 4]], schema=["a", "b"])
# df = df.filter(df.a > 1)
# df.show()
# pandas_df = df.to_pandas()  # this requires pandas installed in the Python environment
# result = df.collect()
