import psutil

print("Hello World")



def mem():
    print("MEMORY\n\nvirtual memory\n--------------\n---------  ----------")
    number = 0
    words = ("total","available","percent","used","free","active","inactive","buffers","cached","shared","slab")
    while number < len(psutil.virtual_memory()):
        print(words[number] + ":    " + str(psutil.virtual_memory()[number]))
        number = number +1
    print("---------  ----------\n\nswap\n----\n-------  ----------")
    number = 0
    words = ("total","used","free","percent","sin","sout")
    while number < len(psutil.swap_memory()):
        print(words[number] + ":   " + str(psutil.swap_memory()[number]))
        number = number+1
    print("-------  ----------")



def cpu():
    print("CPU\n---\n\ncores\n------\n-")
    print(psutil.cpu_count())
    print("-\n\nload average\n------------\n  1    5    15\n----  ----  ----")
    line = ""
    for a in psutil.getloadavg():
        line = line+str(a)+"  "
    print(line)
    number = 0

    print("times\n-----\n      user    nice      system    idle    iowait    irq    softirq    steal    guest    guest_nice\n--  ------  ------    --------  ------  --------  -----  ---------  -------  -------  ------------")

    for a in psutil.cpu_times(percpu=True):
        line = ""
        for b in a:

            line = line + str(b) + "     "
        print(str(number) + "   " + line)
        number = number + 1
    print("\nutilization\n-----------")
    number = 0
    Count = "  0"
    Line = "----  "
    while number+1 < psutil.cpu_count(logical=True):
        number = number + 1
        Count = Count + "     " + str(number)
        Line = Line + "----  "

    print(Count+"\n"+Line)
    b = " "
    for a in psutil.cpu_percent(percpu=True):
        b=b+str(a)+"   "
    print(b)
cpu()
mem()
