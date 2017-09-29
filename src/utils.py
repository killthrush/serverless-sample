import logging
import os


def setup_logging(name, level='INFO'):
    lambda_format = (
        '%(asctime)s.%(msecs)-3d (Z)\t%(aws_request_id)s\t'
        '[%(levelname)s]\t%(message)s\n'
    )
    data_format = '%Y-%m-%d %H:%M:%S'

    # Ensure root logger is setup correctly, see https://github.com/serverless/serverless/issues/1796
    logger = logging.getLogger()
    for hand in [h for h in logger.handlers]:
        hand.setFormatter(logging.Formatter(lambda_format, datefmt=data_format))

    # Configure named logger correctly as well
    logger = logging.getLogger(name)
    for hand in [h for h in logger.handlers]:
        hand.setFormatter(logging.Formatter(lambda_format, datefmt=data_format))
    else:
        logging.basicConfig(format='%(asctime)s.%(msecs)-3d (Z)\t[%(levelname)s]\t%(message)s\n',
                            datefmt=data_format)

    log_level = os.environ.get('LOG_LEVEL', level)
    logger.setLevel(logging.getLevelName(log_level))

    # populate the custom value that AWS Lambda injects so local testing is possible
    logger = logging.LoggerAdapter(logger, {'aws_request_id': 'LOCAL'})
    return logger