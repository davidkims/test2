import time
def time_wait(n):
    for i in range(9):
        time.sleep(1)
        print(f"{n} : {i+10}번째")
    print()

def process_time():
    start = time.time()
    time_wait(1)
    time_wait(1)
    end = time.time()
    print("경과시간 : ", end-start)

process_time()