import logging
import logging.handlers

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"


def configure_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    existing = {h.get_name() for h in root.handlers}
    formatter = logging.Formatter(LOG_FORMAT)

    if "pipeline_file" not in existing:
        fh = logging.handlers.RotatingFileHandler(
            "pipeline.log", maxBytes=1024 * 1024, backupCount=3
        )
        fh.set_name("pipeline_file")
        fh.setFormatter(formatter)
        root.addHandler(fh)

    if "pipeline_console" not in existing:
        sh = logging.StreamHandler()
        sh.set_name("pipeline_console")
        sh.setFormatter(formatter)
        root.addHandler(sh)