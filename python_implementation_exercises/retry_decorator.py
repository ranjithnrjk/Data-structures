from functools import wraps

attempt = 0

def retry_dec(max_retry=3):

    def decorator(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts <= max_retry:
                try:
                    return func(*args, **kwargs)

                except Exception:
                    
                    attempts += 1

                    if attempts > max_retry:
                        
                        raise 
                    
                    print(f"Retrying.....Attempt:{attempts}")
        
        return wrapper
    
    return decorator


@retry_dec(max_retry=3)
def main_func(n):

    global attempt
    attempt += 1

    if attempt < 3:
        raise Exception("Temporary error")
    
    print("Succeeded")

    return "Success"


if __name__ == '__main__':
    output = main_func(3)
    print(output)
    