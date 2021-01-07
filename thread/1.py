from concurrent.futures import ThreadPoolExecutor

def func():
    pass

executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix="test")
executor.submit()