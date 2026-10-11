def unstable_func(value, multiplier=1):
    print("Inside unstable_func")
    raise ValueError("Temporary failure")

def transform(value, multiplier=1):
    return value * multiplier

def run_pipeline(func, *args, retries=3, **kwargs):
    retry = 0 

    if type(retries) is not int or retries < 0:
        raise ValueError

    while True:
        try:
            print("function being called")
            result = func(*args,**kwargs)
            return result
        except (ValueError):
            if retry >= retries:
                raise
            retry += 1

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0
from functools import reduce

def calculate_amount(transactions):
    completed_transactions = list(filter(lambda x: x["status"].strip().lower() == "completed", transactions))
    transaction_amount = reduce(lambda acc, x: acc+x, list(map(lambda x: to_int(x["amount"]), completed_transactions)), 0)
    return transaction_amount

from functools import wraps

def retry_decorator(retries=2):
    if type(retries) is not int or retries < 0:
        raise ValueError("retries must be a non-negative integer")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1

            while True:
                try:
                    return func(*args, **kwargs)

                except ValueError:
                    if attempt >= retries + 1:
                        print(f"Attempt {attempt} failed. No retries left.")
                        raise

                    print(
                        f"Attempt {attempt} failed. "
                        f"{retries - (attempt - 1)} retries remaining."
                    )
                    attempt += 1

        return wrapper
    return decorator


@retry_decorator(retries=5)
def fetch_data(source, limit=100):
    print(f"Fetching data: {source}, limit={limit}")
    if type(limit) is not int:
        raise ValueError("limit must be an integer")
    return {"source": source, "limit": limit}


import logging

logging.basicConfig(level=logging.INFO)

class ETLException(Exception):
    pass

def extract():
    val = int("Alice")
    return ["  Alice ", " Bob  ", "Charlie "]

def transform(data):
    return [name.strip() for name in data]

def load(data):
    return {"loaded_count": len(data)}

def run_etl():
    try:
        data = extract()
        logging.info("Extraction completed")

        transformed_data = transform(data)
        logging.info("Transformation completed")

        result = load(transformed_data)
        logging.info("Loading completed")

        return result

    except Exception as e:
        logging.exception("ETL pipeline failed")
        raise ETLException("ETL pipeline execution failed") from e

    finally:
        logging.info("ETL pipeline finished")


def transform_records(lines):
    return [line.strip().upper() for line in lines if line.strip()]

def process_file(path):
    try:
        with open(path, "r") as file:
            records = file.readlines()
            result = transform_records(records)
            logging.info("File processing succeeded")
            return result

    except FileNotFoundError as e:
        logging.exception("Input file not found")
        raise ETLException("Input file not found") from e
    
    except Exception as e:
        logging.exception("File processing failed")
        raise ETLException("File processing failed") from e
    finally:
        logging.info("File processing is completed")

def main():

    process_file(r"Python\Topicwise_Programs\Python_basics\README.md")

    # try:
    #     result = run_etl()
    #     print(result)
    # except ETLException as e:
    #     print(f"Pipeline error: {e}")

    # fetch_data("json",2000)
#     transactions = [
#     {"id": 1, "amount": "450", "status": "completed"},
#     {"id": 2, "amount": "1200", "status": "pending"},
#     {"id": 3, "amount": "invalid", "status": "completed"},
#     {"id": 4, "amount": "2500", "status": "failed"},
#     {"id": 5, "amount": "600", "status": "completed"},
#     {"id": 6, "amount": "300", "status": "completed"},
# ]

#     print(calculate_amount(transactions))
    # print(run_pipeline(unstable_func, 1, retries=1, multiplier = 4) )

if __name__ == "__main__":
    main()


    