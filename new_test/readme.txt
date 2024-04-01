Upload the attached csv in a Pandas Dataframe.

1. Create a new column col5. The value in col5 should be the maximum value of col1, col2, col3 and col4 for the particular row.
2. Calculate the standard deviation for each column, col1 to col5. Store the standard deviation for each column in a dictionary. 
eg. output should be {"col1": 32.2, "col2": 23.3, ...}
3. Find out all the index numbers(row numbers) if the value in any column of the row is more than 1.5 times of the average value of the corresponding column.




#### comp_load exercise

1. Find out the datatype of all the columns from the csv with below logic.

1. If the column has alphanumeric values, it should be a string.
2. If the column has alphanumeric values and the values are non unique, it should be string-categorical.
3. If the column has decimal values, the datatype should be Decimal(x, y) where x is the maximum number of digits before the decimal and y is the maximum number of digits after the decimal in the particular column.
4. If the column has integers, the datatype should be integer.
5. If the column has date values, the datatype should be Date (DD-MMM-YYYY). You should deduce the date format from the values.


### data 2.csv
For every table id, keep the row with the highest version id and delete other rows.