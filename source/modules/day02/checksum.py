def process(freqs):
    """
    Given an array of freqs
    get the checksum
    """
    sum_count2 = 0
    sum_count3 = 0
    for freq in freqs:
        sum_count2 += freq[0]
        sum_count3 += freq[1]
    response = sum_count2 * sum_count3
    return response