class MooreMachine:
    def __init__(self):
        # Initial state
        self.state = 'A'
        # State outputs
        self.outputs = {
            'A': '0',
            'B': '0',
            'C': '1'
        }

    def transition(self, input_symbol):
        """Handles state transitions based on input symbol."""
        if self.state == 'A':
            if input_symbol == '1':
                self.state = 'B'
            else:  # input_symbol == '0'
                self.state = 'C'

        elif self.state == 'B':
            if input_symbol == '1':
                self.state = 'B'
            else:
                self.state = 'C'

        elif self.state == 'C':
            if input_symbol == '1':
                self.state = 'B'
            else:
                self.state = 'C'

    def process(self, input_string):
        """Process input string and return output string."""
        output = ''
        for symbol in input_string:
            self.transition(symbol)
            output += self.outputs[self.state]
        return output


# Example usage
if __name__ == "__main__":
    machine = MooreMachine()
    input_string = "0110"
    print(f"Input:  {input_string}")
    print(f"Output: {machine.process(input_string)}")
