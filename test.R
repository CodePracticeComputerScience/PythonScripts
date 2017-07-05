12 - 64

a <- 2
a

assign("kp",45)
kp

name = "kp"
nchar(name)
nchar("name")

todaydate <- as.Date("2014-04-23")
date <- ("2014-04-23")
class(todaydate)
class(date)
nchar(todaydate)
# CASE SENSITIVE FUNCTION CAMEL CASE

todaydate <- as.Date("20140423")
date <- ("2014-04-23")
class(todaydate)
class(date)
nchar(todaydate)
nchar(date)

# ToDo : for dates nchar is 5 ??

# logical operators

a == a
5 == 7
6 == 6
"michel" == "michal"

#vectors

a <- c(1,2,3,4,5)
a * 2
b <- c("k","m")
b  

a ^ 2
sqrt(a)
a + 4

nchar(a)
length(a)

var <- 1:10
var

var1 <- 20:29
var + var1

length(var)
length(var1)

# getting specific items from a vector

a <- 1:5
b <- 1:3
a
b
a + b


a <- 1:6
b <- 1:3
a
b
a + b

a <- 1:9
b <- 1:3
a
b
a + b


a <- 1:10
a < 5
any(a < 5)
all(a < 5)

a[1]
a[1:5]

# Data Frame

id <- 1:15
age <- 20:34
name <- c("kp","hm","nb","kb","pk","kp","hm","nb","kb","pk","kp","hm","nb","kb","pk")

length(id) 
length(age) 
length(name)

x <-  data.frame(id,age,name)
x
nrow(x)
ncol(x)
dim(x) # no of rows and columns

names(x)[2] # second number column name in x 

head(x)

tail(x)

x[2]  # all from second column
x[2,3]  # second value from third column

x[2,1:3]
x[1:3,3]
x[ ,3]
x[3, ]

class(x["age"])
class(x[,"age"])
x["age"]
x[,"age"]

#lists

kplist <- list(2, "puri", c(1:5),"fish",x)
names(kplist) <- c("favnum","favfood","favvector","goodfood","favdata")
kplist[["favfood"]]
kplist[["favvector"]][3]
kplist[["favdata"]][,1]
kplist[["favdata"]]$name

kplist[["sisname"]] <- "soni"
kplist
length(kplist)

#matrix datatype should be same for whole matrix not like list that any datatype can be part of list

one <- matrix(1:100,nrow = 10)
one

two <- matrix(51:60,nrow = 2)
three <- matrix(61:70,nrow = 2)

two
three
dim(two)
dim(three)

two * three
two + three

# read data from csv file

getwd()  #make csv file in same working directory


csv <- read.csv("brUsers.csv",TRUE,",")  #true is for file with columnnames, , is for comma separator
class(csv)

head(csv)

csv1 <- read.csv("http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv",TRUE,",")
head(csv1)
dim(csv1)

# how to install packages

# what is packages already written code just we have to use it just install and use it

# items <- readHTMLTable("https://www.w3schools.com/html/html_tables.asp",which = 1)
# items  <- readHTMLTable()
# 
# zz = readHTMLTable("http://www.inflationdata.com/Inflation/Consumer_Price_Index/HistoricalCPI.aspx")
# 
# installed.packages()
# 
# install.packages('xml2')

# theurl <- "http://en.wikipedia.org/wiki/Brazil_national_football_team"
# webpage <- getURL(theurl)


# library(XML)
# library(RCurl)
# library(rlist)
# theurl <- getURL("https://en.wikipedia.org/wiki/Brazil_national_football_team",.opts = list(ssl.verifypeer = FALSE) )
# tables <- readHTMLTable(theurl)
# tables <- list.clean(tables, fun = is.null, recursive = FALSE)
# n.rows <- unlist(lapply(tables, function(t) dim(t)[1]))




#charts and graphics

bData <- read.csv("brUsers.csv",TRUE,",")
head(bData)

#histogram

hist(bData$age,main = "Ages of Users",ylab = "Users",xlab = "Ages")

#scatterplot

plot(bData$age,bData$income,ylab = "Income",xlab = "Age")

#boxplot

boxplot(bData$age)


#ggplot2

install.packages("ggplot2")

library(ggplot2)
head(diamonds)

#scatterplot with color

qplot(diamonds$carat,diamonds$price,diamonds)
qplot(diamonds$carat,diamonds$price,diamonds,color = diamonds$clarity)

