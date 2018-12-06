class Event:

    def trigger_units_of(self, polymer: [str]):

        stack = []

        for c in polymer:
            if stack and stack[-1] == c.swapcase():  # if stack and opposite
                stack.pop()  # react
            else:  # if similar
                stack.append(c)

        result = str().join(stack)  # convert list to string

        return result
