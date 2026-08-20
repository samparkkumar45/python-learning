# list slicing
my_list = [0,1,2,3,4,5,6,7,8,9]
#          0,1,2,3,4,5,6,7,8,9
print(my_list[1:6]) #slicing
print (my_list[1:-2])
print(my_list[5:])
print(my_list[:-1])
print(my_list[2:-1:2]) #list[start:end:step]
print(my_list[::-1]) #it reverese the list.

#string slicing
sample_url = 'http://sampark.com'
print(sample_url)
#Reverese the url
print(sample_url[::-1])
#Get top level domain
print(sample_url[-4:])
#Print the url without the http://
print(sample_url[-11:])
#Print the url without the http:// or top level domain
print(sample_url[7:-4])