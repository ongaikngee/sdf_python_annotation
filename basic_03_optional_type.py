from typing import Optional

def greet(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"
    
def main():
    
    my_result = greet('Jack')
    print(my_result)
    
    my_result = greet(None)
    print(my_result)
    
main()