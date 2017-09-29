"""
Sample lambda handler
"""

from src.utils import setup_logging

logger = setup_logging('serverless-sample')


def echo(event, context):
    logger.info('Received event: {}'.format(event))

    return {
        'statusCode': 200,
        'body': 'Hello World! Event was {}'.format(event)
    }

