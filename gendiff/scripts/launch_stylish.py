#!/usr/bin/env python3
from gendiff.diff_generators import stylish


def main():
    stylish.stylish('__tests__/fixtures/before.json', '__tests__/fixtures/after.json')
