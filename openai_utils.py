import openai

def combine_prompts(fixed_sql_prompt,user_query):
    """
This function combines two strings, a fixed SQL prompt and a user query, to create a final user input.

Parameters:
fixed_sql_prompt (str): A fixed SQL prompt.
user_query (str): A user query.

Returns:
final_user_input (str): The combined strings.

    """
    
    final_user_input = f'### A query to answer: {user_query}\nSELECT'
    return fixed_sql_prompt + final_user_input


def create_table_definition_prompt(df, table_name):
    """
This function creates a table definition prompt from a given dataframe and table name.

Parameters:
df (DataFrame): The dataframe from which the table definition will be created.
table_name (str): The name of the table.

Returns:
prompt (str): A string containing the table definition.

    """

    prompt = '''### sqlite table, with it properties:
#
# {}({})   
#
'''.format(table_name,','.join(str(col) for col in df.columns))

    return prompt


def send_to_openai(prompt):
    """
This function sends a prompt to OpenAI's completion API and returns the response.

Parameters:
prompt (str): The prompt to be sent to the OpenAI API.

Returns:
response (dict): The response from the OpenAI API.
     """

    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = prompt,
        temperature = 0,
        max_tokens = 150,
        top_p = 1.0,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = ['#', ';']
    )
    return response


def user_query_input():
    """
This function allows a user to input a query about the data.

Parameters:
    None

Returns:
    user_input (str): The query input by the user.

    """

    user_input = input("Tell OpenAi what you want to know about the data: ")
    return user_input
