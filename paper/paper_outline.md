## Hive Pig Paper Outline

### 1. Opening Paragraph Explaining what is going to be covered
<li> This article is going give a brief introduction on Apache Hive and Apache Pig. The document is going to go into detail on how to set up their environments as well as going into the languages that control Pig and Hive. The article will also provide an example on using Hive and Pig which will cover adding information in, displaying the information, as well as finding the average, maximum, and minimum. </li>
<li> This document is going to cover how to use Apache Hive as well as Apache Pig, explain what Hive and Pig is, as well as instructions on how to set up the environment.</li>

### 2. Paragraph that explains what Hive and HQL is

### 3. How to set up Hive Environment that I used in Docker
<li> To set Hive Environment first install we will be using Docker and command line operator to use the install and use Hive </li>
<li> We are going on the assumption that Docker you Docker already installed installed if not you can go to Dockers website and download it, it straight forward on downloading it.</li>
<li> First open a command line operator and copy and paste this command: git clone https://github.com/big-data-europe/docker-hive.git this command goes to the github repostity and pulls a copy of all the files inside of it</li>
<li> Once the information is downloaded go into the docker-hive folder then: docker-compose up -d followed by: docker-compose up -d presto-coordinator which both of these commands are used to fully build the docker image that was downloaded. </li>
<li> Finally you can access the Docker image from the command line by doing: docker-compose exec hive-server bash once the image is open you can access Hive by: /opt/hive/bin/beeline -u jdbc:hive2://localhost:10000</li>
<li> </li>
<li> </li>
<li> git clone this reposity https://github.com/big-data-europe/docker-hive you can also </li>
<li> This document has the instructions on how to get the Apache Hive Docker iamge running but I'm also going to go through the commands. </li>
  
### 4. How to generate the database, table, average, minimum, maximum, and showing output
![Alt text](https://github.com/NicAllison/data603-sp22/blob/Paper_Outline/paper/Creating_database_and_table.jpg)
![Alt text](https://github.com/NicAllison/data603-sp22/blob/Paper_Outline/paper/Hive_Average_Output.jpg)
![Alt text](https://github.com/NicAllison/data603-sp22/blob/Paper_Outline/paper/Hive_Max_Output.jpg)
![Alt text](https://github.com/NicAllison/data603-sp22/blob/Paper_Outline/paper/Hive_Min_Output.jpg)
![Alt text](https://github.com/NicAllison/data603-sp22/blob/Paper_Outline/paper/Hive_Showing_all_age.jpg)
### 5. Paragraph that explains what Pig and Pig Latin are
### 6. How to set up Pig Environment that I used
### 7. Code used to create each a table and pieces of data, then find the average, maximum, and minimum from the table as well as display all pieces of data as output
### 8. Summary of what hive and pig are and how they display the average, max, and min. 

#### References
Data Used: https://www.superprof.com/blog/top-20-artists/
Hive Docker: https://hub.docker.com/r/bde2020/hive/
Hive Docker Instructions: https://github.com/big-data-europe/docker-hive
Hive Help:https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.0/bk_data-access/content/new-feature-insert-values-update-delete.html
https://phoenixnap.com/kb/hive-create-table
https://datafibers-community.github.io/blog/2018/02/02/2018-02-02-hive-get-max-min-value-rows/
https://www.projectpro.io/questions/5760/hive-query-for-avg-of-marks
https://www.tutorialspoint.com/hive/index.htm

