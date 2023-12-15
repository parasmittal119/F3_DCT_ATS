def countsubseq(s):
    # Convert string to a list of integers
    nums = [int(x) for x in s]
    n = len(nums)

    # Initialize a list to store counts for each digit
    counts = [0] * 10

    # Iterate through each digit in the string
    for i in range(n):
        # Increment the count for the current digit
        counts[nums[i]] += 1

        # For each digit less than nums[i],
        # add the count of subsequences ending with that digit
        for j in range(nums[i]):
            counts[nums[i]] += counts[j]

    # Sum up counts for all digits to get total subsequences
    return sum(counts)


# Example usage:
s = "1123"
result = countsubseq(s)
print(f"The number of non-empty subsequences: {result}")
