# ============================================================
# 07-10-2026
# Python Basics: Data Types, Variables, Mutation & Data Cleaning
# ============================================================


# ============================================================
# Problem 1: Data Types + Variables + Mutation
# ============================================================

# Given:
# numbers = [10, 20, 30, 40, 50]
#
# Create:
# 1. total -> sum of all numbers
# 2. average -> average of the numbers
# 3. above_average -> numbers greater than average
# 4. original -> must remain unchanged

numbers = [10, 20, 30, 40, 50]

original = numbers.copy()

total = sum(numbers)
average = total / len(numbers)

above_average = [n for n in numbers if n > average]


# ============================================================
# Problem 2: Batch Metrics
# ============================================================

# Given:
# total_records = 1200
# failed_records = 37
#
# Create:
# successful_records
# failure_rate
# is_healthy -> True if failure rate < 5%
# is_large_batch -> True if total records >= 1000

total_records = 1200
failed_records = 37

successful_records = total_records - failed_records
failure_rate = failed_records / total_records * 100

is_healthy = failure_rate < 5
is_large_batch = total_records >= 1000

print(successful_records)
print(failure_rate)
print(is_healthy)
print(is_large_batch)


# ============================================================
# Problem 3: Record Filtering and Normalization
# ============================================================

# Requirements:
# successful_ids:
#   IDs whose normalized status is exactly "success"
#
# retryable_ids:
#   status is not "success"
#   AND retries is a valid integer
#   AND retries < 3
#
# Handle:
# - whitespace
# - uppercase/lowercase
# - None
# - empty strings
# - numeric strings
# - invalid numeric values
#
# Do not modify the original records.

records = [
    {"id": "101", "status": " SUCCESS ", "retries": "1"},
    {"id": "102", "status": "failed", "retries": "2"},
    {"id": "103", "status": " SUCCESS", "retries": None},
    {"id": "104", "status": "", "retries": "0"},
    {"id": "105", "status": None, "retries": "1"},
    {"id": "106", "status": "FAILED", "retries": "3"},
]

successful_ids = [
    record["id"]
    for record in records
    if record["status"] is not None
    and record["status"].lower().strip() == "success"
]

retryable_ids = [
    record["id"]
    for record in records
    if (
        (record["status"] is None
         or record["status"].lower().strip() != "success")
        and int(record["retries"]) < 3
    )
]

print(successful_ids, retryable_ids)


# ============================================================
# Problem 4: Raw Record Cleaning
# ============================================================

# Each raw record is expected to follow:
#
# id | status | duration
#
# Keep only records where:
# - id is a valid integer
# - status is normalized
# - status is either "success" or "failed"
# - duration is a valid integer
#
# Do not modify the original records.

records = [
    " 101 | SUCCESS | 25 ",
    "102| failed|10",
    " 103|SUCCESS| 30",
    "104 | FAILED |abc",
    "105| success |",
    "106|SUCCESS| 40 ",
    "107|SUCCESS",
    "108|SUCCESS|0",
    "109|UNKNOWN|20",
    "110|SUCCESS|abc",
    "111|SUCCESS|-5",
    "112|SUCCESS| 15 ",
]

cleaned_records = []

for raw_record in records:

    # 1. Split raw record into fields
    fields = raw_record.split("|")

    # 2. Validate number of fields
    if len(fields) != 3:
        continue

    # 3. Normalize status
    status = fields[1].strip().lower()

    # 4. Validate status
    if status not in {"success", "failed"}:
        continue

    # 5. Convert numeric fields safely
    try:
        record_id = int(fields[0].strip())
        duration = int(fields[2].strip())
    except ValueError:
        continue

    # 6. Apply business rule
    if duration < 0:
        continue

    # 7. Build cleaned record
    cleaned_records.append(
        {
            "id": record_id,
            "status": status,
            "duration": duration,
        }
    )

print(cleaned_records)