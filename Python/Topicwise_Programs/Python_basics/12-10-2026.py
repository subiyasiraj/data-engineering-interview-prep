
import logging
from pathlib import Path
from time import perf_counter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)


def file_count(path: str | Path) -> int:
    """Count non-empty, non-whitespace lines in a UTF-8 text file."""
    file_path = Path(path)
    start_time = perf_counter()

    logger.info("Starting file count: %s", file_path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            count = sum(1 for line in file if line.strip())

        duration = perf_counter() - start_time
        logger.info(
            "File count completed: path=%s count=%d duration=%.3fs",
            file_path,
            count,
            duration,
        )
        return count

    except (OSError, UnicodeError):
        logger.exception("File count failed: %s", file_path)
        raise

import datetime
from zoneinfo import ZoneInfo

def format_datetime(datestamp):
    
    
    return datetime.datetime.strptime(datestamp,'%Y-%m-%dT%H:%M:%S%z')

def time_zone_unaware(naive_time_stamp):
    dt = datetime.datetime.strptime(naive_time_stamp, "%Y-%m-%d %H:%M:%S")
    return dt.replace(tzinfo=ZoneInfo("America/New_York"))

import re

def extract_info(str1):
    # match = re.search(r"(?P<date>[\d-]+)[\s]+(?P<log_level>[\w]+)[\s]+user_id=(?P<user_id>[\d]{4})[\s]+action=(?P<action>[\w]+)",str1)
    # print(match.group("date"),match.group("log_level"),match.group("user_id"),match.group("action"))

    split_string = re.compile(r"[,;|]+")
    print(split_string.split(f"alice,,bob; charlie|david"))
    try:
        match = re.match(r"[A-Z0-9]{6,10}$", str1)
        print(match.group())
    except Exception as e:
        print("nothing matches")



def main() -> None:
    str1 = 'ANA123 '

    extract_info(str1)



    # datestamp = '2026-10-15T09:30:00+05:30'
    # naive_time_stamp = '2026-11-01 01:30:00'

    

    # resolved_time = format_datetime(datestamp)
    # print(resolved_time,resolved_time + datetime.timedelta(days = 5))
    # print(time_zone_unaware(naive_time_stamp))

    # path = Path(
    #     r"Python\Topicwise_Programs\Python_basics\README.md"
    # )

    # try:
    #     count = file_count(path)
    #     print(f"Non-empty lines: {count}")
    # except (OSError, UnicodeError) as exc:
    #     logger.error("Unable to process input file: %s", exc)
    #     raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
