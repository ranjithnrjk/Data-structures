import time
from functools import wraps


def log_runtime(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()

        print(f"{func.__name__} took {end-start:.2f} seconds.")

        return result
    
    return wrapper

@log_runtime
def train_model(n):
    '''Simulates model training'''
    for i in range(n):
        time.sleep(0.01)
    
    return 'Training ..... Completed.'

if __name__ == "__main__":
    output = train_model(10)
    print(output)
    print(train_model.__name__)
    print(train_model.__doc__)