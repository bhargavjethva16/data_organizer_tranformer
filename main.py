print("\n ========= Welcome To The Data Analyzer And Transformer Program ============ ")

data = []

def input_Data():
    """Displays 1D and 2D array """
    global data 
    print()
    print("select option :")
    print("1. 1D Array ")
    print("2. 2D Array ")
    
    num = int(input("Enter No. from the given option:- "))

    if num == 1:
        num = input("Enter The Number (Separated By Spaces) : ").split()
        data = list(map(int,num))
        print ("Input data has been stored successfully.")

    elif num == 2:
        print()
        row = int(input("Enter the No. of rows:- "))
        columns = int(input("Enter the No. of columns:- "))
        
        data = []
        for n in range(row):
            n=[]
            for c in range(columns):
                num = int(input("Enter Number: "))
                n.append(num)
            data.extend(n)
            
        print("2D Array data has been stored successfully. ")
        print()
def converter(data):
    if len(data)>0 and isinstance( data[0],list):
        l = []
        for x in data:
            l.extend(x)
        return l
    else:
        return data 

    
def summary(data):
    
    """Displays the summary data of 1D and 2D """
    new_data = converter(data)
    print("\nData Summary:")
    print(f"- Total Element :- {len(new_data)}")
    print(f"- Minimum Value :- {min(new_data)}")
    print(f"- Maximum Value :- {max(new_data)}")
    print(f"- Sum Of All Element :- {sum(new_data)}")
    print(f"- Average Value :- {sum(new_data) / len(new_data)}")
    print()


def fact(n):
    """Calculates the Factorial (Recursion)."""
    print()
    if n<=0:
        return 1
    return n*fact(n-1)
    
 
def factorial():
    """Calculates the factorial of a number using Recursion."""
    print()
    num = int(input("Enter a No. to calculate its Factorial:-  "))
    print(f"Factorial of {num} is {fact(num)}")
    print()
    return num
    

def threshold(data):
    """Filters data based on Threshold value"""
    print()   
    new_data = converter(data)
    data_input = int(input("Enter No. to filter out the Threshold value:-  "))
    print(f"Filtered Data (Values >= {data_input})")
    data_input = list(filter(lambda x : x > data_input , new_data ))
    print(*data_input,sep=", ")
    print()

def sort(data):
    """Sorts data in ascending and descending order accordingly."""
    print()
    print("Select an option: ")
    print("1. Ascending Order")
    print("2. Descending Order")
    
    choose = int(input("Enter Number from the given option:-  "))
    
    if choose == 1:
        accending= sorted(data)
        print(accending)
    elif choose == 2 :
        descending = sorted(data, reverse=True)
        print(descending)        

def data_statistics(*values):
    """Displays the statistics data from the given data."""
    print()
    values = converter(values)
    Minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total/len(values)
    return Minimum,maximum,total,average

def statistics():
    """Display statistics of the data."""
    if len(data) == 0:
        print("No Data has been taken")
        print()
        return 
    
    Minimum,maximum,total,average = data_statistics(data)
    print(f"-Minimun Value: {Minimum}")
    print(f"- Maximun Value: {maximum}")
    print(f"- Sum Of All Value: {total}")
    print(f"- Average  Value: {average}")
    print()


while True:
    print("\nMain Menu: ")
    print()
    print("1. Input Data ")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Value) ")
    print("7. Exit ")
    print()
    
    print()
    choice = int(input("Enter your choice:- "))
    print()
    
    if choice == 1 :
        input_Data()
    elif choice == 2 :
        summary(data)
    elif choice == 3 :
        factorial()
    elif choice == 4:
        threshold(data)
    elif choice == 5 :
        sort(data)
    elif choice == 6:
        new_data = converter(data)
        Minimum,maximum,total,average = data_statistics(data)
        print(f"-Minimun Value: {Minimum}")
        print(f"- Maximun Value: {maximum}")
        print(f"- Sum Of All Value: {total}")
        print(f"- Average  Value: {average}")
        print()

    elif choice == 7 :
        print("Exiting program...")
        break

    else:
        print("Enter a valid choice from the given choice. ")