import subprocess
import random

# Function to generate a random three-digit number as a string
def generate_random_three_digit():
    return str(random.randint(0, 999)).zfill(3)

# Generate a list of unique patterns (if you want to avoid repetition)
patterns = set(generate_random_three_digit() for _ in range(10))  # Example for 10 unique patterns

for pattern in patterns:
    cmd = f"solana-keygen grind --starts-with pow{pattern}:1000 --num-threads 120"
    subprocess.run(cmd, shell=True)
