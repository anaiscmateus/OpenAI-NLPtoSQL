# DATASET: https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

import os 
import logging
import pandas as pd
import openai
import db_utils
import openai_utils

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# SET UP API KEY
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Sales Dataset
dataset = r"C:\Users\anais\Documents\Projects\OpenAI\OpenAI_NLP_to_SQL\OpenAI-NLPtoSQL\data\sales_data_sample.csv"

if __name__ == '__main__':
    logging.info("Loading Data...")
    df = pd.read_csv(dataset)
    logging.info(f"Data Format: {df.shape}")

    logging.info("Converting to database...")
    database = db_utils.dataframe_to_database(df, 'Results')

    fixed_sql_prompt = openai_utils.create_table_definition_prompt(df, 'Results')
    logging.info(f'Fixed SQL Prompt: {fixed_sql_prompt}')

    logging.info("Waiting for user input...")
    user_input = openai_utils.user_query_input()
    final_prompt = openai_utils.combine_prompts(fixed_sql_prompt, user_input)
    logging.info(f'Final prompt: {final_prompt}')

    logging.info("Sending to OpenAI...")
    response = openai_utils.send_to_openai(final_prompt)
    proposed_query = response['choices'][0]['text']
    proposed_query_postprocessed = db_utils.handle_response(response)
    logging.info(f'Response obtained. Proposed sql query: {proposed_query_postprocessed}')
    result = db_utils.execute_query(database, proposed_query_postprocessed)
    logging.info(f'Result: {result}')
    print(result)