# ==========================================
# TEST 1: Syntax Error (Missing Parenthesis)
# Expected Output: SyntaxError: unexpected EOF while parsing / '(' was never closed
# ==========================================

def calculate_total(price, tax):
    total = price + (price * tax
    return total

print("This line will never print because Python fails at compile/parse time.")

"""
Python Runtime Error Test Suite
Uncomment one line at the bottom to trigger a specific runtime error.
"""

def trigger_zero_division():
    """Triggers ZeroDivisionError"""
    result = 100 / 0


def trigger_type_error():
    """Triggers TypeError"""
    greeting = "User age: " + 25


def trigger_index_error():
    """Triggers IndexError"""
    items = ["apple", "banana", "cherry"]
    print(items[10])


def trigger_key_error():
    """Triggers KeyError"""
    config = {"host": "localhost", "port": 8080}
    print(config["database_name"])


def trigger_attribute_error():
    """Triggers AttributeError"""
    count = 42
    count.append(10)  # Integers do not have an append method


def trigger_value_error():
    """Triggers ValueError"""
    number = int("not_a_number")


def trigger_file_not_found():
    """Triggers FileNotFoundError"""
    with open("missing_config_file.json", "r") as file:
        data = file.read()


def trigger_recursion_error():
    """Triggers RecursionError (Maximum recursion depth exceeded)"""
    def infinite_loop():
        return infinite_loop()
    infinite_loop()


if __name__ == "__main__":
    print("Executing Runtime Error Test...")
    
    # --- UNCOMMENT ONE LINE AT A TIME TO TEST ---
    
    # trigger_zero_division()
    # trigger_type_error()
    # trigger_index_error()
    # trigger_key_error()
    # trigger_attribute_error()
    # trigger_value_error()
    # trigger_file_not_found()
    # trigger_recursion_error()

import traceback

def inspect_error(func):
    print(f"\n==========================================")
    print(f" Testing: {func.__name__}")
    print(f"==========================================")
    try:
        func()
        print("Result: No error occurred.")
    except Exception as e:
        print(f"Exception Caught : {type(e).__name__}")
        print(f"Error Message    : {e}")
        print("\nFull Traceback:")
        traceback.print_exc(limit=2)

if __name__ == "__main__":
    from test_runtime import (
        trigger_zero_division,
        trigger_type_error,
        trigger_index_error,
        trigger_key_error,
        trigger_attribute_error,
        trigger_value_error,
        trigger_file_not_found
    )

    test_cases = [
        trigger_zero_division,
        trigger_type_error,
        trigger_index_error,
        trigger_key_error,
        trigger_attribute_error,
        trigger_value_error,
        trigger_file_not_found
    ]

    for test in test_cases:
        inspect_error(test)