import json
import boto3 # Importando a biblioteca boto3 para trabalhar com os serviços da AWS
import os # Para recuperar variáveis de ambiente

rekognition_client = boto3.client("rekognition") # Instanciando o cliente do Rekognition
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    
    # Captura do Evento de Put do Amazon S3
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(event)
    print(bucket_name)
    print(file_name)

    # Chama do evento de detecção de labels do rekognition
    response = rekognition_client.detect_labels(
        Image={'S3Object': {'Bucket':bucket_name, 'Name': file_name }},
        MaxLabels=10,
        MinConfidence=80
    )
    
    # Lista de labels detectadas
    labels = [label['Name'] for label in response['Labels']]
    
    print(labels)
    
    sqs_client.send_message(
        QueueUrl=os.environ['SQS_URL'],
        MessageBody=json.dumps({
            'bucket': bucket_name,
            'key': file_name,
            'labels': labels
        })
    )
    