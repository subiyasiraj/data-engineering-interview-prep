import extract, transform
from utils.logger import getlog

def main():
    data = extract.extract_data()
    transformed_data = transform.transform_data(data)
    print(transformed_data)
    logger = getlog()
    logger.info("ETL pipeline completed")

if __name__ == "__main__":
    main()