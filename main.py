from utils import get_data, get_filtered_data, get_last_values, get_formated_data
from pprint import pprint


def main():
    count_values = 5
    filtered_empty_from = True

    data = get_data()
    data = get_filtered_data(data, filtered_empty_from)
    data = get_last_values(data, count_values)
    data = get_formated_data(data)

    for row in data:
        print(row, end='\n')


if __name__ == "__main__":
    main()
