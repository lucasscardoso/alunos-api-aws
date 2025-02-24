import json
import boto3 # Importando a biblioteca boto3 para trabalhar com os serviços da AWS
import os # Para recuperar variáveis de ambiente


bedrock_client = boto3.client("bedrock-runtime")
model_id = os.environ['MODEL_ID'] # ID do modelo de Machine Learning criado no Bedrock
prompt_title = os.environ['PROMPT_TITLE'] # Título do prompt criado no Bedrock
prompt_description = os.environ['PROMPT_DESCRIPTION'] # Descrição do prompt criado no Bedrock


def lambda_handler(event, context):
    