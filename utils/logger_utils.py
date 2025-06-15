import logging
import os
from config.test_config import TestConfig

# Global flag to ensure we only configure logging once
_logger_configured = False

def setup_logger(name=None):
    """Setup logger configuration - call once at application startup"""
    global _logger_configured

    if not _logger_configured:
        config = TestConfig()

        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(config.LOG_FILE)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure root logger
        logging.basicConfig(
            level=getattr(logging, config.LOG_LEVEL),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(config.LOG_FILE),
                logging.StreamHandler()
            ],
            force=True # Override any existing configuration
        )
        _logger_configured = True

    # Return a logger for the specific module
    logger_name = name if name else __name__
    logger = logging.getLogger(logger_name)
    return logger


def get_logger(name=None):
    """Get a logger instance for any module"""
    # Ensure logging is configured
    if not _logger_configured:
        setup_logger()

    logger_name = name if name else __name__
    return logging.getLogger(logger_name)

