import psutil
import time
import sys
import getopt

def notice(unit):
    print("Input PID to get memory usage.")
    print("Unit:",unit)
    print("Use Ctrl+C or make process be exited to break.",end="\n\n")

def basic_info(pid):
    try:
        process = psutil.Process(pid)
    except:
        print("\033[31mProcess Exited!\033[0m")
        sys.exit()
    print('|'+' '*19+"Process NAME:",process.name())
    print('|'+' '*19+"Process status:",process.status())
    print('|'+' '*19+"Process file:",process.exe())
    print('|'+' '*19+"Process CPU usage percent:",process.cpu_percent())
    print("")

def memory_get(pid,he):
    try:
        process = psutil.Process(pid)
    except:
        print("\033[31mProcess Exited!\033[0m")
        sys.exit()
    last = process.memory_info().rss
    last = int(last/he)
    info = time.strftime("[%y-%m-%d %H:%M:%S] ", time.localtime())+"(INIT) Momory usage is " + str(last)
    print(info)
    basic_info(pid)

    while True:
        info = ""
        try:
            now = process.memory_info().rss
        except(psutil.NoSuchProcess):
            print("\033[31mProcess Exited!\033[0m")
            sys.exit()
        now = int(now/he)
        if now != last:
            now_t = time.strftime("[%y-%m-%d %H:%M:%S] ", time.localtime())
            info = now_t + "Compare last time momory usage "
            der = now - last
            if der >= 0:
                info = info + '+'
            info = info + str(der) + '.  ' + "Total usage is " + str(now) + '.'
            print(info)
            last = now
            time.sleep(0.75)

def into(argv):
    input_pid = ''
    hexa = 1
    hexa_name = "Byte"
    try:
        opts, args = getopt.getopt(argv,"hp:mk",["pid="])
    except getopt.GetoptError:
        print('-p <PID> [-k|-m <Unit>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-p <PID> [-k|-m <Unit>]')
            sys.exit()
        elif opt in ("-p", "--pid"):
            input_pid = arg
        else:
            if opt in "-m":
                hexa = 1024*1024
                hexa_name = "MB"
            elif opt in "-k":
                hexa = 1024
                hexa_name = "KB"
    notice(hexa_name)
    memory_get(int(input_pid),hexa)

if __name__ == "__main__":
   into(sys.argv[1:])
