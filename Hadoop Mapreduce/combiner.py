import sys

def read_map_output(file):
    for line in file:
        yield line.strip().split("\t",3)

'''
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
