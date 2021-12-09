class Stack:

    def __init__(self):
        self.items=[]

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def peek(self):
        return self.items[-1] # Use peek to look at the top of the stack


# class Simplestack():
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self, v):
#         self.stack.append(int(v))
#
#     def pop(self):
#         return self.stack.pop()
#
#     def inc(self, n, inc_by):
#         n, inc_by = int(n), int(inc_by)
#         for pos in range(n):
#             self.stack[pos] += inc_by
#
#     def run(self, operations: list):
#         funcs = {
#             'push': self.push,
#             'pop' : self.pop,
#             'inc' : self.inc
#         }
#
#         for operation in operations:
#             op, *args = operation.split(' ')
#             funcs[op](*args)
#
#             print(self.stack[-1] if self.stack else "EMPTY")
#
# super_stuck = Simplestack()
# super_stuck.run(['push 4', 'push 5', 'inc 2 1', 'pop', 'pop'])