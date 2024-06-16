import os
import time
import logging
from sympy import isprime

# Set up logging
logging.basicConfig(filename='prime_quadruple.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_prime_quadruples(start, end):
    prime_quadruples = []
    for num in range(start, end):
        if isprime(num) and isprime(num + 2) and isprime(num + 6) and isprime(num + 8):
            prime_quadruples.append((num, num + 2, num + 6, num + 8))
    return prime_quadruples

def save_prime_quadruples(prime_quadruples, filename):
    with open(filename, 'a') as f:
        for quadruple in prime_quadruples:
            f.write(f"{quadruple[0]:,}, {quadruple[1]:,}, {quadruple[2]:,}, {quadruple[3]:,}\n")
            logging.info(f"Saved prime quadruple: {quadruple[0]:,}, {quadruple[1]:,}, {quadruple[2]:,}, {quadruple[3]:,}")

def read_last_prime_quadruple(filename):
    if not os.path.exists(filename):
        return 1  # Start from the beginning if the file does not exist
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            return 1  # Start from the beginning if the file is empty
        last_line = lines[-1]
        last_quadruple = last_line.strip().split(", ")
        return int(last_quadruple[3].replace(',', '')) + 1

filename = "prime_quadruples.txt"
buffer = []

try:
    start = read_last_prime_quadruple(filename)
    iteration_count = 0
    while True:
        end = start + 1000  # Adjust the range as needed

        logging.info(f"Starting prime quadruples search from {start:,} to {end:,}")

        prime_quadruples = find_prime_quadruples(start, end)
        buffer.extend(prime_quadruples)

        logging.info(f"Completed prime quadruples search from {start:,} to {end:,}")

        # Update start for next iteration
        start = end + 1

        # Print the found prime quadruples
        for quadruple in prime_quadruples:
            print(f"{quadruple[0]:,}, {quadruple[1]:,}, {quadruple[2]:,}, {quadruple[3]:,}")

        iteration_count += 1

        # Save the buffer to file every 1000 iterations
        if iteration_count % 1000 == 0:
            save_prime_quadruples(buffer, filename)
            buffer = []  # Clear the buffer

        # Sleep for a bit to avoid overwhelming the system
        #time.sleep(1)

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")
