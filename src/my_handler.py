"""
Sample lambda handler
"""

from src.utils import setup_logging

logger = setup_logging('serverless-sample')


def test_handler_1(event, context):
    logger.info('Received event: {}'.format(event))
