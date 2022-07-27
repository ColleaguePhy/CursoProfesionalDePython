from datetime import datetime

def exectuin_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        print(f'pasaron:  {final_time - initial_time}') 
    
    return wrapper

@exectuin_time
def random_func():
    for _ in range(1,100000):
        pass

def main(): 
    random_func()

if __name__ == '__main__':
    main()