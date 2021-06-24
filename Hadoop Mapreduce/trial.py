import csv
c1='GB'
c2='US'
dict1={}
dict2={}



with open("./ALLvideos.csv", 'r') as fr:
     rows =csv.DictReader(fr)
     for row in rows:
         if row['country'] == c2:
          dict1[row['video_id']] = row['category']+c2
          print(row['category'], row['video_id']+';2')

         if row['country'] == c1:
          dict2[row['video_id']] = row['category']+c1
          print(row['category'], row['video_id']+';1')