```python
from statistics import mean


# ==================================================
# 1. FLEXIBLE AGGREGATION FUNCTION
# Concepts: *args, dictionaries, functions, validation
# ==================================================

def aggregate_numbers(*args, operation="sum"):
    operations = {
        "sum": sum,
        "max": max,
        "min": min,
        "avg": mean,
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    if not args:
        raise ValueError("At least one number must be provided")

    return operations[operation](args)


# ==================================================
# 2. CLOSURE-BASED COUNTER
# Concepts: Nested functions, closures, nonlocal
# ==================================================

def make_counter(start=0):
    counter = start

    def counter_increment():
        nonlocal counter
        counter += 1
        return counter

    return counter_increment


# ==================================================
# 3. LOGGING DECORATOR
# Concepts: Decorators, *args, **kwargs
# ==================================================

def log_execution(func):
    def agg_func(*args, **kwargs):
        print(f"{func.__name__} starting")

        result = func(*args, **kwargs)

        print(f"{func.__name__} finished")
        return result

    return agg_func


@log_execution
def calculate_total(a, b):
    return a + b


# ==================================================
# 4. GENERATOR-BASED RECORD PROCESSING
# Concepts: Generators, yield, exception handling
# ==================================================

def valid_high_value_records(records, threshold=100):
    for record in records:
        try:
            amount = int(record["amount"])
        except (ValueError, KeyError, TypeError):
            continue

        if amount >= threshold:
            yield record


# ==================================================
# 5. MAIN FUNCTION
# ==================================================

def main():

    records = [
        {"id": 1, "amount": "100"},
        {"id": 2, "amount": "250"},
        {"id": 3, "amount": "invalid"},
        {"id": 4, "amount": "50"},
        {"id": 5, "amount": "300"},
    ]

    # Generator example
    print("\n--- High-Value Records ---")

    for record in valid_high_value_records(
        records,
        threshold=100
    ):
        print(record)

    # Decorator example
    # print("\n--- Logging Decorator ---")
    # print(calculate_total(4, 5))

    # Closure example
    # print("\n--- Counter ---")
    # counter_a = make_counter(5)
    # counter_b = make_counter()
    #
    # print(counter_a())  # 6
    # print(counter_a())  # 7
    # print(counter_b())  # 1
    # print(counter_a())  # 8

    # Aggregation examples
    # print("\n--- Aggregation ---")
    # print(aggregate_numbers(10, 20, 30))                   # 60
    # print(aggregate_numbers(10, 20, 30, operation="min"))  # 10
    # print(aggregate_numbers(10, 20, 30, operation="max"))  # 30
    # print(aggregate_numbers(10, 20, 30, operation="avg"))  # 20


# ==================================================
# 6. PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":
    main()


# ==================================================
# LEARNING NOTES
# ==================================================
#
# 1. Aggregation:
#    *args collects positional arguments into a tuple.
#
# 2. Closures:
#    nonlocal allows the nested function to update
#    the counter defined in the enclosing function.
#
# 3. Decorators:
#    A decorator wraps a function to add behavior
#    without changing its original implementation.
#
# 4. Generators:
#    yield returns qualifying records one at a time.
#    Invalid amounts are skipped without crashing.
#
# Production consideration:
#    Track or log invalid records rather than silently
#    discarding data in a real pipeline.

