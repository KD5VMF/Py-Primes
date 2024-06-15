import os
import time
import logging
from sympy import isprime

# Set up logging
logging.basicConfig(filename='twin_prime.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end):
        if isprime(num) and isprime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

def save_twin_primes(twin_primes, filename):
    with open(filename, 'a') as f:
        for twin in twin_primes:
            f.write(f"{twin[0]:,}, {twin[1]:,}\n")
            logging.info(f"Saved twin prime: {twin[0]:,}, {twin[1]:,}")

def read_last_twin_prime(filename):
    if not os.path.exists(filename):
        return 1  # Start from the beginning if the file does not exist
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            return 1  # Start from the beginning if the file is empty
        last_line = lines[-1]
        last_twin = last_line.strip().split(", ")
        return int(last_twin[1].replace(',', '')) + 1

filename = "twin_primes.txt"
buffer = []

try:
    start = read_last_twin_prime(filename)
    iteration_count = 0
    while True:
        end = start + 1000  # Adjust the range as needed

        logging.info(f"Starting twin primes search from {start:,} to {end:,}")

        twin_primes = find_twin_primes(start, end)
        buffer.extend(twin_primes)

        logging.info(f"Completed twin primes search from {start:,} to {end:,}")

        # Update start for next iteration
        start = end + 1

        # Print the found twin primes
        for twin in twin_primes:
            print(f"{twin[0]:,}, {twin[1]:,}")

        iteration_count += 1

        # Save the buffer to file every 1000 iterations
        if iteration_count % 1000 == 0:
            save_twin_primes(buffer, filename)
            buffer = []  # Clear the buffer

        # Sleep for a bit to avoid overwhelming the system
        #time.sleep(1)

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")
