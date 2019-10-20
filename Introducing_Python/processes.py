import os, subprocess, multiprocessing as mp


def whoami(what):
    print(f"PID: {os.getpid()}, says {what}")

def washer(dishes, output):
    for dish in dishes:
        print(f"Washing {dish} dish")
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print(f"Drying {dish} dish")
        input.task_done()

if __name__ == "__main__":  #this is needed to identify the main process
    #Get process Id and current directory
    print(f"PID: {os.getpid()}.  Current directory: {os.getcwd()}")

    # #Get a tuple with the return code and the output
    output = subprocess.getstatusoutput("dir")
    print(f"Return code: {output[0]} ")
    print(f"Output: {output[1]}")

    #Starts 5 processes
    for i in range(5):
        p = mp.Process(target=whoami, args=(f"Iteration : {i}",))
        p.start()

    #multiprocessing using queues
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad','bread','entree','dessert']
    washer(dishes, dish_queue)
    dish_queue.join()