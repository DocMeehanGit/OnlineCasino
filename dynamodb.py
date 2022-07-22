"""
Author: Wyatt Meehan
Created on 6/5/2022

This class represents an AWS DyanmoDB client
and encapsulates DynamoDB related functionality
"""

class DynamoDB:
    """Encapsulates DynamoDB related functions."""
    
    def __init__(self, dynamodb_client, table_name, dynamodb_key):
        self.dynamodb_client = dynamodb_client
        self.table_name = table_name
        self.dynamodb_key = dynamodb_key
        
    def delete_dynamodb_item(self, username):
        try:
            self.dynamodb_client.delete_item(
                TableName=self.table_name,
                Key={self.dynamodb_key: {'S' : username}})
            print('DynamoDB entry deleted: [%s]', username)
        except Exception as e:
            print(e)
            raise Exception('Error while deleteing DynamoDB item: [%s]', str(e))
            
    def ddb_get_item(self, username):
        try:
            ddb_item = self.dynamodb_client.get_item(
                TableName=self.table_name,
                Key={
                    self.dynamodb_key:{'S': str(username)}
                })
            return ddb_item
        except Exception as e:
            print(e)
            raise Exception('Error while getting DynamoDB item: [%s]', str(e))
    
    def ddb_update_balance(self, username, balance):
        try:
            self.dynamodb_client.update_item(
                TableName=self.table_name,
                Key={
                    self.dynamodb_key:{'S': str(username)}
                },
                UpdateExpression='set Balance = :b',
                ExpressionAttributeValues={
                    ':b' : {'S' : str(balance)}
                })
        except Exception as e:
            print(e)
            raise Exception('Error while updating DynamoDB item: [%s]', str(e))
            