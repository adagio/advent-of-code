class Preparer:


    def sort_file(self, in_filepath, out_filepath):
        lines = open(in_filepath).read().split('\n')
        lines.sort()

        with open(out_filepath, 'w') as sorted_file:
            for line in lines:
                sorted_file.write(f'{line}\n')


    def prepare_file(self, in_filepath, out_filepath):
        with open(in_filepath) as in_file:
            with open(out_filepath, 'w') as out_file:
                line = in_file.readline()
                while line:
                    # print(line)
                    line = line.strip()
                    line = line.replace('Guard ', '')
                    line = line.replace('begins shift', '')
                    line = line.replace('wakes up', 'WU')
                    line = line.replace('falls asleep', 'FA')
                    words = line.split()
                    # print(words)

                    date, time = words[0][1:], words[1][:-1]
                    occurrence = words[2]
                    parsed_time = time.split(':')[1]
                    parsed_line = f'{date},{parsed_time},{occurrence}\n'
                    # print(parsed_line)

                    out_file.write(parsed_line)
                    line = in_file.readline()
