<h1>Decorators without arguments</h1>
FLow:

```
function → decorator(func) → wrapper → execute wrapper
```

```
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # before logic
        result = func(*args, **kwargs)
        # after logic
        return result

    return wrapper    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
Usage:

```
@decorator
def my_function():
    pass
```
- Pythod Internally does 
```my_function = decorator(my_function)```

<h1>Decorators with arguments</h1>
Flow

```
decorator(args) 
    ↓
decorator(func)
    ↓
wrapper
```


```
from functool import wraps

def decorator_with_args(param):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Before Logic using param
            result = func(*args, **kwargs)
            # After Logic
            return  result
        
        return wrapper
    
    return decorator
```

Usage:

```@decorator_with_args(3)
def my_function():
    pass
```

- Python internally does: ```my_function = decorator_with_args(3)(my_function)```