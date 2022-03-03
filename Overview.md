
#View All Tables

- Send GET request to http://127.0.0.1:8000/ 

this will display all tables available and show number of seats they hold i.e 2, 4, 6 or 12.

![1](https://user-images.githubusercontent.com/38029772/156491301-09cbf6f5-8c7f-4bf3-8c93-a51a87cbc4e6.png)

#Book a Table

- Send POST request to http://127.0.0.1:8000/tables/< id-of-table >

this will book the table if empty and if booking time is between 5pm to 11pm

![3](https://user-images.githubusercontent.com/38029772/156491869-d50d5af5-b549-4aee-ad75-414fc8d98dd6.png)

if you try to book outside the time period it will send back this response

![2](https://user-images.githubusercontent.com/38029772/156492091-684811aa-3eb7-474a-90a7-226dae59c81b.png)

#Check-out from a Table

- Send POST request to http://127.0.0.1:8000/tables/clear/< id-of-table >

this will update table status to empty if it was perviously occupied

![4](https://user-images.githubusercontent.com/38029772/156492282-88b9250a-42e4-4194-8062-806149920196.png)

after an occupied table has been updated to empty it will be out of service for next 10 min before it can be used again

![5](https://user-images.githubusercontent.com/38029772/156492463-38918661-9e02-4b83-b700-7adf4964f448.png)
