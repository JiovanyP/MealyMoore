class MooreMachine:
    def __init__(self):
        self.transitions = {
            'A': {'0': 'A', '1': 'B'},
            'B': {'0': 'C', '1': 'D'},
            'C': {'0': 'D', '1': 'B'},
            'D': {'0': 'B', '1': 'C'},
            'E': {'0': 'D', '1': 'E'}
        }

        self.outputs = {
            'A': 'A',
            'B': 'B',
            'C': 'C',
            'D': 'C',
            'E': 'C'
        }

        self.current_state = 'A'

    def reset(self):
        """Ibalik sa initial state."""
        self.current_state = 'A'

    def process_input(self, input_string):
        """Proseso ng buong input string at ibalik ang output sequence."""
        output_sequence = self.outputs[self.current_state]
        print(
            f"Initial state: {self.current_state} (Output: {output_sequence})")

        for i, symbol in enumerate(input_string):
            if symbol not in ['0', '1']:
                raise ValueError("Input should only contain 0 or 1.")

            next_state = self.transitions[self.current_state][symbol]
            self.current_state = next_state
            output = self.outputs[self.current_state]

            print(
                f"Step {i+1}: Input={symbol}, Next State={next_state}, Output={output}")
            output_sequence += output

        return output_sequence


if __name__ == "__main__":
    moore = MooreMachine()

    test_inputs = ["00110", "11001", "1010110", "1011111"]

    for test in test_inputs:
        print(f"\nProcessing input: {test}")
        output = moore.process_input(test)
        print(f"Output sequence: {output}")
        moore.reset()
