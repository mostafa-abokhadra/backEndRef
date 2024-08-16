### pagination (paging)الترقيم او تقسيم الصفحات
**Pagination is the process of displaying the data on multiple pages rather than showing them on a single page. You usually do pagination when there is a database with numerous records. Dividing those records increases the readability of the data. It can retrieve this data as per the user's requests**
1. How to paginate a dataset with simple page and page_size parameters
2. How to paginate a dataset with hypermedia metadata
3. How to paginate in a deletion-resilient manner

**Most endpoints that returns a list of entities will need to have some sort of pagination.**

#### offset pagination
**This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.**
**Limit/Offset Paging would look like GET /items?limit=20&offset=100. This query would return the 20 rows starting with the 100th row.**

#### Example
(Assume the query is ordered by created date descending)\
Client makes request for most recent items: GET /items?limit=20\
On scroll/next page, client makes second request GET /items?limit=20&offset=20\
On scroll/next page, client makes third request GET /items?limit=20&offset=40\
As a SQL statement, the third request would look like:
```
SELECT
    *
FROM
    Items
ORDER BY Id
LIMIT 20
OFFSET 40;
```
#### Ref
https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination