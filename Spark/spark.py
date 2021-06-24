
import argparse

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Application Name").getOrCreate()

def extractData(record):
    try:
        video_id = record.split(",")[0]
        #trending_date = record.split(",")[1]
        country = record.split(",")[17]
        views = int(record.split(",")[8])
        country_id = country + ";" + video_id
        return (country_id,views)
    except:
        return ()


def Process(line):
    try:
        if len(list(line[1])) >= 2:
         for i in range(0,len(list(line[1]))-1):
             for j in range(i+1,len(list(line[1]))-1):
                 if line[1][i]>line[1][j]:
                     line[1][i],line[1][j] = line[1][j],line[1][i]
             n1 = int((line[1][0]))
             #print(n1)
             n2 = int((line[1][1]))
             #print("##"+str(n2))
             value = abs(n1-n2)
             if n1>=n2:
              increase = 100*value/n2
              result = round(increase, 1)
             elif n1<n2:
              increase = 100*value/n1
              result = round(increase,1)
             #print(increase)
             if result > 1000:
             #print("##{},{}% ".format(line[0],result))
              return("{},{}% ".format(line[0],result))
    except:
        pass

def Final_sort(list):
        print(len(list))

        country,i= list.split(';')

        id,increase = i.split(',')

        return(country+"-"+increase,id)


def reorder(list):
    country,increase=list[0].split("-")
    id=list[1]

    return("{};{},{}".format(country,id,increase))



if __name__ == "__main__":
 #sc = SparkContext(appName=" trending impact")
 parser = argparse.ArgumentParser()
 parser.add_argument("--input", help="the input path",
                        default='/Users/alfred/PycharmProjects/demo/')
 parser.add_argument("--output", help="the output path",
                        default='/Users/alfred/PycharmProjects/demo/t25')

 args = parser.parse_args()
 input_path = args.input
 output_path = args.output

 data = spark.read.csv(input_path+"Allvideos.csv", header=True).rdd

 #print(data.take(2))

 data1=data.map(lambda x: (x.country + ";"+x.video_id,x.views))

 #print(data1.take(10))

 processed_data = data1.groupByKey().map(lambda x: (x[0], list(x[1])))
 #print(processed_data.take(100))

 result = processed_data.map(Process)
 #print(result.take(3))
 result2= result.filter(lambda x:  x is not None)
 #print(result2.take(10))
 #result3 = result2.sort()

 result3=result2.map(Final_sort)

 res = result3.sortByKey(False)

 #print(res.take(15))
 #print (final.take(15))

 res2=res.map(reorder)
 res2.saveAsTextFile(output_path)
 #print(res2)









