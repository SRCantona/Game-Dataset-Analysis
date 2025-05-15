import pandas as pd
import time as pt
import sys
sys.setrecursionlimit(15000)


def insertion_sort(collection: list) -> list:
    for insert_index, insert_value in enumerate(collection[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index + 1] = collection[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            collection[insert_index + 1] = insert_value
    return collection


# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def insertionBestCase():
    # making data frame from csv file
    insertionBest = pd.read_csv("Video_Games_Sales.csv")
    list1 = (insertionBest['NA_Sales'].to_list())
    data = list1[16394:16404]

    print("""this is a elements from Confirmed column sorted in order
    which is the best case for insertion sort """)
    print(data)

    # record start time
    start = pt.time()
    # calls the insertion sort function
    ib = insertion_sort(data)
    # record end time
    end = pt.time()

    print("after applying insertion sort")
    print(ib)
    # print elapsed time in seconds
    print("Elapsed time", (end - start) * 10**6, "ms.")


def quickBestCase():
    # making data frame from csv file
    quickBest = pd.read_csv("Video_Games_Sales.csv")
    list1 = (quickBest['Other_Sales'].to_list())
    data = list1[42:54]

    print("""this shows the pivit wil go to the middle
    which is the best case for quick sort """)
    print(data)
    size = len(data)

    # record start time
    # start = pt.time()
    # calls the quick sort function
    quickSort(data, 0, size - 1)
    # record end time
    # end = pt.time()

    print("after applying quick sort")
    print(data)
    # print elapsed time in seconds
    # print("Elapsed time", (end - start) * 10**, "ms.")


def QuickWorstCase():
    # making data frame from csv file
    quickWorst = pd.read_csv("Video_Games_Sales.csv")
    list4 = (quickWorst['NA_Sales'].to_list())
    data = list4[16394:16404]

    print("""this is a elements from Confirmed column sorted in order
    which is the worst case for quick sort """)
    print(data)
    size = len(data)

    # record start time
    # start = pt.time()
    # calls the insertion sort function
    quickSort(data, 0, size - 1)
    # record end time
    # end = pt.time()

    print("after applying quick sort")
    print(data)
    # print elapsed time in seconds
    # print("Elapsed time", (end - start) * 10**, "ms.")


def insertionAverageCase(i):
    # making data frame from csv file
    insertionAverage = pd.read_csv("Video_Games_Sales.csv")
    list2 = (insertionAverage['EU_Sales'].to_list())
    data = list2[0:i]
    print("""this is a elements from Confirmed column 
    are in jumbled order that is not properly ascending and not properly descending
    which is the average case for insertion sort """)
    print(data)
    # record start time
    start = pt.process_time()
    # calls the insertion sort function
    ia = insertion_sort(data)
    # record end time
    end = pt.process_time()

    print("after applying insertion sort")
    print(ia)
    # print elapsed time in seconds
    print("Elapsed time using process_time()", (end - start) * 10**3, "ms.")


def quickAverageCase(i):
    # making data frame from csv file
    quickAverage = pd.read_csv("Video_Games_Sales.csv")
    list5 = (quickAverage['EU_Sales'].to_list())
    data = list5[0:i]
    print("""this is a elements from Confirmed column 
    are in jumbled order that is not properly ascending and not properly descending
    which is the average case for quick sort """)
    size = len(data)
    # record start time
    start = pt.process_time()

    # calls the insertion sort function
    quickSort(data, 0, size - 1)

    # record end time
    end = pt.process_time()

    print("after applying quick sort")
    print(data)
    # print elapsed time in seconds
    # print("Elapsed time using process_time()", (end - start) * 10**3 , "ms.")


def insertionWorstCase():
    # making data frame from csv file
    insertionWorst = pd.read_csv("Video_Games_Sales.csv")
    # ser = pd.Series(insertionWorst['Deaths'])
    list3 = (insertionWorst['JP_Sales'].to_list())
    data = list3[0:10]
    print("""this is a elements from Deaths column sorted in reverse 
    which is the worst case for insertion sort """)
    print(data)
    # record start time
    # start = pt.process_time()
    # calls the insertion sort function
    iw = insertion_sort(data)
    # record end time
    # end = pt.process_time()

    print("after applying insertion sort")
    print(iw)
    # print elapsed time in seconds
    # print("Elapsed time", (end - start) * 10**3, "ms.")

    # return pt.timeit(best.apply(insertion_sort), number =1)


def main():
    loop = True
    while loop:
        print("""
              1- Insertion sort
              2- Quick sort
              3- quit
              """)
        scan = int(input("Choose the any sorted algorithm: "))
        if scan == 1:
            BAW = True
            while BAW:
                input1 = int(input("""
                      print:
                      1- Best case
                      2- Average case
                      3- Worst case
                      4- Quit
                      Choose: 
                      """))
                if input1 == 1:
                    insertionBestCase()
                elif input1 == 2:
                    input3 = int(input("Enter the range: between 10 to 10000: "))
                    if 10 > input3 > 10000:
                        print("Out of range")
                        BAW = False
                    else:
                        insertionAverageCase(input3)
                elif input1 == 3:
                    insertionWorstCase()
                else:
                    BAW = False
        elif scan == 2:
            BAW = True
            while BAW:
                input1 = int(input("""
                      print:
                      1- Best case
                      2- Average case
                      3- Worst case
                      4- Quit
                      Choose: 
                      """))
                if input1 == 1:
                    quickBestCase()
                elif input1 == 2:
                    input3 = int(input("Enter the range between 10 to 10000: "))
                    if 10 < input3 > 10000:
                        print("Out of range")
                        BAW = False
                    else:
                        quickAverageCase(input3)
                elif input1 == 3:
                    QuickWorstCase()
                else:
                    BAW = False
        else:
            loop = False


if __name__ == "__main__":
    main()