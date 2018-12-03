def process(freqs):
    """
    Given an array of freqs
    get the checksum
    """
    sum_count2 = 0
    sum_count3 = 0
    for freq in freqs:
        if freq[0] == True:
            sum_count2 += 1
        if freq[1] == True:
            sum_count3 += 1
    response = sum_count2 * sum_count3
    return response
