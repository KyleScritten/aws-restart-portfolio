# Introduction to Amazon DynamoDB

## Lab overview

Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale. It is a fully managed database and supports both document and key-value data models. Its flexible data model and reliable performance make it a great fit for mobile, web, gaming, ad-tech, Internet of Things (IoT), and many other applications.

In this lab, I create a table in DynamoDB to store information about a music library. I query the music library and then delete the DynamoDB table.

## Task 1: Create a new table
In DynamoDB each table requires a partition key (or a primary key) that is used to partition data across DynamoDB servers. 
A table can also have a sort key. The combination of a partition key and sort key uniquely identifies each item in a DynamoDB table.

I create a new table in DynamoDB with this configuration:
* Table name: `Music`
* Partition key: `Artist` (String)
* Sort key - optional: `Song` (String)

![DynamoDB Music Table](./images/lab09-dynamoDB-music.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

## Task 2: Add data

>[!Note]
> A table is a collection of data on a particular topic. Each table contains multiple items. An item is a group of attributes that is uniquely identifiable among all of the other items. Items in DynamoDB are similar in many ways to rows in other database systems. In DynamoDB, there is no limit to the number of items you can store in a table.
> Each item consists of one or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further. For example, an item in a Music table contains attributes such as song and artist. Attributes in DynamoDB are similar columns in other database systems, but each item (row) can have different attributes (columns).
> When writing an item to a DynamoDB table, only the partition key and sort key (if used) are required. Other than these fields, the table does not require a schema. This means that it is possible to add attributes to one item that may be different than the attributes for other items.

I add 3 items into to the Music table using the button `Create item` on the Music table page. The items have the following attributes:

*First item:*
* Artist: `Pink Floyd` (partition key)
* Song: `Money` (sort key)
* Album: `The Dark Side of the Moon` (new string attribute)
* Year: `1973` (new number attribute)

![DynamoDB Music Table - Create item](./images/lab09-dynamoDB-music-create-item.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

*Second item:*
* Artist: `John Lennon` (partition key)
* Song: `Imagine` (sort key)
* Album: `Imagine` (attribute)
* Year: `1971` (attribute)
* Genre: `Soft rock` (new string attribute)

*Third item:*
* Artist: `Psy` (partition key)
* Song: `Gangnam Style` (sort key)
* Album: `Psy 6 (Six Rules), Part 1` (attribute)
* Year: `2011` (attribute)
* LengthSeconds: `219` (new number attribute)

![DynamoDB Music Table with Items](./images/lab09-dynamoDB-music-with-items.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

The possibility to add items with different attributes demonstrates the flexibility of a NoSQL database.

There are also faster ways to load data into DynamoDB, such as using AWS Command Line Interface, programmatically loading data, 
or using one of the free tools available on the internet.

## Task 3: Modify an existing item
I now notice that there is an error in my data. In this task, I modify an existing item.

1. In the DynamoDB dashboard, under **Tables**, I choose **Explore Items**.
2. I choose the **Music** button, then choose `Psy`.
3. I change the **Year** from `2011` to `2012`.
4. I choose **Save changes**.

The item is now updated.

![DynamoDB Music Table - Create item](./images/lab09-dynamoDB-music-edit-item.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

## Task 4: Query the table
There are two ways to query a DynamoDB table: *query* and *scan*.

1. A query operation finds items based on the primary key and optionally the sort key. It is fully indexed, so it runs very fast.

    * Artist (Partition key): `Psy`
    * Song (Sort key): `Gangnam Style`

![DynamoDB Music Table - Query](./images/lab09-dynamoDB-music-query.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

2. Scan for an item involves looking through every item in a table, so it is less efficient and can take significant time for larger tables.

    * Attribute name: `Year`
    * Type: `Number`
    * Value`: `1971`

*Only the song released in 1971 is displayed:*

![DynamoDB Music Table - Scan](./images/lab09-dynamoDB-music-scan.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

## Task 5: Delete the table
Delete a table, also delete all the data in the table.

![DynamoDB Music Table - Delete](./images/lab09-dynamoDB-music-delete.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

![DynamoDB Music Table - Deleting](./images/lab09-dynamoDB-music-deleting.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="1000">
</p>

## Conclusion

In this lab, I have successfully:

* Created an Amazon DynamoDB table
* Entered data into an Amazon DynamoDB table
* Queried an Amazon DynamoDB table
* Deleted an Amazon DynamoDB table
