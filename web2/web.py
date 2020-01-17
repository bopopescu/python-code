import time


def progress_bar(num):
    j = "#";
    k = "=";
    t = "|/-\\";  # s = " " * (num + 1)

    for i in range(0, num + 1):
        j += "#";
        k += "=";
        s = ("=" * i) + (" " * (num - i))

        # print(int(i/num*100), end='%\r')
        # print('%.2f' % (i/num*100), end='%\r')
        # print('%.2f' % (i*100/num), end='%\r')
        # print('complete percent:', time.strftime("%Y-%m-%d %H:%M:%S", \
        #        time.localtime()), int((i/num)*100), end='%\r')
        # print(str(int(i/num*100)) + '% ' + j + '->', end='\r')
        # print(k + ">" + str(int(i/num*100)), end='%\r')
        # print("[%s]" % t[i%4], end='\r')
        # print("[%s][%s][%.2f" % (t[i%4], k, (i/num*100)), "%]", end='\r')
        print("[%s][%s][%.2f" % (t[i % 4], s, (i / num * 100)), "%]", end='\r')

        time.sleep(0.2)

    print()


progress_bar(300)
