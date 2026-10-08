# Python Basics

This folder contains hands-on Python practice focused on building strong fundamentals for Data Engineering work.

The exercises are intentionally based on data-processing scenarios rather than isolated syntax drills.

---

# 07-10-2026

## Data Types, Variables, Mutation & Data Cleaning

### Topics Covered

- Python data types
- Variables
- Lists
- Dictionaries
- Mutable objects
- Copying lists
- Arithmetic operators
- Comparison operators
- List comprehensions
- String manipulation
- `strip()`
- `lower()`
- `split()`
- `None`
- `int()`
- `try/except`
- `ValueError`
- `for` loops
- `continue`
- Dictionary construction
- Input validation
- Data normalization
- Basic data-cleaning pipelines

---

## 1. Lists, Variables and Mutation

Worked with a list of numbers and calculated:

- total
- average
- values above average
- an independent copy of the original list

Important concept:

```python
original = numbers.copy()
```

creates a separate list.

The goal was to understand the difference between working with an existing mutable object and creating a new object.

---

## 2. Batch Metrics

Processed batch-level metrics such as:

```python
total_records = 1200
failed_records = 37
```

Calculated:

- successful records
- failure rate
- batch health
- large-batch status

Concepts:

- arithmetic operators
- comparison operators
- boolean expressions
- percentage calculations

---

## 3. Record Filtering and Normalization

Processed records containing inconsistent values such as:

```text
" SUCCESS "
"FAILED"
None
""
"1"
"2"
```

Used:

```python
strip()
lower()
```

to normalize string values before comparison.

Created:

- `successful_ids`
- `retryable_ids`

Important concept:

External data should be normalized before applying business logic.

---

## 4. Safe Numeric Conversion

Used:

```python
int()
```

to convert numeric strings.

Used:

```python
try:
    ...
except ValueError:
    ...
```

to prevent malformed numeric input from crashing the processing pipeline.

Production consideration:

```python
int("abc")
```

raises `ValueError`.

External data should never be assumed to be valid.

---

## 5. Raw Record Parsing

Processed pipe-delimited source records such as:

```text
101 | SUCCESS | 25
102 | failed | 10
103 | SUCCESS | 30
```

Used:

```python
split("|")
strip()
lower()
```

to transform raw strings into structured dictionaries.

Example:

```python
{
    "id": 101,
    "status": "success",
    "duration": 25
}
```

---

## 6. Validation and Cleaning Pipeline

The processing flow was:

```text
Raw record
    ↓
Split fields
    ↓
Validate field count
    ↓
Normalize strings
    ↓
Validate status
    ↓
Convert numeric fields
    ↓
Handle conversion errors
    ↓
Apply business rules
    ↓
Build cleaned record
```

Important distinction:

### Validation

Checks whether data has the expected structure and type.

### Business rule

Checks whether the value is acceptable for the particular application.

For example:

```python
duration = int(...)
```

is type conversion.

Whereas:
