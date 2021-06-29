# Youtube-Trending-Analysis-with-Hadoop-and-Spark

Library required to run the code:
-pyspark

Python Version: 3.3 or higher

Development Environment: PyCharm

The MapReduce implementation should run in a pseudo-distributed mode.

The Spark implementation should run in a standalone cluster or YARN cluster on a single machine.

For detailed technical design and decription, please refer to Youtube Analysis_report.PDF

1.Analysis Workload Description

1.1 Category and Trending Correlation

Some videos are trending in multiple countries. We are interested to know if there is any
correlation between category and overlapping trending. For instance, if UK and CA users
have common interests in music, but very different interest in sports, we might see 3%
trending music videos in UK that also appear in the trending list of CA; while only 0.5% of
trending sports videos in UK appears in CA’s trending list.

In this workload, it is expected to find out, for a given pair of countries A and B,
for each category in country A, the total number of videos trending in country A and
the percentage of them that are also trending in country B. For any video with multiple
trending appearances in a country, it should be counted as one video in that country.
The result would look like, suppose the country is GB and US
Entertainment; total: 617; 31.4% in US
Sports; total:152; 17.1% in US
...
It means that there are 617 videos from Entertainment category in UK’s trending list.
31.4% of the 617 videos also appear in US’s trending list; There are 152 videos from Sports
category in UK’s trending list. 17.1% of the 100 videos also appear in US’s trending list.


1.2 Impact of Trending on View Number

Listing a video as trending would help it attract more views. The view number may quickly
increase after a video is listed as trending for the first time. In fact it is not unusual for the
view number to double between a video’s first and second trending appearance.

Below are a few records of a particular video:
videoID Trending Date Publish Time Views Country

xYtsL9znopI 18.17.02 2018-02-16T14:00:09.000Z 960453 CA

xYtsL9znopI 18.18.02 2018-02-16T14:00:09.000Z 2109193 CA

xYtsL9znopI 18.19.02 2018-02-16T14:00:09.000Z 2768767 CA

xYtsL9znopI 18.20.02 2018-02-16T14:00:09.000Z 3213410 CA

The video has four trending appearances in CA between February 17 of 2018 and February
20 of 2018. The view number in its first appearance (2018/02/17) is 960,453; the view
number in its second appearance (2018/02/18) is 2,109,193. There is a 119.6% increase
between the second and first appearance. In contrast the increase between the third and
the second appearance is only 31.2%.

In this workload, it is expected to find out, for each country, all videos that have greater than or equal to 1,000% increase in viewing number between its second and first
trending appearance. The result should be grouped by country and sorted discerningly by
percent increase.

The result would look like

DE; V1zTJIfGKaA, 19501.9%

DE; RIgNyiGttog, 12346.5%

...
CA; _I_D_8Z4sJE, 8438.1%

CA; -K9ujx8vO_A, 8298.3%
