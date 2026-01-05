from typing import List

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)


def main():
    my_result = process_numbers([1,2,3,4])
    print(my_result)
    
main()