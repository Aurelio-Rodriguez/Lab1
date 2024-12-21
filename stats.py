def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else min(modes)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))
