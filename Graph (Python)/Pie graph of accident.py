"""

 ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██████╔╝███████║██████╔╝███████║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║

"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """Print accident graph (Pie Charts)"""
    accipie([])

def accipie(lis_y):
    """Plot a Pie Graph of that only accident happened"""
    lis_x = ["2014", "2015", "2016", "2017", "2018"]
    colors = ["dodgerblue", "lawngreen", "yellow", "orangered", "violet"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Types'])
    dataframe = group.get_group("accident")
    year2014 = dataframe[dataframe['Years'] == 2014]
    year2015 = dataframe[dataframe['Years'] == 2015]
    year2016 = dataframe[dataframe['Years'] == 2016]
    year2017 = dataframe[dataframe['Years'] == 2017]
    year2018 = dataframe[dataframe['Years'] == 2018]
    accident_all_years = total(year2014, year2015, year2016, year2017, year2018, lis_y)
    plt.pie(accident_all_years, labels=lis_x, autopct="%1.1f%%", startangle=90, colors=colors)
    plt.axis("equal")
    plt.title("สถิติการเกิดอุบัติเหตุเปรียบเทียบทุกปี", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("หน่วย(ครั้ง)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("จำนวนอุบัติเหตุ", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def total(year2014, year2015, year2016, year2017, year2018, lis_y):
    """Calculate sum of all data in all years"""
    check = 0
    for i in year2014.Times:
        check += int(i)
    lis_y.append(check)
    check = 0
    for i in year2015.Times:
        check += int(i)
    lis_y.append(check)
    check = 0
    for i in year2016.Times:
        check += int(i)
    lis_y.append(check)
    check = 0
    for i in year2017.Times:
        check += int(i)
    lis_y.append(check)
    check = 0
    for i in year2018.Times:
        check += int(i)
    lis_y.append(check)
    return lis_y

main()
