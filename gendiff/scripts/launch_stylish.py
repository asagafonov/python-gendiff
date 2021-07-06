#!/usr/bin/env python3
from gendiff.diff_generators import stylish


def main():
    stylish.stylish('__fixtures__/before.json', '__fixtures__/after.json')
