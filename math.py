
import math

limit = (math.pi * 2)
inc = limit / 16

def main():
    count = 0.0
    c = 0.0
    while count <= limit+inc:
        v=(339 * math.sin(count))
        print count,v

        c=c+(abs(v) * abs(v))
        print c
        count = count + inc

    print "=========================="
    print math.sqrt(c / 16)
main()
