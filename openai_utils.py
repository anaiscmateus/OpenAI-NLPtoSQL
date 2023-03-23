import openai

def create_table_definition_prompt(df, table_name):

    # CREATE TABLE DEFINITION FROM A DATAFRAME

    prompt = '''### sqlite table, with it properties:
#
# {}({})   
#
'''.format(table_name,','.join(str(col) for col in df.columns))

    return prompt

def user_query_input():

    # ACCEPT INPUT FROM A NON TECHNICAL USER

    user_input = input("Tell OpenAi what you want to know about the data: ")
    return user_input

def combine_prompts(fixed_sql_prompt,user_query):
    
    # COMBINE THE PROMPTS ABOVE TO GET THE OPENAI PROMPT
    
    final_user_input = f'### A query to answer: {user_query}\nSELECT'
    return fixed_sql_prompt + final_user_input

def send_to_openai(prompt):
    
    # PASS THE PROMPT TO THE COMPLETION CREATE WITH STOP TOKEN

    response = openai.Completion.create(
        model = 'code-davinci-002',
        prompt = prompt,
        temperature = 0,
        max_tokens = 150,
        top_p = 1.0,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = ['#', ';']
    )
    return response