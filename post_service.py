import boto3, json, datetime
from random import randint

lambda_client = boto3.client('lambda')

def random_post_id():
    return randint(0, 99999)

class PostTable:
    def list_posts():
        response = lambda_client.invoke(
            FunctionName="list_posts",
            InvocationType='RequestResponse',
            Payload=json.dumps({})
        )
        posts_bytes = response['Payload'].read()
        return json.loads(posts_bytes.decode("utf-8"))['body']['items']

    def get_post(post_id):
        response = lambda_client.invoke(
            FunctionName="get_post",
            InvocationType='RequestResponse',
            Payload=json.dumps({'post_id': post_id})
        )
        post_bytes = response['Payload'].read()
        return json.loads(post_bytes.decode("utf-8"))['body']

    def create_post(form_info, user_info):
        lambda_request = {
          "id": random_post_id(),
          "user_info": user_info,
          "title": form_info['title'],
          "content": form_info['content'],
          "created_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "views": 0,
          "comments": []
        }
        caller_res = lambda_client.invoke(
            FunctionName="create_post",
            InvocationType='RequestResponse',
            Payload=json.dumps(lambda_request)
        )

    def create_comment(form_info, user_info, post_id):
        lambda_request = {
          "post_id": post_id,
          "id": random_post_id(),
          "content": form_info['content'],
          "user_info": user_info,
          "created_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        caller_res = lambda_client.invoke(
            FunctionName="create_comment",
            InvocationType='RequestResponse',
            Payload=json.dumps(lambda_request)
        )
