class Queue:
    def __init__(self, queue_list):
        self.queue = queue_list

    def show_queue(self):
        print(self.queue)

    def queue_length_check(self):
        return f"Queue is ---> {len(self.queue)} long" if len(self.queue) > 0 else "Queue is empty"

    def queue_put(self, customer):
        return self.queue.append(customer)

    def queue_get(self):
        return self.queue.pop[0]


def main():
    l1 = Queue(["a", "b", "c", "d"])
    l1.show_queue(l1)
