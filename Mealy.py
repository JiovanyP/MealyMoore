class MealyMachine:
    def __init__(self):
        # Define states
        self.state = 'A'
    
    def transition(self, input_symbol):
        """
        Transition logic for the Mealy Machine that outputs:
        - 'a' when sequence '01' is encountered
        - 'b' otherwise
        """
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'A'
                return 'b'

        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'C'
                return 'a'

        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'A'
                return 'b'

    def process(self, input_string):
        """Process the full input binary string and return the output string."""
        output = ''
        for symbol in input_string:
            output += self.transition(symbol)
        return output


# Example usage
if __name__ == "__main__":
    machine = MealyMachine()
    
    input1 = "0110"
    input2 = "1000"

    print(f"Input: {input1} → Output: {machine.process(input1)}")
    
    # Reset machine for next input
    machine = MealyMachine()
    print(f"Input: {input2} → Output: {machine.process(input2)}")
