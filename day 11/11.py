from pprint import pprint as print

class Monkey:
    def __init__(self, description: str):
        """Sample---
            Starting items: 91, 66
            Operation: new = old * 13
            Test: divisible by 19
                If true: throw to monkey 6
                If false: throw to monkey 2
            """
        starting, operation, test, true, false, _ = description.split('\n')
        # starting
        self.starting_items = list(map(int, starting.strip(',').split()[2:]))
        # operation
        operation = operation.split()
        n = int(operation[-1])
        if operation[-2] == '*':
            self.operation = lambda x: x*n
        elif operation[-2] == '+':
            self.operation = lambda x: x + n
        # tests
        self.test = lambda x: x % int(test.split()[-1]) == 0
        # true
        self.true_to = int(true.split()[-1])
        # false
        self.false_to = int(false.split()[-1])
        # done

with open("11", 'r') as file:
    monkeys = file.read().split('\n\n')

MM = []
for m in monkeys:
    MM.append(Monkey(m))

print(MM)
        
