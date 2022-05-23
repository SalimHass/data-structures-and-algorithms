# hashtables
we need to implement the Hashtable class, it contains the following fuicntions :
1. on initiation it should get size as argument , and it will construct a list with lenght of the size and filled with None in every entry in the list .
2. hash: this function will take a key as an arguemnt, it will convert the key using ascii codes then multipliate it with a prime number then get the mode of it to the size , this number will be the index of the key-value pair in the list.

3. set:takes a key and value as argument, will assign the key-value pair to the index of inside the hashtable list

4. get: this takes key as an argument, and will return the value of it in the hashtable list

5. contains: takes key as an argument ,and will return True if the key is presented in the list , and False if not.

6. keys: this will return a list of all the keys in the list.



## Whiteboard Process
![whiteboard](../data_structures_and_algorithms/assessts/hashtable.jpg)



## Approach & Efficiency
we created several fucniton to server the purpose of this challenge , each fucntion were created seperatly inside the class as required.

## BigO: 
time: n
space:1

## API
2. hash: this fucntion takes key as argument , it gets the ascii numer for each letter of the key, and then add them togother, the sum of the ascii number then multiplyed by a prime number, then we use the mode of the result and the size to assign it as an index of the main list we call map.

3. set:this takes key and value , this fucntion will use the hash function to get the index of the list that this key value pair should be assigned , then it should assign them to that index, if the index is already filled, then it will appened this to the list of items inside the index

4. get: this method will take the key as an argument and use the hash function to get the index in the main list. in the index it will check if the first element of every element inside the list is equal to the key given then it will return the second element  

5. contains: this method will take the key as an argument and use the hash function to get the index in the main list. in the index it will check if the first element of every element inside the list is equal to the key given then it will return true , else will return false  


6. keys: this will reaverse throught the main list and will check for the not None elements , and then it will append the first element of each element inside the elements in each index.

## pull request
