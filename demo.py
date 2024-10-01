def process_numbers(numbers):
    processed_numbers = []
    for number in numbers:
        incremented = number + 5
        decremented = incremented - 3
        processed_numbers.append(decremented)
    return processed_numbers

# Main program
if __name__ == "__main__":
    numbers = []
    
    # Input 5 numbers from the user
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Process the numbers
    result = process_numbers(numbers)

    # Display the results
    print("Processed numbers (incremented by 5 and then decremented by 3):")
    for original, processed in zip(numbers, result):
        print(f"{original} -> {processed}")
