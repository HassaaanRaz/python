def main():
    print(cal_fact(7))





def cal_fact(n):
    #8 = 8*7*6*5*4*3*2*1
    factorial = 1
    
    for i in range(n):
        factorial = (i+1)* factorial
        

    return factorial



main()