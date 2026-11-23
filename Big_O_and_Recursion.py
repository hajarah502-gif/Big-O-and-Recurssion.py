"""
Big O Notation, Complexity Analysis, and Recursion
DSA assignment source code.

 Big_o_and_recursion.py
"""

def linear_search(data, target):
    """Return the index of target using linear search, or -1 if not found.
    Time complexity: O(n); extra space: O(1).
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple")
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data, target):
    """Search a sorted list using binary search.
    Time complexity: O(log n); extra space: O(1).
    Raises ValueError if the list is not sorted in ascending order.
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple")
    if any(data[i] > data[i + 1] for i in range(len(data) - 1)):
        raise ValueError("binary_search requires data sorted in ascending order")

    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if data[middle] == target:
            return middle
        if data[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def bubble_sort(data):
    """Return a sorted copy using bubble sort.
    Time complexity: O(n^2) average/worst; O(n) best with early exit.
    Extra space: O(n) for the copied list.
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple")
    result = list(data)
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def factorial(n):
    """Calculate n! recursively.
    Time complexity: O(n); call-stack space: O(n).
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    if n in (0, 1):  # Base case stops the recursion.
        return 1
    return n * factorial(n - 1)  # Recursive case reduces the problem.


def iterative_factorial(n):
    """Calculate n! using a loop for comparison with recursion.
    Time complexity: O(n); extra space: O(1).
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    answer = 1
    for value in range(2, n + 1):
        answer *= value
    return answer


def fibonacci(n):
    """Return the nth Fibonacci number using a simple recursive definition.
    Time complexity: O(2^n) approximately; call-stack space: O(n).
    This implementation is intentionally simple for demonstrating recursion.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be zero or greater")
    if n == 0:  # First base case.
        return 0
    if n == 1:  # Second base case.
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def show_complexity_examples():
    """Print sample examples for the presentation."""
    print("BIG O NOTATION AND COMPLEXITY EXAMPLES")
    sample_data = [8, 3, 6, 1, 9, 4]

    print("\nSample data:", sample_data)
    print("Linear search for 9 (index):", linear_search(sample_data, 9))
    sorted_data = bubble_sort(sample_data)
    print("Sorted data:", sorted_data)
    print("Binary search for 6 (index in sorted data):", binary_search(sorted_data, 6))

    print("\nRECURSION EXAMPLES")
    print("Recursive factorial of 5:", factorial(5))
    print("Iterative factorial of 5:", iterative_factorial(5))
    print("Fibonacci number at position 6:", fibonacci(6))


if __name__ == "__main__":
    show_complexity_examples()
