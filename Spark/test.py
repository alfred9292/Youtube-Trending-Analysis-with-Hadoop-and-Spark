#import collections

#lst=[1,1,2,2,2,3,3,3,3]

#d = collections.Counter(lst)
#str = 'entertainment 1234567;us;uk'

#category, intermediate = str.split(' ')
#video_id = intermediate.split(';')[0]
#country = intermediate.split(';')[-2]
#c1 = intermediate.split(';')[-1]
#print(category, video_id, country, c1)

#print(d)

def Process(line):
    if len(list(line[1])) >= 2:
     for i in range(0,len(list(line[1]))):
         for j in range(i+1,len(list(line[1]))):
             if line[1][i]>line[1][j]:
                 line[1][i],line[1][j] = line[1][j],line[1][i]
     increase = 100*(line[1][2]-line[1][1])/line[1][1]
     if increase > 10:
      return(line[0],increase)
     else:
         return 0

line = 'ga',[7,5,3,4,2,10]

print(line[1])

if len(list(line[1])) >= 2:
    for i in range(0, len(list(line[1]))):
        for j in range(i + 1, len(list(line[1]))):
            if line[1][i] > line[1][j]:
                line[1][i], line[1][j] = line[1][j], line[1][i]
    increase = 100 * (line[1][1] - line[1][0]) / line[1][0]
    print(line[1][0],line[1][1],increase)
    if increase > 1000:
        print (line[0], increase+'%')
    else:
        print(0)

str = "video_id='LgVi6y5QIjM', trending_date='17.14.11', title='Sing zu Ende!"

video_id = str.split(",")[0].split("=")[-1]

print(video_id)


list2=['de;4567,200','us;789,150','us;123,300','de;123,300']
for item in list2:
        country_id = item.split(',')[0]
        country = country_id.split(';')[0]
        increase = item.split(',')[-1]
        country_increase = country + increase
        print(country_increase)

        #for i in range(0, len(list2)):
           # for j in range(i + 1, len(list2)):
            #    if list2[i][country_increase] > list[j][country_increase]:
             #       list2[i], list2[j] = list2[j], list2[i]

#print (list2)