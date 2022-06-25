class Stack:
    def __init__(self, stack):
        self.stack = stack

    def show_stack(self):
        print(self.stack.reverse())

    def queue_length_check(self):
        return f"Stack is ---> {len(self.stack)} long" if len(self.stack) > 0 else "Queue is empty"

    def queue_put(self, customer):
        return self.stack.append(customer)

    def queue_get(self):
        return self.stack.pop()


def main():
    l1 = Stack(["a", "b", "c", "d"])
    l1.show_stack()

main()
