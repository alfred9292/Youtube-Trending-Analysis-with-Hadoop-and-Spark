import sys
dict1 = {}
dict2 = {}
dict_same = {}
dict_total = {}
count1 = 0
count2 = 0

'''
In the reducer phase, two dictionaries are created for each country respectively. 
If the indicator shows 1, the record will be inserted to dictionary 1 with key value pair of video id and category. The same principle applies to indicators of 2. 
The next step is to find from dictionary 1, how many records actually overlap with dictionary 2, the result will be stored in the dictionary same with key value pair of category and its corresponding counts. Then for country 1, 
dictionary total is created to calculate the total number for each category in country 1. The last stage is to find for each category in the overlap dictionary, the corresponding count for dictionary total will be count 1 and the count for dictionary same will be count 2,
 the answer will simply be count2/count1 and eventually print the output based on the required format.
'''


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











