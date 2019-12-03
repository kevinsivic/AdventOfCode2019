class Computer:

    @staticmethod
    def compute(memory):
        instruction_pointer = 0
        while 1:
            opcode = int(memory[instruction_pointer])
            num_values = -1
            if opcode == 99:
                break

            if opcode == 1:
                parm1 = instruction_pointer + 1
                parm2 = instruction_pointer + 2
                parm3 = instruction_pointer + 3

                addend1 = int(memory[int(memory[parm1])])
                addend2 = int(memory[int(memory[parm2])])

                memory[int(memory[parm3])] = addend1 + addend2
                num_values = 4

            elif opcode == 2:
                parm1 = instruction_pointer + 1
                parm2 = instruction_pointer + 2
                parm3 = instruction_pointer + 3

                factor1 = int(memory[int(memory[parm1])])
                factor2 = int(memory[int(memory[parm2])])

                memory[int(memory[parm3])] = factor1 * factor2
                num_values = 4

            instruction_pointer += num_values

        return memory;

    @staticmethod
    def get_program():
        f = open("input", "r")
        app = f.read()
        return list(map(int, app.split(",")))

    def main(self):
        for verb in range(0, 99):
            for noun in range(0, 99):

                initial_state = self.get_program()
                initial_state[1] = noun
                initial_state[2] = verb
                output = self.compute(initial_state[:])
                if output[0] == 19690720:
                    print(noun)
                    print(verb)
                    print(100 * noun + verb)
                    break


comp = Computer()

comp.main()
