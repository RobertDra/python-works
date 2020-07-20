result_list = []
list1 = [1,1,2,3,5,8,13,21,34,55,89]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]


def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                if x not in result_list:

                  result_list.append(x)

def result(output):
    print(result_list)

def main():
    output = common_data(list1, list2)
    result(output)

if __name__ == '__main__':
    main()
