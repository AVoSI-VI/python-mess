def longest_series_of_neighbours(l1: list):
    l = 1
    r = 1
    for blah in range(0, len(l1) - 1):
   #     print(l1[blah])
  #      print(l1[blah + 1])
 #       print(l1[blah - 1])
        if l1[blah] - l1[blah + 1] == 1 or l1[blah + 1] - l1[blah] == 1:
            r += 1
 #       elif l1[blah] - l1[blah - 1] == 1:    
 #           r += 1
        else:
            r = 1
        l = max(l, r)
    return l



if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))