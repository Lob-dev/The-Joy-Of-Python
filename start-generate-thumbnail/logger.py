import logging
import os
from datetime import datetime
from logging import handlers, Logger, Formatter
from logging.handlers import TimedRotatingFileHandler


def get_logger(tag, date) -> Logger:
    logging.basicConfig(level=logging.INFO)
    _logger: Logger = logging.getLogger(tag)

    if os.path.isdir('./log') is False:
        os.mkdir('./log')

    file_handler: TimedRotatingFileHandler = handlers.TimedRotatingFileHandler(
        filename=f'./log/{tag}.log.{date}',
        when='midnight',
        interval=1,
        encoding='UTF-8'
    )

    formatter: Formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s'
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix = "%Y%m%d"

    _logger.addHandler(file_handler)
    return _logger


logger = get_logger('logger', str(datetime.today())[:10].replace('-', ''))
