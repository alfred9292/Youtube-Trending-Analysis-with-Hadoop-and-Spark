import sys
dict1 = {}
dict2 = {}
dict_same = {}
dict_total = {}
count1 = 0
count2 = 0




def reducer():
    c1 = ""
    for line in sys.stdin:
      category, video_id, country, indicator = line.strip().split('\t', 3)
      if indicator == '1':
        dict1[video_id] = category
        c1 = country
      if indicator == '2':
        dict2[video_id] = category

    for key in dict2.keys():
        if key in dict1.keys():
            if dict1[key] in dict_same.keys():
                dict_same[dict1[key]] = +1
            else:
                dict_same[dict1[key]] = 1

    for key in dict1.keys():
        if dict1[key] in dict_total.keys():
                dict_total[dict1[key]] = +1
        else:
                dict_total[dict1[key]] = 1

    for key in dict_same.keys():
        count1 = dict_total[key]
        count2 = dict_same[key]
        percentage = 100 * count2/count1
        print("{}; total: {}; {}% in {}".format(key, count1, percentage, c1))


if __name__ == "__main__":
    reducer()











