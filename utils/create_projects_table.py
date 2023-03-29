import boto3


import os

# Set up the DynamoDB client
boto3.setup_default_session(profile_name=os.environ['PROFILE_NAME'])
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Define the table schema
table_name = 'projects'
key_schema = [
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'  # Partition key
    }

]
attribute_definitions = [
    {
        'AttributeName': 'id',
        'AttributeType': 'S'  # String
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput=provisioned_throughput
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
print(f'Table {table_name} created successfully.')
