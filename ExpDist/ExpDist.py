import random
import numpy as np

def generate_samples():
    # Rate parameter
    rate = 1/2

    # Generate 10 samples
    samples = []
    for i in range(50):
        # Generate a random number
        random_number = random.random()

        # Calculate the sample time
        sample_time = -np.log(random_number) / rate

        # Add the sample time to the list
        samples.append(sample_time)

    return samples

# Generate samples
samples = generate_samples()

# Print the samples
print(samples)