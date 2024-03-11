
import json
import boto3

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table_name = 'my-serverless-table'
        table = dynamodb.Table(table_name)

        operation = event.get('operation')
        payload = event.get('payload')

        if operation == 'create':
            table.put_item(Item=payload.get('Item'))
            return {"statusCode": 200}

        if operation == 'read':
            Table_Number = payload.get('Item').get('id')
            response = table.get_item(Key={'id': Table_Number})
            item = response.get('Item')
            return {"statusCode": 200}

        if operation == 'update':
            Table_Number = payload.get('Item').get('id')
            Letter = 'H'
            table.update_item(Key={'id': Table_Number},{'Letter': Letter})
            return {"statusCode": 200}

        if operation == 'delete':
            Table_Number = payload.get('Item').get('id')
            table.delete_item(Key={'id': Table_Number})
            return {"statusCode": 200}


    except Exception as e:
        return {"statusCode": 500}


   