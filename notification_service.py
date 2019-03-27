import boto3, json

lambda_client = boto3.client('lambda')

class Notifier:
    def add_user_sns(user_info):
        user_info['subscriptions'] = []
        response = lambda_client.invoke(
            FunctionName="add_user_sns",
            InvocationType='RequestResponse',
            Payload=json.dumps(user_info)
        )

    def subscribe(target_user_id, user_info):
        lambda_request = {
            'target_user_id': target_user_id,
            'user_info': user_info
        }
        response = lambda_client.invoke(
            FunctionName="add_user_subscription",
            InvocationType='RequestResponse',
            Payload=json.dumps(lambda_request)
        )
