## Hive Pig Paper Outline

### 1. Opening Paragraph Explaining what is going to be covered
<li> This article is going give a brief introduction on Apache Hive and Apache Pig. The document is going to go into detail on how to set up their environments as well as going into the languages that control Pig and Hive. The article will also provide an example on using Hive and Pig which will cover adding information in, displaying the information, as well as finding the average, maximum, and minimum. </li>
<li> This document is going to cover how to use Apache Hive as well as Apache Pig, explain what Hive and Pig is, as well as instructions on how to set up the environment.</li>

### 2. Paragraph that explains what Hive and HQL is
<li> Apache Hive is similar to MapReduce where it is tool that sits on top of Hadoop. For Hive it is a data warehouse that, “summarizes Big Data and makes querying and analyzing easy”(TutorialPoint 1). Using Hive to query data in Hadoop you can use the HiveQL, Hive Query Language, which act similar to SQL, but is not a relational database. </li>

### 3. How to set up Hive Environment that I used in Docker
<li> To set Hive Environment first install we will be using Docker and command line operator to use the install and use Hive </li>
<li> We are going on the assumption that Docker you Docker already installed installed if not you can go to Dockers website and download it, it straight forward on downloading it.</li>
<li> First open a command line operator and copy and paste this command: 
  git clone https://github.com/big-data-europe/docker-hive.git 
  this command goes to the github repostity and pulls a copy of all the files inside of it</li>
<li> Once the information is downloaded go into the docker-hive folder by:
  cd docker-hive
  once in the folder use: 
  docker-compose up -d 
  follow it up by: 
  docker-compose up -d presto-coordinator 
  which both of these commands are used to fully build the docker image that was downloaded. </li>
<li> Finally you can access the Docker image from the command line by doing:
  docker-compose exec hive-server bash 
  once the image is open you can access Hive by: 
  /opt/hive/bin/beeline -u jdbc:hive2://localhost:10000</li>
<li> Now you are inside and can begin creating HQL commands. </li>
  
### 4. How to generate the database, table, average, minimum, maximum, and showing output
###### 1. Now that you should be inside of Hive you can begin writing HQL queries.
First you will have to create a database and a table to add information to. For this example we are going to create a art database and an artist table which will include the name and age at which the artist died unless they are still living. 
```
CREATE DATABASE art;
use art;
create table artist (name string, age int);
INSERT INTO TABLE artist VALUES ('Edgar Degas', 83), ('Leonardo da Vinci', 67);
```
###### 2. Next you can get the average of the table for this case by doing
```
select AVG(age) from artist; 
```
###### 3. Similarly as the average you can also produce the Minimum and Maximum.
```
select MAX(age) from artist; 
select MIN(age) from artist;
```
###### 4. You can also print out all the information for be it the database and/or the table
```
show tables;
show databases;
```
### 5. Paragraph that explains what Pig and Pig Latin are
<li> Apache Pig is similar to Spark and Hive where they sit on top of MapReduce. Pig is a tool that can analyze large sets of data and then able to represent the data as a data flow. When using Apache Pig it as a procedural language, Pig Latin which allows you to make perform MapReduce commands without having to use the clunky ness of Java. </li>

### 6. How to set up Pig Environment that I used
<li> Issues setting up Pig Environment.</li>

### 7. Code used to create each a table and pieces of data, then find the average, maximum, and minimum from the table as well as display all pieces of data as output
<li> First create a CSV/text file which will contain the names and age of the artists </li>
```
artist = LOAD ‘artist_age.csv’ USING PigStorage(',') AS (name:chararray, age:isnt);
artist_gp_all = Group artist All;
avr_age = foreach artist_gp_all generate AVG(artist.age);
min_age = foreach artist_gp_all generate MIN(artist.age);
max_age = foreach artist_gp_all generate MAX(artist.age);
Dump min_age;
Dump max_age;
Dump avr_age;
Dump artist;
```

### 8. Summary of what hive and pig are and how they display the average, max, and min. 

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
