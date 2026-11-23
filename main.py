import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("\n======================================")
print("       RETAIL SALES DATA ANALYZER")
print("======================================")

class RetailAnalyzer:

    def __init__(self):
        self.data = None

   
    def load_data(self):
        

        file = input("Enter CSV File Name (retail_sales.csv) :- ")

        self.data = pd.read_csv(file)

        print("Data Loaded Successfully!")


    def menu(self):

        while True:

            print("\n======================================")
            print("       RETAIL SALES DATA ANALYZER")
            print("======================================")

            print("1. Explore Data")
            print("2. Clear Data")
            print("3. Perform Data Analysis")
            print("4. Visualization Data")
            print("5. Data Analysis Report")
            print("6. Exit")

            choice = int(input("Enter Choice Between (1-6) :- "))


          

            if choice == 1:

                print("\n===== Explore Data =====")

                print("1. Top 5 Data")
                print("2. Last 5 Data")
                print("3. Information Of Data")
                print("4. Datatype")

                ch = int(input("Enter Choice (1-4) :- "))

                if ch == 1:
                    print(self.data.head())

                elif ch == 2:
                    print(self.data.tail())

                elif ch == 3:
                    self.data.info()

                elif ch == 4:
                    print(self.data.dtypes)

                else:
                    print("Invalid Choice!")


            elif choice == 2:

                print("\n===== Clear Data =====")

                print("1. Check Missing Data")
                print("2. Handle Missing Data")
                print("3. Show Duplicate Data")

                ch = int(input("Enter Choice (1-3) :- "))

                if ch == 1:

                    print(self.data.isnull().sum())

                elif ch == 2:

                    print("1. Delete Missing Data")
                    print("2. Fill Missing Data")

                    c = int(input("Enter Choice (1-2) :- "))

                    if c == 1:

                        self.data = self.data.dropna()

                        print("Missing Data Deleted!")
                        print(self.data)

                    elif c == 2:

                        self.data = self.data.fillna(0)

                        print("Missing Data Filled!")
                        print(self.data)

                    else:
                        print("Invalid Choice!")

                elif ch == 3:

                    print(self.data[self.data.duplicated()])

                else:
                    print("Invalid Choice!")


        

            elif choice == 3:

                print("\n===== Data Analysis =====")

                print("1. Total Sales")
                print("2. Average Sales")
                print("3. Maximum Sales")
                print("4. Minimum Sales")
                print("5. Total Quantity Sold")
                print("6. Most Popular Product")

                ch = int(input("Enter Choice (1-6) :- "))
                
                try:
                    if ch == 1:

                        print(self.data["total sales"].sum())

                    elif ch == 2:

                        print(self.data["total sales"].mean())

                    elif ch == 3:

                        print(self.data["total sales"].max())

                    elif ch == 4:

                        print(self.data["total sales"].min())

                    elif ch == 5:

                        print(self.data["quantity sold"].sum())

                    elif ch == 6:

                        product = self.data.groupby("Product")["quantity sold"].sum()

                        print("Most Popular Product:", product.idxmax())

                    else:
                        print("Invalid Choice!")
                except:
                    print("Invalid Input !")


    

            elif choice == 4:

                print("\n===== Data Visualization =====")

                print("1. Bar Chart")
                print("2. Pie Chart")
                print("3. Line Chart")
                print("4. Scatter Chart")
                print("5. Histogram Chart")

                ch = int(input("Enter Choice (1-5) :- "))
                
                try:
                        

                    if ch == 1:

                        sns.barplot(data=self.data, x="category", y="total sales",errorbar=None)

                        plt.title("Category Wise Sales")
                        plt.show()

                    elif ch == 2:

                        sales = self.data.groupby("category")["total sales"].sum()

                        sales.plot.pie(autopct="%1.1f%%")

                        plt.title("Category Wise Sales")
                        plt.ylabel("")
                        plt.show()

                    elif ch == 3:

                        daily = self.data.groupby("date")["total sales"].sum().reset_index()

                        sns.lineplot(data=daily, x="Date", y="total sales")

                        plt.title("Daily Sales Trend")
                        plt.show()

                    elif ch == 4:

                        self.data.plot.scatter(x="price", y="total sales")

                        plt.title("Price vs Total Sales")
                        plt.show()

                    elif ch == 5:

                        self.data["total sales"].plot.hist()

                        plt.title("Sales Distribution")
                        plt.show()

                    else:
                        print("Invalid Choice!")
                except:
                    print("Invalid input !")


      

            elif choice == 5:

                print("\n========== RETAIL SALES REPORT ==========")

                print("Total Sales:", self.data["total sales"].sum())

                print("Average Sales:", round(self.data["total sales"].mean(), 2))

                print("Maximum Sales:", self.data["total sales"].max())

                print("Minimum Sales:", self.data["total sales"].min())

                print("Total Quantity Sold:", self.data["quantity sold"].sum())

                product = self.data.groupby("product")["quantity sold"].sum()

                print("Most Popular Product:", product.idxmax())

                print("\n========== DATASET INFORMATION ==========")

                print("Total Records:", len(self.data))

                print("Total Columns:", len(self.data.columns))

                print("Missing Values:", self.data.isnull().sum().sum())

                print("Duplicate Records:", self.data.duplicated().sum())


         

            elif choice == 6:

                print("\nThank You For Using Retail Sales Data Analyzer!")
                break

            else:

                print("Invalid Choice! Please Enter Between (1-6).")



obj = RetailAnalyzer()
obj.load_data()
obj.menu()