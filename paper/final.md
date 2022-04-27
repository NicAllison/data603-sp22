## Beginning Guide for Hive and Pig

&ensp; &ensp; This article is going give a brief introduction on Apache Hive and Apache Pig. The document is going to go into detail on how to set up their environments as well as going into the languages that control Pig and Hive. The article will also provide examples on using Hive and Pig which will cover adding data, displaying the data, as well as finding the average, maximum, and minimum.

&ensp; &ensp; Apache Hive is a data warehouse tool, similar to Apache Spark, which allows you to run commands on Hadoop without having to deal with the complicated commands of MapReduce. Apache Hive is able to do this because it uses MapReduce which is one of the two ways that Hadoop processes data. When you are running commands for Hive you will be using HQL, Hive Query Language, which is similar SQL but it is not a relational database. HQL is not a relational database because it uses a schema for each database and it uses Hadoop Distributed File System (HDFS). HQL does have very similar commands to SQL which you will soon seen in action once you have set up the Hive Environment.

&ensp; &ensp; The Set up for Apache Hive environment requires the installation of Docker. You are able to install it by going to https://docs.docker.com/get-docker/ and you will be given the option to download it based on what Operating System that you are using. Once Docker is installed the first step is to open a command line terminal so you can clone the repository. 
```
  git clone https://github.com/big-data-europe/docker-hive.git
```
This command goes to the website and makes a copy of all the data that is inside of it and pulls it down to a folder on your local machine. Once the information is downloaded you can access it.
```
  cd docker-hive
```
The cd is a common command for Linux, Mac and Windows Operating Systems to go through the folders on your computer. After you are in the folder you will run two commands which are used to build the image.
```
  docker-compose up -d 
```
```
  docker-compose up -d presto-coordinator 
```
The final step in setting up the Docker image is creating the container. Since this is a large image which requires multiple pieces for the container to properly run that is why there are multiple building steps in creating the container.
```
  docker-compose exec hive-server bash
```
You should now be inside of the Docker image, and the final step is to open Hive.  
```
  /opt/hive/bin/beeline -u jdbc:hive2://localhost:10000
```
With this command you have the Docker image fully operational, and are able to create HQL queries, databases, and tables.
  
&ensp; &ensp; Currently you should have the repository installed, Docker installed, inside of the Docker container, and opened into Hive where you can begin writing code. In this example you will need to write in each name and age of the artist at this time, due to there being issues with adding the csv file into this container. The first step is to create a Database.
```
CREATE DATABASE art;
```
```
use art;
```
You will need to create a database otherwise Hive will not understand where the table and the data will need to be added. Once you have created the Database you will need to run the use command otherwise Hive will not understand which database you want to access. The next step is to create the table to add the data.
```
create table artist (name string, age int);
```
You should now have a database being used and a table running inside of it. When creating the tables you will need to have the keywords create and table then a name chosen by you for each value that is needed along with its datatype. At this point you will need to add data into the table.
```
INSERT INTO TABLE artist VALUES ('Vincent van Gogh',37), ('Paul Gauguin',55), ('Claude Monet',86), ('Edouard Manet',51), ('Paul Cezanne',67), ('Auguste Renoir',78), ('Pablo Picasso',91), ('Edgar Degas',83), ('Leonardo da Vinci',67), ('Rembrandt',63), ('Sandro Botticelli',65), ('Peter Paul Rubens',63), ('Michaelangelo',89), ('Francisco Goya',82), ('Gustave Courbet',58), ('Salvador Dali',85);
```
To add value into the table you can either add them one at a time or you can as shown above add all at once. When adding data to tables you will need to have the keywords INSERT, INTO, TABLE, and VALUES. You will also need to make sure you specify after table which table you intend to add the information to, as well as you will need to put parenthesis around the values you intend to add. Similar to Python you will have to use quotations be it single or double when adding in Strings and will not need quotes for integers and floats. The next step it find the Average, Maximum, and Minimum values from the data.
```
select AVG(age) from artist; 
select MAX(age) from artist; 
select MIN(age) from artist;
```
```
+-----+
| _c0 |
+-----+
| 70.0|
+-----+

+-----+
| _c0 |
+-----+
| 91  |
+-----+

+-----+
| _c0 |
+-----+
| 37  |
+-----+
```
As you can tell all three commands for finding the Maximum, Minimum, and Average are very similar. Except the keywords that are use MAX, MIN, and AVG the other keywords select and from remain the same even the column that is selected as well as the table. Finally you can see results.
```
show tables;
show databases;
```
Lastly you can see all databases and tables that were created with the show command followed by either general or specific tables and databases. Next you will learn about Apache Pig, how to set up the environment, as well as running commands with Pig.

&ensp; &ensp; Apache Pig is similar to MapReduce where instead of being a process for Hadoop, Pig works along side with Hadoop so that you can analyze large sets of data. Coding with Pig is easier than using MapReduce because with MapReduce you have to go through the complexity of Java as well as having to deal with the commands for MapReduce. To run commands with Pig you will use a language called PigLatin which has similarities to SQL, but you do not specifically define tables and databases. In the example used later you will end up using a CSV file but most Pig commands require that any file is first transformed into a HDFS.

&ensp; &ensp; Setting up the Environment for Apache Pig is a little daunting if you are not using a Mac. With a Mac all you will need to do is follow the proceeding steps below, if not the Docker image that is used does not work on a Windows machine, and there is no information if it will work on a Linux machine. If you happen to be using a Windows or Linux machine this guide does not show the environment set up but you can go to Apache Pig’s website or TutorialPoint they have instructions on how to install what is needed to run Apache Pig. The set up for Apache Pig with a Mac is simple, as long as you followed the Hive instructions on installing Docker than pulling and using the Docker Image is easy. First open up a command terminal and start off by pulling the Docker image. 
```
docker pull hakanserce/apache-pig
```
Once the image is pulled the next step is to build the image as a container; this command also adds a name pig-demo and will put you inside of the container. 
```
docker run --name pig-demo -it hakanserce/apache-pig /etc/bootstrap.sh -bash
```
Now that you are in the Docker image the next step is to import files that you will need for this example, it is easiest to first create a folder inside of the container and label it data so that when it comes time to adding in the csv file it will have no issues.
```
mkdir /data
```
To import the data into the container it is easier to use a separate terminal so you will be able to continue using the container. If you end up closing the container remember that to reopen the container you will have to go into the Docker Application and find the pig-demo then start and open in Terminal to reopen the container.
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
the second option is the easiest because you will be able to use the normal csv file and can avoid creating an hdfs which is required for the first option and is not covered in this tutorial. At this point as long as you are using a Mac you should be inside of the container with pig running and the csv file ready to read.

&ensp; &ensp; Now that the Apache-Pig Environment is set up you should have the container and Pig running along with having the csv file imported. Now you can begin running commands. First you will need to import the csv file which requires the need of the Load command.
```
artist = LOAD ‘artist_age.csv’ USING PigStorage(',') AS (name:chararray, age:isnt);
```
The load command has a few distinct parts first it needs the location of the file in quotations, the function that is going to be use, and the schema for the data. In between each part of the load you will see the keywords Load, Using, and As. In this example the function being used is PigStorage there are a few others out there such as JsonLoad, TextLoader, BinStorage. The next step is grouping the data.
```
artist_gp_all = Group artist All;
```
The data needs to be grouped because it allows for a relationship between the data. The Group function has two parts, it requires the function that needs a relationship and by what value there is going to be a relationship. For this tutorial GROUP and ALL are the only keywords that are used, but you can replace ALL with BY and you could specify for this example it could be used with age or name. Finally you can find the Maximum, Minimum, and Average.
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
```
(37)
(91)
(70.0)
(Vincent van Gogh,37)
(Paul Gauguin,55)
(Claude Monet,86)
(Edouard Manet,51)
(Paul Cezanne,67)
(Auguste Renoir,78)
(Pablo Picasso,91)
(Edgar Degas,83)
(Leonardo da Vinci,67)
(Rembrandt,63)
(Sandro Botticelli,65)
(Peter Paul Rubens,63)
(Michaelangelo,89)
(Francisco Goya,82)
(Gustave Courbet,58)
(Salvador Dali,85)
```
You should have noticed even though you put in the command there was no output that is because you will need to use the DUMP command which requires the keyword dump followed by the value that you want to view. This is similar to a print function in Python. Now you are able to add data into Pig, add relationships to the data, print the data, and find the Maximum, Minimum, and Average values all in Apache Pig.

&ensp; &ensp; During this beginners guide you should have gained some insight into what Apache Hive and Apache Pig are. While also learning how to set up the Docker image to run their environments. Finally you should have also learned about using the languages to find the Maximum, Minimum, and Average ages of the Artists from the data that was given in the beginning.



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
