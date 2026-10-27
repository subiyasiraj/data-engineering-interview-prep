import logging
import logging_config

logging_config.configure_logging()
logging_config.configure_logging()
logging_config.configure_logging()

log_obj = logging.getLogger("extract")
log_obj.info("Extract file has started")