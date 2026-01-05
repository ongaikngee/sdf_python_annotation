from typing import Union

def double_or_square(number: Union[int, float]) -> Union[int, float]:
    if isinstance(number, int):
        return number * 2
    else:
        return number ** 2
    
    
def main():
    my_result = double_or_square(4)
    print(my_result)
    
main()