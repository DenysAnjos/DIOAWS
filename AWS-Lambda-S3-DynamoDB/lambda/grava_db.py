import json
import os
import boto3
from decimal import Decimal
from datetime import datetime
from urllib.parse import unquote_plus


ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", "http://localhost.localstack.cloud:4566")
REGION = os.environ.get("AWS_REGION", "us-east-1")
TABLE_NAME = os.environ.get("TABLE_NAME", "NotasFiscais")


def to_decimal(value):
    return Decimal(str(value))


def lambda_handler(event, context):
    print("Evento recebido:")
    print(json.dumps(event))

    s3 = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        region_name=REGION
    )

    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url=ENDPOINT_URL,
        region_name=REGION
    )

    table = dynamodb.Table(TABLE_NAME)

    registros_processados = 0

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])

        print(f"Lendo arquivo: s3://{bucket}/{key}")

        response = s3.get_object(Bucket=bucket, Key=key)
        conteudo = response["Body"].read().decode("utf-8")

        notas = json.loads(conteudo, parse_float=to_decimal)

        if isinstance(notas, dict):
            notas = [notas]

        for nota in notas:
            item = {
                "id": str(nota["id"]),
                "cliente": str(nota.get("cliente", "")),
                "valor": Decimal(str(nota.get("valor", 0))),
                "data_emissao": str(nota.get("data_emissao", "")),
                "arquivo_origem": key,
                "processado_em": datetime.utcnow().isoformat()
            }

            table.put_item(Item=item)
            registros_processados += 1

            print(f"Nota fiscal salva no DynamoDB: {item['id']}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensagem": "Processamento concluído",
            "registros_processados": registros_processados
        })
    }
