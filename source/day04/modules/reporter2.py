from collections import defaultdict

class Reporter2:

    def produce_data2(self, filename):

        filepath = f'data/{filename}-sorted.csv'

        time_by_guards = defaultdict()
        guard = None
        asleep = None

        with open(filepath) as in_file:
            line = in_file.readline()
            while line:
                line = line.replace('\n', '')
                if line == '':
                    break
                date, time, occurrence = line.split(',')
                time = int(time)
                if '#' in occurrence:
                    guard = int(occurrence[1:])
                    asleep = None
                elif occurrence == 'FA':
                    asleep = time
                elif occurrence == 'WU':
                    if asleep == None:
                        line = in_file.readline()
                        continue
                    for t in range(asleep, time):
                        if (guard, t) in time_by_guards:
                            time_by_guards[(guard, t)] += 1
                        else:
                            time_by_guards[(guard, t)] = 1

                line = in_file.readline()

        return time_by_guards

    def __get_G_most_asleep(self, C):
        most = None
        for k,v in C.items():
            if most is None or v > C[most]:
                most = k
        return most, C[most]


    def report(self, C):
        worst_guard, minutes = self.__get_G_most_asleep(C)
        print(f'Worst guard: {worst_guard}')
        print(f'Minutes asleep: {minutes}')
        return worst_guard


    def produce_data(self, filename):

        filepath = f'data/{filename}-sorted.csv'

        C = defaultdict(int)
        time_by_guards = defaultdict()
        guard = None
        asleep = None

        with open(filepath) as in_file:
            line = in_file.readline()
            while line:
                line = line.replace('\n', '')
                if line == '':
                    break
                date, time, occurrence = line.split(',')
                time = int(time)
                if '#' in occurrence:
                    guard = occurrence[1:]
                    asleep = None
                elif occurrence == 'FA':
                    asleep = time
                elif occurrence == 'WU':
                    if asleep == None:
                        line = in_file.readline()
                        continue
                    for t in range(asleep, time):
                        if guard in time_by_guards:
                            time_by_guards[guard].append(t)
                        else:
                            time_by_guards[guard] = []
                            time_by_guards[guard].append(t)
                        C[guard] += 1

                line = in_file.readline()

        return C, time_by_guards
