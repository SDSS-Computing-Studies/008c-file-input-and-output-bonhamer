
def find(stock):
    filename = "task02.csv"
    file = open(filename, "r")
    count = 0
    list1 = []
    for i in file:
        if stock in i:
            count = count + 1
            test = i.strip()
            linedata = test.split(",")
            
            list1.append(linedata[1])
    if len(list1) > 1:
        print(f"There are {len(list1)} stocks with that symbol")
    elif len(list1) == 1:
        print(list1)
    elif len(list1) == 0:
        print("No matches")

x = input("Enter stock symbol: ")
find(x)


    

