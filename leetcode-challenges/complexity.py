import time
import functools
import numpy as np # type: ignore

def BigO(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Measure time for different input sizes
        input_sizes = [10, 100, 1000, 10000]
        times = []
        
        for size in input_sizes:
            test_args = ([i for i in range(size)], *args[1:])
            start_time = time.time()
            func(*test_args, **kwargs)
            end_time = time.time()
            times.append(end_time - start_time)
        
        # Estimate complexity
        log_sizes = np.log(input_sizes)
        log_times = np.log(times)
        slope, _ = np.polyfit(log_sizes, log_times, 1)
        
        if slope < 1.5:
            complexity = "O(n)"
        else:
            complexity = "O(n^2)"
        
        print(f"Estimated complexity of {func.__name__}: {complexity}")
        
        # Run the actual function
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.6f} seconds")
        
        return result

    return wrapper