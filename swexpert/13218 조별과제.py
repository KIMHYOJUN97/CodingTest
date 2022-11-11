if __name__=="__main__":
    T = int(input())

    for t in range(1,T+1):
        n = int(input())
        print("#{} {}".format(t,n//3))