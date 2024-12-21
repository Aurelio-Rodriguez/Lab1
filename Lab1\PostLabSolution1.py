# stats.py

def mean(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:  # Even number of elements
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:  # Odd number of elements
        return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]

    if len(modes) == len(numbers):
        return None  # Every number appears with the same frequency (no mode)
    return modes[0]  # Return the first mode found

# Example usage
if __name__ == "__main__":
    # Prompt user for input
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    # Convert input string to a list of numbers
    try:
        data = list(map(float, user_input.split()))
        
        print("Mean:", mean(data))
        print("Median:", median(data))
        print("Mode:", mode(data))
    except ValueError as e:
        print("Error:", e)
