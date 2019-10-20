#shows how to user threads
import threading, queue, time

def do_this(what):
    # whoami(what)
    print(f"Thread {threading.current_thread()} says: {what}")

# def whoami(what):
#     print(f"Thread {threading.current_thread()} says: {what}")

def washer(dishes, dish_queue):
    for dish in dishes:
        print(f"Washing {dish} dish")
        time.sleep(5)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print(f"Drying {dish} dish")
        time.sleep(10)
        dish_queue.task_done()

if __name__ == "__main__":
    # whoami("I am the main program")
    do_this("I am the main program")
    for n in range(5):
        p = threading.Thread(target=do_this, args=(f"I am function {n}",))
        p.start()

    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    dish_queue = queue.Queue()
    for i in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['salad','bread','entree','dessert']
    washer(dishes, dish_queue)
    dish_queue.join()