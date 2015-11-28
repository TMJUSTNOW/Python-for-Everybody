import re
def main():

    myfile = open("regex_sum_200866.txt",'r')    
       
    print sum([int(x) for x in (re.findall(r'[0-9]+',myfile.read()))])


if __name__ == '__main__':
    main()
