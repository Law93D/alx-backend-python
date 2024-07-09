# 0x02. Python - Async Comprehension

## Description
This project covers asynchronous comprehensions and generators in Python. You will learn how to write asynchronous generators, use async comprehensions, and type-annotate generators.

## Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Tasks

### Task 0: Async Generator
Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

### Task 1: Async Comprehensions
Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

### Task 2: Run time for four parallel comprehensions
Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

## Requirements
- Python 3.7
- All files should be PEP8 compliant
- Type annotations should be used in all functions and coroutines
- Each module and function must have a proper docstring
