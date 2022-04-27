## Beginning Guide for Hive and Pig

### 1. Opening Paragraph Explaining what is going to be covered
&ensp; &ensp; This article is going give a brief introduction on Apache Hive and Apache Pig. The document is going to go into detail on how to set up their environments as well as going into the languages that control Pig and Hive. The article will also provide an example on using Hive and Pig which will cover adding data, display the data, as well as finding the average, maximum, and minimum.


### 2. Paragraph that explains what Hive and HQL is
&ensp; &ensp; Apache Hive is a data warehouse tool, similar to Apache Spark, where it allows you to run commands on Hadoop without having to deal with the complicated commands of MapReduce. Apache Hive is able to do this because it sits on top of MapReduce which is one of the two ways that Hadoop processes data. When you are running commands for Hive you will be using HQL, Hive Query Language, which is similar SQL but it is not a relational database like SQL. Since HQL is used for a data warehouse tool it uses a schema in a database also since it can use HDFS files as the data, so this means that HQL is not a Relation Database. HQL does have very similar commands to SQL which you will soon seen in action once you have set up the Hive Environment.

Apache Hive is similar to MapReduce where it is tool that sits on top of Hadoop. For Hive it is a data warehouse that, “summarizes Big Data and makes querying and analyzing easy”(TutorialPoint 1). Using Hive to query data in Hadoop you can use the HiveQL, Hive Query Language, which act similar to SQL, but is not a relational database. 

### 3. How to set up Hive Environment that I used in Docker
&ensp; &ensp; To set Hive Environment first install we will be using Docker and command line operator to use the install and use Hive. We are going on the assumption that Docker you Docker already installed installed if not you can go to Dockers website and download it, it straight forward on downloading it. First open a command line operator and copy and paste this command:
```
  git clone https://github.com/big-data-europe/docker-hive.git
```
this command goes to the github repostity and pulls a copy of all the files inside of it. Once the information is downloaded go into the docker-hive folder by:
```
  cd docker-hive
```
once in the folder use: 
```
  docker-compose up -d 
```
follow it up by: 
```
  docker-compose up -d presto-coordinator 
```
which both of these commands are used to fully build the docker image that was downloaded. Finally you can access the Docker image from the command line by doing
```
  docker-compose exec hive-server bash
```
once the image is open you can access Hive by: 
```
  /opt/hive/bin/beeline -u jdbc:hive2://localhost:10000
```
Now you are inside and can begin creating HQL commands. </li>
  
### 4. How to generate the database, table, average, minimum, maximum, and showing output
&ensp; &ensp; Currently you should have the repository installed, Docker installed, inside of the Docker container, and opened into Hive where you can begin writing code. In this example you will need to write in each name and age of the artist at a time do to there being issues with adding the csv file into this container. The first step is to create a Database.
```
CREATE DATABASE art;
```
```
use art;
```
You will need to create a database because Hive will not understand where the table and the data will need to be added. Once you have created the Database you will need to use it otherwise Hive will not understand which database you want to use. The next step is to create the table to add the data in.
```
create table artist (name string, age int);
```
You should now have a database being used and a table running inside of it. When creating the tables you will need to have the keywords create and table then a name chosen by you for each value that is needed along with its datatype. The next step is to add data into the table.
```
INSERT INTO TABLE artist VALUES ('Edgar Degas', 83), ('Leonardo da Vinci', 67);
```





```
select AVG(age) from artist; 
```
Similarly as the average you can also produce the Minimum and Maximum.
```
select MAX(age) from artist; 
select MIN(age) from artist;
```
You can also print out all the information for be it the database and/or the table
```
show tables;
show databases;
```
### 5. Paragraph that explains what Pig and Pig Latin are
&ensp; &ensp; Apache Pig is similar to MapReduce, instead of being a process for Hadoop; Pig works along side with Hadoop so that you can analyze large sets of data. Coding with Pig is easier than using MapReduce because with MapReduce you have to go through the complexity of Java as well as having to deal with the commands for MapReduce. To run commands with Pig you will use a language called PigLatin which has a similar feel to SQL, but you do not define specifically tables and databases. In the example used later you will end up using a CSV file but most Pig commands require that any file is first transformed into a HDFS.

Apache Pig is similar to Spark and Hive where they sit on top of MapReduce. Pig is a tool that can analyze large sets of data and then able to represent the data as a data flow. When using Apache Pig it as a procedural language, Pig Latin which allows you to make perform MapReduce commands without having to use the clunky ness of Java.

### 6. How to set up Pig Environment that I used

&ensp; &ensp; Setting up the Environment for Apache Pig is a little daunting if you are not using a Mac. With a Mac all you will need to do is a follow the preceding steps below, if not the Docker image that is used does not work on a Windows machine, and there is no information if it will work on a Linux machine. If you happen to be using a Windows or Linux machine this guide does not show the environment set up but you can go to Apache Pig’s website or TutorialPoint they have instructions on how to install what is needed to run Apache Pig. The set up for Apache Pig with a Mac is simple, as long as you followed the Hive instructions on installing Docker than pulling and using the Docker Image it is easy to use. First open up a command terminal and start off by pulling the Docker image. 
```
docker pull hakanserce/apache-pig
```
Once the image is pulled the next step is to build the image as a container; this command also add’s a name pig-demo and will put you inside of the container. 
```
docker run --name pig-demo -it hakanserce/apache-pig /etc/bootstrap.sh -bash
```
Now that you are in the Docker image the next step is to import files that you will need for this example, it is easiest to first create a folder inside of the container and label it data so that when it comes time to adding in the csv file it is will have no issues.
```
mkdir /data
```
To import the data into the container it is easier to use a separate terminal so you will be able to continue using the container. If you end up closing the container remember that to reopen the container you’ll have to go into the Docker Application and find the pig-demo then start and open in Terminal to reopen the container.
```
docker cp artist_age.csv pig-demo:/data/
```
Now the container should be open and the csv file is imported the next step is to start up Pig, there are two ways you can choose from either
```
pig
```
or
```
pig -x local
```
the second option is the easiest because you will be able to use the normal csv file and can avoid creating an hdfs which is required for the first option and is not covered in this tutorial. At this point as long as you are using a Mac you should be inside of the container with pig running and the csv file ready to to read.

### 7. Code used to create each a table and pieces of data, then find the average, maximum, and minimum from the table as well as display all pieces of data as output

&ensp; &ensp; Now that the Apache-Pig Environment is set up and you should have the container and Pig running as well as having the csv file imported you can begin running commands. First you will need to import the csv file which requires the need of the Load command.
```
artist = LOAD ‘artist_age.csv’ USING PigStorage(',') AS (name:chararray, age:isnt);
```
The load command has a few parts first it needs the location of the file in quotations, followed by what function is going to be used, then the schema for the data in between each section you will see the keywords Load, Using, and As. The PigStorage is the type of function that is used for this example there are a few others out there such as JsonLoader, TextLoder, and BinStorage. The next step is grouping the data.
```
artist_gp_all = Group artist All;
```
The data needs to be grouped because it allows for a relationship with between the data. The Group function has two parts it requires the function that needs a relationship and by what value there is going to be a relationship. For the tutorial GROUP and ALL are the only keywords that are used, but you can replace ALL with BY and you could specify for this example it could be used with age or name. Finally you can find the Maximum, Minimum, and Average.
```
avr_age = foreach artist_gp_all generate AVG(artist.age);
min_age = foreach artist_gp_all generate MIN(artist.age);
max_age = foreach artist_gp_all generate MAX(artist.age);
```
Getting the Maximum, Average, and Minimum are very similar and only differ by the final keyword. Finding each of these requires the foreach function which requires the value that has a relationship and a function of what you are looking for in the data. You will also need these keywords FOREACH, GENERATE, MAX, MIN, and AVG.
```
Dump min_age;
Dump max_age;
Dump avr_age;
Dump artist;
```
You should have noticed even though you put in the command there was no output that is because you will need to use the DUMP command which requires the keyword dump follows by the value that you want to view it is similar to a print function in Python. Now you are able to add data into Pig, add relationships to the data, print the data, and find the Maximum, Minimum, and Average values all in Apache Pig.

### 8. Summary of what hive and pig are and how they display the average, max, and min. 
&ensp; &ensp; During this beginners guide you should have gained some insight into what Apache Hive and Apache Pig are. While also learning how to set up the Docker image to run there environments. Finally you should have also learned about using the language to be able to find the Maximum, Minimum, and Average ages of the Artists from the data that was given in the beginning.



#### References
1. Data Used: https://www.superprof.com/blog/top-20-artists/
2. Hive Docker: https://hub.docker.com/r/bde2020/hive/
3. Hive Docker Instructions: https://github.com/big-data-europe/docker-hive
4. Hive Help:https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.0/bk_data-access/content/new-feature-insert-values-update-delete.html
5. https://phoenixnap.com/kb/hive-create-table
6. https://datafibers-community.github.io/blog/2018/02/02/2018-02-02-hive-get-max-min-value-rows/
7. https://www.projectpro.io/questions/5760/hive-query-for-avg-of-marks
8. https://www.tutorialspoint.com/hive/index.htm
9. https://pig.apache.org/docs/latest/basic.html
10. https://www.tutorialspoint.com/apache_pig/apache_pig_avg.htm
