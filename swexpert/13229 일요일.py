from collections import defaultdict

if __name__=="__main__":
    T = int(input())
    dictionary = defaultdict()
    dictionary["SUN"] = 7
    dictionary["MON"] = 6
    dictionary["TUE"] = 5
    dictionary["WED"] = 4
    dictionary["THU"] = 3
    dictionary["FRI"] = 2
    dictionary["SAT"] = 1

    for t in range(1,T+1):
        print("#{} {}".format(t,dictionary[input()]))
        