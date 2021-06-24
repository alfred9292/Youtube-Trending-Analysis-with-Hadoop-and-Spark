import csv
import sys
dict1={}
dict2={}

def mapper():

    with open("./ALLvideos.csv", 'r') as fr:
     rows =csv.DictReader(fr)
     python_arguments = sys.argv
     c1 = python_arguments[1]
     c2 = python_arguments[2]
     for row in rows:
         if row['country'] == c2:
          dict1[row['video_id']] = row['category']+c2
          print(row['category'], row['video_id']+';2'+';'+c1)

         if row['country'] == c1:
          dict2[row['video_id']] = row['category']+c1
          print(row['category'], row['video_id']+';1'+';'+c1)


if __name__ == "__main__":
    mapper()

