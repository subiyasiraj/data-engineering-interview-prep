# ============================================================
# 1. Global
# ============================================================

processed_records, failed_records = 0, 0


def process_batch(records):
    global processed_records, failed_records

    failed_records += sum(
        1
        for record in records
        if record["status"] == "failed"
    )

    processed_records += len(records)

    return {
        "processed": processed_records,
        "failed": failed_records
    }


# ============================================================
# 2. Nonlocal / Closure
# ============================================================

def create_batch_processor():
    processed_records, failed_records = 0, 0

    def process_batch(records):
        nonlocal processed_records, failed_records

        failed_records += sum(
            1
            for record in records
            if record["status"] == "failed"
        )

        processed_records += len(records)

        return {
            "processed": processed_records,
            "failed": failed_records
        }

    return process_batch


# ============================================================
# 3. Mutable Object vs Rebinding
# ============================================================

def update_metrics(metrics, records):
    for record in records:
        metrics["processed"] += 1

        if record["status"] == "failed":
            metrics["failed"] += 1


# ============================================================
# 4. Logical Operators / Short-Circuiting
# ============================================================

def validate_record(record):
    return (
        "status" in record
        and isinstance(record["status"], str)
        and record["status"].strip().lower() == "success"
        and "amount" in record
        and (
            isinstance(record["amount"], int)
            or isinstance(record["amount"], float)
        )
        and record["amount"] > 0
    )


# ============================================================
# 5. Bitwise Flags
# ============================================================

SCHEMA_VALID = 1 << 0
AMOUNT_VALID = 1 << 1
STATUS_VALID = 1 << 2
SOURCE_TRUSTED = 1 << 3


def add_flag(flags, flag):
    return flags | flag


def has_flag(flags, flag):
    return (flags & flag) != 0


def remove_flag(flags, flag):
    return flags & ~flag


# ============================================================
# Main
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. Test global state
    # --------------------------------------------------------

    records = [
        {"id": 101, "status": "success"},
        {"id": 102, "status": "failed"},
        {"id": 103, "status": "success"},
    ]

    print("Q1:", process_batch(records))


    # --------------------------------------------------------
    # 2. Test closure / nonlocal state
    # --------------------------------------------------------

    processor = create_batch_processor()

    print("Q2:", processor(records))


    # --------------------------------------------------------
    # 3. Test mutable dictionary
    # --------------------------------------------------------

    metrics = {
        "processed": 0,
        "failed": 0
    }

    update_metrics(metrics, records)

    print("Q3:", metrics)


    # --------------------------------------------------------
    # 4. Test logical operators
    # --------------------------------------------------------

    record = {
        "status": " SUCCESS ",
        "amount": 500
    }

    print("Q4:", validate_record(record))


    # --------------------------------------------------------
    # 5. Test bitwise flags
    # --------------------------------------------------------

    flags = 0

    flags = add_flag(flags, SCHEMA_VALID)
    flags = add_flag(flags, STATUS_VALID)

    print("Q5 flags:", flags)
    print("Schema valid:", has_flag(flags, SCHEMA_VALID))
    print("Amount valid:", has_flag(flags, AMOUNT_VALID))

    flags = remove_flag(flags, SCHEMA_VALID)

    print("After removing schema flag:", flags)


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()