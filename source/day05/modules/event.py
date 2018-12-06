class Event:

    def trigger_units_of(self, polymer: [str]):

        stack = ['#']  # a pillow

        for c in polymer:
            tail = stack[-1]
            if tail == c.swapcase():  # if different and opposite
                stack.pop()  # react
            else:  # if similar
                stack.append(c)

        stack = stack[1:]  # remove pillow, at head

        result = ''.join(stack)  # convert list to string

        return result
