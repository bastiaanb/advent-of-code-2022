#!/usr/bin/env python

from collections import OrderedDict
from dataclasses import dataclass
import fileinput
import re
import numpy as np

@dataclass
class Monkey:
    items: list
    operation: str
    test: int
    if_: dict
    all_monkeys: dict
    inspections = 0

    def do_turn(self, product, worry_divisor):
        for item in self.items:
            self.inspections += 1
            new_worry = int(eval(self.operation, {"old": item}) / worry_divisor) % product
            self.all_monkeys[self.if_[new_worry % self.test == 0]].items.append(new_worry)

        self.items = []

def read_inputs(inputs):
    monkeys = OrderedDict()

    monkey_id = None
    items = []
    operation = ""
    test = ""
    if_ = {}

    for input in inputs:
        if input == "":
            continue
        m = re.match("Monkey ([0-9]+):", input)
        if m:
            if monkey_id:
                monkeys[monkey_id] = Monkey(items, operation, test, if_, monkeys)
            monkey_id = m.group(1)
            if_ = {}
        else:
            m = re.match("  Starting items: (.+)", input)
            if m:
                items = [ int(i) for i in m.group(1).split(", ") ]
            else:
                m = re.match("  Operation: new = (.+)", input)
                if m:
                    operation = m.group(1)
                else:
                    m = re.match("  Test: divisible by ([0-9]+)", input)
                    if m:
                        test = int(m.group(1))
                    else:
                        m = re.match("    If (true|false): throw to monkey ([0-9]+)", input)
                        if m:
                            if_[m.group(1) == "true"] = m.group(2)
                        else:
                            print(f"unknown input '{input}'")
                            break

        if monkey_id:
            monkeys[monkey_id] = Monkey(items, operation, test, if_, monkeys)

    return monkeys

def calculate_monkey_business(monkeys, rounds, worry_divisor):
    product = np.prod([ monkey.test for monkey in monkeys.values() ])

    for round in range(rounds):
        for id, monkey in monkeys.items():
            monkey.do_turn(product, worry_divisor)

    inspections = [ monkey.inspections for monkey in monkeys.values() ]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

inputs = [ line.rstrip() for line in fileinput.input() ]

monkeys = read_inputs(inputs)
print(f"star 21: {calculate_monkey_business(monkeys, 20, 3)}")

monkeys = read_inputs(inputs)
print(f"star 22: {calculate_monkey_business(monkeys, 10000, 1)}")
