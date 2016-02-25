# Task 4 - People say this is tricky, though it seems not at all

stack_size = int(input())
callstack = input().split()
dummy_number = int(input())
exception_handling = {}
for _ in range(dummy_number):
    fun, inex, outex = input().split()
    if fun in exception_handling:
        exception_handling[fun][inex] = outex
    else:
        exception_handling[fun] = {inex: outex}
this_exception = input()

output_stack = callstack.copy()
for i in range(1, stack_size + 1):
    can = this_exception in exception_handling[callstack[-i]]
    if can:
        if exception_handling[callstack[-i]][this_exception] == '_':
            break
        else:
            this_exception = exception_handling[callstack[-i]][this_exception]
            output_stack = output_stack[:-1]
    else:
        output_stack = output_stack[:-1]
        continue

print(' '.join(output_stack))
