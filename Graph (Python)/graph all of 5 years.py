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
    """Print main Graph"""
    graph2014(2014, [])
    graph2015(2015, [])
    graph2016(2016, [])
    graph2017(2017, [])
    graph2018(2018, [])

def graph2014(year, lis_y):
    """Plot Graph between year 2013-2014 at range 28 Dec 2013 to 3 Jan 2014"""
    lis_x = ["28 Dec", "29 Dec", "30 Dec", "31 Dec", "1 Jan", "2 Jan", "3 Jan"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Years'])
    dataframe = group.get_group(year)
    accident = dataframe[dataframe['Types'] == "accident"]
    injured = dataframe[dataframe['Types'] == "injured"]
    dead = dataframe[dataframe['Types'] == "dead"]
    data_accident = point(accident, lis_y)
    data_injured = point(injured, lis_y)
    data_dead = point(dead, lis_y)
    plt.plot(lis_x, data_accident, "o-", color="blue", label="Accident")
    plt.plot(lis_x, data_injured, "o-", color="magenta", label="Injured")
    plt.plot(lis_x, data_dead, "o-", color="red", label="Dead")
    plt.title("สถิติการเกิดอุบัติเหตุและผู้ประสบเหตุ", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง หรือ คน)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ช่วงปี 2013 ไป 2014", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def graph2015(year, lis_y):
    """Plot Graph between year 2014-2015 at range 30 Dec 2014 to 5 Jan 2015"""
    lis_x = ["30 Dec", "31 Dec", "1 Jan", "2 Jan", "3 Jan", "4 Jan", "5 Jan"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Years'])
    dataframe = group.get_group(year)
    accident = dataframe[dataframe['Types'] == "accident"]
    injured = dataframe[dataframe['Types'] == "injured"]
    dead = dataframe[dataframe['Types'] == "dead"]
    data_accident = point(accident, lis_y)
    data_injured = point(injured, lis_y)
    data_dead = point(dead, lis_y)
    plt.plot(lis_x, data_accident, "o-", color="blue", label="Accident")
    plt.plot(lis_x, data_injured, "o-", color="magenta", label="Injured")
    plt.plot(lis_x, data_dead, "o-", color="red", label="Dead")
    plt.title("สถิติการเกิดอุบัติเหตุและผู้ประสบเหตุ", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง หรือ คน)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ช่วงปี 2014 ไป 2015", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def graph2016(year, lis_y):
    """Plot Graph between year 2015-2016 at range 29 Dec 2015 to 4 Jan 2016"""
    lis_x = ["29 Dec", "30 Dec", "31 Dec", "1 Jan", "2 Jan", "3 Jan", "4 Jan"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Years'])
    dataframe = group.get_group(year)
    accident = dataframe[dataframe['Types'] == "accident"]
    injured = dataframe[dataframe['Types'] == "injured"]
    dead = dataframe[dataframe['Types'] == "dead"]
    data_accident = point(accident, lis_y)
    data_injured = point(injured, lis_y)
    data_dead = point(dead, lis_y)
    plt.plot(lis_x, data_accident, "o-", color="blue", label="Accident")
    plt.plot(lis_x, data_injured, "o-", color="magenta", label="Injured")
    plt.plot(lis_x, data_dead, "o-", color="red", label="Dead")
    plt.title("สถิติการเกิดอุบัติเหตุและผู้ประสบเหตุ", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง หรือ คน)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ช่วงปี 2015 ไป 2016", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def graph2017(year, lis_y):
    """Plot Graph between year 2016-2017 at range 30 Dec 2016 to 5 Jan 2017"""
    lis_x = ["30 Dec", "31 Dec", "1 Jan", "2 Jan", "3 Jan", "4 Jan", "5 Jan"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Years'])
    dataframe = group.get_group(year)
    accident = dataframe[dataframe['Types'] == "accident"]
    injured = dataframe[dataframe['Types'] == "injured"]
    dead = dataframe[dataframe['Types'] == "dead"]
    data_accident = point(accident, lis_y)
    data_injured = point(injured, lis_y)
    data_dead = point(dead, lis_y)
    plt.plot(lis_x, data_accident, "o-", color="blue", label="Accident")
    plt.plot(lis_x, data_injured, "o-", color="magenta", label="Injured")
    plt.plot(lis_x, data_dead, "o-", color="red", label="Dead")
    plt.title("สถิติการเกิดอุบัติเหตุและผู้ประสบเหตุ", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง หรือ คน)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ช่วงปี 2016 ไป 2017", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def graph2018(year, lis_y):
    """Plot Graph between year 2017-2018 at range 28 Dec 2016 to 3 Jan 2017"""
    lis_x = ["28 Dec", "29 Dec", "30 Dec", "31 Dec", "1 Jan", "2 Jan", "3 Jan"]
    data = pd.read_csv('data1.csv')
    group = data.groupby(['Years'])
    dataframe = group.get_group(year)
    accident = dataframe[dataframe['Types'] == "accident"]
    injured = dataframe[dataframe['Types'] == "injured"]
    dead = dataframe[dataframe['Types'] == "dead"]
    data_accident = point(accident, lis_y)
    data_injured = point(injured, lis_y)
    data_dead = point(dead, lis_y)
    plt.plot(lis_x, data_accident, "o-", color="blue", label="Accident")
    plt.plot(lis_x, data_injured, "o-", color="magenta", label="Injured")
    plt.plot(lis_x, data_dead, "o-", color="red", label="Dead")
    plt.title("สถิติการเกิดอุบัติเหตุและผู้ประสบเหตุ", fontname='JasmineUPC', fontsize='25')
    plt.ylabel("ปริมาณ หน่วย(ครั้ง หรือ คน)", fontname='JasmineUPC', fontsize='20')
    plt.xlabel("ช่วงปี 2017 ไป 2018", fontname='JasmineUPC', fontsize='20')
    plt.legend()
    plt.show()

def point(data1, lis_y):
    """The position of data that will plot on graphs"""
    lis_y = []
    for i in data1.Times:
        lis_y.append(int(i))
    return lis_y

main()
