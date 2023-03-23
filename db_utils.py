from sqlalchemy import create_engine
from sqlalchemy import text

def dataframe_to_database(df, table_name):

    # CONVERT PANDAS DATAFRAME TO A DATABASE

    # CREATE TEMPORARY DATABASE IN RAM
    engine = create_engine('sqlite:///:memory:', echo=False)

    # PUSH PANDAS DATAFRAME --> TEMPORARY DATABASE
    df.to_sql(name = table_name, con = engine, index = False)
    return engine

def handle_response(response):

    # CLEAN UP THE RESPONSE TO GET THE SQL QUERY

    query = response['choices'][0]['text']
    if query.startswith(" "):
        query = "SELECT"+query
    return query

def execute_query(engine, query):
    
    # ADD OPENAI SQL QUERY TO GET RESULTS

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()