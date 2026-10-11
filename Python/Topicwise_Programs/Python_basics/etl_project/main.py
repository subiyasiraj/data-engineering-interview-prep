import extract
import transform
from utils.logger import get_logger

def main():
    logger = get_logger(__name__)

    data = extract.extract_data()
    transformed_data = transform.transform_data(data)

    print(transformed_data)
    logger.info("ETL pipeline completed")

if __name__ == "__main__":
    main()