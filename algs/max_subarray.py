import sys
from matplotlib import pyplot as plt
def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -sys.maxsize
    right_sum = -sys.maxsize
    sum = 0
    max_left = 0
    max_right = 0
    for i in reversed(range(low, mid+1)):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    for j in range(mid, high+1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(arr, low, high):
    # base case
    if high == low:
        return (low, high, arr[low])
    # recursive case
    else:
        # division of params
        mid = (low + high) //2
        (left_low, left_high, left_sum) = find_maximum_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def transform_to_difference_list(arr):
    result = []
    for i in range(len(arr)-2):
        result.append(arr[i+1] - arr[i])
    return result

if __name__ == '__main__':
    stock_ls = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    plt.plot(stock_ls)
    plt.show()
    diff_list = transform_to_difference_list(stock_ls)
    plt.plot(diff_list)
    plt.show()
    # ls = [2, -3, 4, 1, -2, 4,1, 3 , -2, -6]
    # ls = [1,2,3,4]
    low, high, sum = find_maximum_subarray(diff_list, 0, len(diff_list)-1)
    print(low, high, sum)