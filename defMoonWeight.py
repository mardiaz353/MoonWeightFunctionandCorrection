#moon Weight function designed to grab three user inputs
def moonWeight(myWeight, increase, years):
    #my starting weight will be 30 kilos
    print("Please enter your weight")
    myWeight = int(input())
    print("Please enter how much you want to increase your weight by every year")
    increase = int(input())
    print("How many years would you like this to happen for?")
    years = int(input())
    for i in range(1, years):
        
        #I'm going to add 1 kilo every year
        myWeight = myWeight + increase
        #Now I need to convert that to moon weight every time
        #because it's in kilos not moon weight as it stands
        moonWeight = myWeight * 0.165
        #now I need to output this
        print("Year %s Weight: %s" % (years, moonWeight))


#2 Moon weight function and more years
