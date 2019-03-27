import boto3, json

lambda_client = boto3.client('lambda')

class Notifier:
    def add_user_sns(user_info):
        response = lambda_client.invoke(
            FunctionName="add_user_sns",
            InvocationType='RequestResponse',
            Payload=json.dumps(user_info)
        )
