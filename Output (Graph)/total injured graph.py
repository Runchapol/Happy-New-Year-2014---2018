""" Graph Injured every Year """
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """Print main Graph"""
    graphinjured("injured", [])


def graphinjured(injured, lis_y):
    lis_x = ["2014", "2015", "2016", "2017", "2018"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Types'])
    dataframe = group.get_group(injured)
    y2014 = dataframe[dataframe['Years'] == 2014]
    y2015 = dataframe[dataframe['Years'] == 2015]
    y2016 = dataframe[dataframe['Years'] == 2016]
    y2017 = dataframe[dataframe['Years'] == 2017]
    y2018 = dataframe[dataframe['Years'] == 2018]
    total_injured = total(y2014, y2015, y2016, y2017, y2018, lis_y)
    plt.plot(lis_x, total_injured, "o-", color="Green", label="injured")
    plt.title("สถิติผู้บาดเจ็บในแต่ละปี", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ปี", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def total(year2014, year2015, year2016, year2017, year2018, lis_y):
    """ Calculate sum of all data in all years """
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
    check = 0
    return lis_y

main()