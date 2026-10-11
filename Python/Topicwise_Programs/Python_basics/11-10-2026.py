
# ============================================================
# 1. FUNCTIONS AND RETRY PIPELINE
# ============================================================

def unstable_func(value, multiplier=1):
    print("Inside unstable_func")
    raise ValueError("Temporary failure")


def transform(value, multiplier=1):
    return value * multiplier


def run_pipeline(func, *args, retries=3, **kwargs):
    if type(retries) is not int or retries < 0:
        raise ValueError("retries must be a non-negative integer")

    retry = 0

    while True:
        try:
            print("Function being called")
            return func(*args, **kwargs)

        except ValueError:
            if retry >= retries:
                raise

            retry += 1
            print(f"Retrying: {retry}/{retries}")


# ============================================================
# 2. TRANSACTION PROCESSING
# ============================================================

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def calculate_amount(transactions):
    completed_transactions = (
        transaction
        for transaction in transactions
        if transaction["status"].strip().lower() == "completed"
    )

    return sum(
        to_int(transaction["amount"])
        for transaction in completed_transactions
    )


# ============================================================
# 3. RETRY DECORATOR AND DATA FETCHING
# ============================================================

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

                    remaining = retries - (attempt - 1)
                    print(
                        f"Attempt {attempt} failed. "
                        f"{remaining} retries remaining."
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


# ============================================================
# 4. ETL PIPELINE AND EXCEPTION HANDLING
# ============================================================

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ETLException(Exception):
    """Raised when an ETL operation fails."""


def extract():
    # Replace this with your actual extraction logic.
    return ["  Alice ", " Bob  ", "Charlie "]


def transform_data(data):
    return [name.strip() for name in data]


def load(data):
    return {"loaded_count": len(data)}


def run_etl():
    try:
        data = extract()
        logging.info("Extraction completed")

        transformed_data = transform_data(data)
        logging.info("Transformation completed")

        result = load(transformed_data)
        logging.info("Loading completed")

        return result

    except Exception as exc:
        logging.exception("ETL pipeline failed")
        raise ETLException("ETL pipeline execution failed") from exc

    finally:
        logging.info("ETL pipeline finished")


# ============================================================
# 5. FILE PROCESSING
# ============================================================

def transform_records(lines):
    return [
        line.strip().upper()
        for line in lines
        if line.strip()
    ]


def process_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            records = file.readlines()

        result = transform_records(records)
        logging.info("File processing succeeded")
        return result

    except FileNotFoundError as exc:
        logging.exception("Input file not found")
        raise ETLException("Input file not found") from exc

    except Exception as exc:
        logging.exception("File processing failed")
        raise ETLException("File processing failed") from exc

    finally:
        logging.info("File processing finished")


# ============================================================
# 6. PYTHONIC DATA CLEANING
# ============================================================

def clean_records(records):
    return [
        {
            **record,
            "name": record["name"].strip(),
            "age": 0 if record["age"] is None else record["age"],
        }
        for record in records
        if record["active"] is True
    ]


# ============================================================
# 7. CUSTOMER TRANSACTION RECONCILIATION
# ============================================================

def reconcile_totals(customer_ids, totals):
    return {
        customer_id: total
        for customer_id, total in zip(
            customer_ids,
            totals,
            strict=True,
        )
        if total != 0
    }


# ============================================================
# 8. MAIN ENTRY POINT
# ============================================================

def main():
    # Example 1: Retry pipeline
    # print(run_pipeline(unstable_func, 1, retries=1, multiplier=4))

    # Example 2: Fetch data using a retry decorator
    # print(fetch_data("json", limit=2000))

    # Example 3: Calculate completed transaction totals
    # transactions = [
    #     {"id": 1, "amount": "450", "status": "completed"},
    #     {"id": 2, "amount": "1200", "status": "pending"},
    #     {"id": 3, "amount": "invalid", "status": "completed"},
    #     {"id": 4, "amount": "2500", "status": "failed"},
    #     {"id": 5, "amount": "600", "status": "completed"},
    #     {"id": 6, "amount": "300", "status": "completed"},
    # ]
    # print(calculate_amount(transactions))

    # Example 4: Run the ETL pipeline
    # try:
    #     print(run_etl())
    # except ETLException as exc:
    #     print(f"Pipeline error: {exc}")

    # Example 5: Process a file
    # print(process_file("README.md"))

    # Example 6: Clean customer records
    # records = [
    #     {"name": " Alice ", "age": 30, "active": True},
    #     {"name": " Bob ", "age": None, "active": False},
    #     {"name": " Charlie ", "age": 25, "active": True},
    #     {"name": " Diana ", "age": 28, "active": True},
    # ]
    # print(clean_records(records))

    # Example 7: Reconcile customer totals
    customer_ids = [101, 102, 103, 104, 105]
    totals = [250.0, 0.0, 475.5, 120.0, 0.0]

    print(reconcile_totals(customer_ids, totals))


if __name__ == "__main__":
    main()
