from collections import Counter


class Reporter:

    def get_freqs_by_date(self, entries):
        """
        Given an array of entries
        returns the frequencies, as a Counter
        """

        prev_date = ''
        curr_date = ''

        entries_by_date = {}

        curr_date_entries = []

        for entry in entries:

            curr_date = entry['date']

            if prev_date == '':
                curr_date_entries.append(entry)
            else:
                if curr_date != prev_date:
                    entries_by_date[prev_date] = self.get_m_freqs(curr_date_entries)
                    curr_date_entries = []
                curr_date_entries.append(entry)

            prev_date = curr_date

        entries_by_date[prev_date] = self.get_m_freqs(curr_date_entries)

        return entries_by_date

    def get_m_freqs(self, entries):
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
