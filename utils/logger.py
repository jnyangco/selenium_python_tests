import logging
import os
from config.config import TestConfig


def setup_logger():
    """Setup logger configuration"""
    config = TestConfig()

    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logger
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("Logger configured successfully")
    return logger