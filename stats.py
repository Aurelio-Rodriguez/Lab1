def mean(numbers):
    """
    Compute the mean (average) of a list of numbers.

    :param numbers: List of numbers
    :return: Mean of the numbers
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Compute the median of a list of numbers.

    :param numbers: List of numbers
    :return: Median of the numbers
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_numbers[midpoint]
    else:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

def mode(numbers):
    """
    Compute the mode of a list of numbers.

    :param numbers: List of numbers
    :return: Mode of the numbers
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")

    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_frequency]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes  # Return a list of modes if there's a tie

if __name__ == "__main__":
    # Example usage
    sample_numbers = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8]
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))
