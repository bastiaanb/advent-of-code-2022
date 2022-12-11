#!/usr/bin/env python

from collections import OrderedDict
from dataclasses import dataclass, field
import fileinput
import re
import numpy as np

@dataclass
class Monkey:
    all_monkeys: dict
    items: list = field(default_factory=list)
    operation: str = None
    test: int = 0
    if_: dict = field(default_factory=dict)
    inspections = 0

    def do_turn(self, product, worry_divisor):
        for item in self.items:
            self.inspections += 1
            new_worry = int(eval(self.operation, {"old": item}) / worry_divisor) % product
            self.all_monkeys[self.if_[new_worry % self.test == 0]].items.append(new_worry)

        self.items = []

def read_inputs(inputs):
    monkeys = OrderedDict()

    for input in inputs:
        match input.replace(":", "").replace(",", "").split():
            case []:
                pass
            case ["Monkey", id]:
                monkey = Monkey(monkeys)
                monkeys[id] = monkey
            case ["Starting", "items", *items]:
                monkey.items = [ int(i) for i in items ]
            case ["Operation", "new", "=", *ops]:
                monkey.operation = " ".join(ops)
            case ["Test", "divisible", "by", divisor]:
                monkey.test = int(divisor)
            case ["If", true_false, "throw", "to", "monkey", throw_to]:
                monkey.if_[true_false == "true"] = throw_to
            case _:
                print(f"unknown input '{input}'")
                break

    return monkeys

def calculate_monkey_business(monkeys, rounds, worry_divisor):
    product = np.prod([ monkey.test for monkey in monkeys.values() ])

    for round in range(rounds):
        for id, monkey in monkeys.items():
            monkey.do_turn(product, worry_divisor)

    inspections = [ monkey.inspections for monkey in monkeys.values() ]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

inputs = [ line.strip() for line in fileinput.input() ]

monkeys = read_inputs(inputs)
print(monkeys)
print(f"star 21: {calculate_monkey_business(monkeys, 20, 3)}")

monkeys = read_inputs(inputs)
print(f"star 22: {calculate_monkey_business(monkeys, 10000, 1)}")
