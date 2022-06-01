from matplotlib import pyplot as plt

def plot_win_percentage():

    with open("results.txt") as fp:
        results = list()
        for line in fp:
            token = line.rstrip('\n')
            results.append(token)

    print(results)

    results_count = list()
    results_count.append(results.count('Win'))
    results_count.append(results.count('Loss'))
    results_count.append(results.count('Incomplete'))

    print(results_count)

    results_percentage = [int((each_element/sum(results_count))*100) for each_element in results_count]
    print(results_percentage)
    pie_chart_labels = ["Win","Loss","Incomplete"]

    plt.title("Number of games = 20\nDepth = 10\nNumber of searches = 50")
    plt.pie(results_percentage, labels=pie_chart_labels)
    plt.show()

def main():
    plot_win_percentage()

if __name__ == "__main__":
    main()