from collections import Counter

class Reporter:

    def get_freqs(entries):
        """
        Given an array of entries
        returns the frequencies, as a Counter
        """

        awake = True
        prev_time = -1
        curr_time = -1
        asleep_mins = []

        for entry in entries:
            if prev_time == -1:
                prev_time = int(entry['time'][3:])
            else:
                curr_time = int(entry['time'][3:])
                if not(awake):
                    for i in range(prev_time, curr_time):
                        asleep_mins.append(i)
                prev_time = curr_time
            awake = not(awake)

        freqs = Counter(asleep_mins)

        return freqs
