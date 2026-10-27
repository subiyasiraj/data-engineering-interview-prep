import logging
import logging_config

logging_config.configure_logging()
logging_config.configure_logging()
logging_config.configure_logging()

log_obj = logging.getLogger(__name__)
log_obj.info("Extract file has started")