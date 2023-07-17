import numpy

# Set the desired number of samples
number_of_samples = 20

# Set the mean wait time
mean_wait_time = 2

# Generate 20 samples from the exponential distribution
generated_wait_time_samples = numpy.random.default_rng().exponential(scale=mean_wait_time, size=number_of_samples)

# Print the samples
print(generated_wait_time_samples)

# Convert the array of samples to boolean values (1 if sample is less than 2, 0 otherwise)
is_sample_less_than_two = generated_wait_time_samples < 2

# Calculate the number of samples less than 2
number_of_samples_less_than_two = is_sample_less_than_two.sum()

# Estimate the probability that any given sample wait time will be less than 2
prob_sample_less_than_two = number_of_samples_less_than_two/number_of_samples

# Print out the estimated probability
print(prob_sample_less_than_two)