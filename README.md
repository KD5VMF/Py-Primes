# Twin Primes Finder

This project is a Python script that finds twin primes within a specified range and saves them to a file. Twin primes are pairs of prime numbers that differ by exactly two. For example, (3, 5) and (11, 13) are twin primes. The script continuously searches for twin primes, logging the results and resuming from the last found pair.

Features
Efficient Prime Checking: Utilizes the sympy library for efficient prime number validation.
Continuous Operation: The script runs in an infinite loop, continuously finding twin primes within incrementing ranges.
Persistent Storage: Twin primes are saved to a text file, allowing the script to resume from the last found pair upon restart.
Detailed Logging: Logs the start and end of each search range, as well as each twin prime found, to a log file for easy debugging and tracking.
