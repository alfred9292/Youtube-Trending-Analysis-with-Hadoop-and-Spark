import sys

def read_map_output(file):
    for line in file:
        yield line.strip().split("\t",3)

'''
Combiner is used to minimize the input to reduce phase by removing the duplicate records. 
This is achieved by using country plus video id to search in the list created in the combiner function, if there is no hit, the combiner will output the results. 
Otherwise it will jump to the next record, denoting a detection of duplicate records.
'''
def combiner():
    data = read_map_output(sys.stdin)
    list=[]
    for category,video_id,country,indicator in data:
        check = country+video_id
        if check in list:
            continue
        if check not in list:
            list.append(check)
            print("{}\t{}\t{}\t{}".format(category, video_id, country, indicator))

if __name__ == "__main__":
    combiner()
