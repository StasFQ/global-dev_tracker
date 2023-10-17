### **1. BookCreateView**

```http
POST /api/posts/
```

- Authorization: Access token

**Params:**

| Name     | Type     | Required | Values(default) | Description  |
| -------- |----------|----------|-----------------|--------------|
| title   | str      | Yes      | -               | Head of book |
| author     | int      | Yes      | -               |  |
| year_published     | int      | Yes      | -               |  |
| short_description     | str      | Yes      | -               |  |
| full_description     | str      | Yes      | -               |  |
| last_read_date     | datetime | Yes      | -               |  |


**Example response:**

**Example response:**

```json
{
    "id": 1,
    "title": "The Great Gatsby",
    "year_published": 1925,
    "short_description": "A novel depicting the lavish and reckless lifestyle of the wealthy elite in the 1920s.",
    "full_description": "The Great Gatsby is a novel by F. Scott Fitzgerald that depicts the lavish and reckless lifestyle of the wealthy elite in the 1920s. It is widely regarded as one of the greatest American novels of the 20th century.",
    "last_read_date": "2023-10-16",
    "author": 1
}
```

### **2. BookDetailView**

```http
GET /api/book_detail/<int:id>
```

- Authorization: Access token

**Params:**

| Name | Type | Required | Values(default) | Description    |
|------|------|----------|-----------------|----------------|
| id   | int  | Yes      | -               | id of the book |


    

**Example response:**
```json
{
    "id": 1,
    "title": "The Great Gatsby",
    "year_published": 1925,
    "short_description": "A novel depicting the lavish and reckless lifestyle of the wealthy elite in the 1920s.",
    "full_description": "The Great Gatsby is a novel by F. Scott Fitzgerald that depicts the lavish and reckless lifestyle of the wealthy elite in the 1920s. It is widely regarded as one of the greatest American novels of the 20th century.",
    "last_read_date": "2023-10-16",
    "author": 1
}
```


### **3. BookListView**

```http
GET /api/book_detail_list
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description       |
| -------- | ---- |----------|-----------------|-------------------|


**Example response:**

```json
[
    {
        "title": "The Great Gatsby",
        "author": 1,
        "year_published": 1925,
        "short_description": "A novel depicting the lavish and reckless lifestyle of the wealthy elite in the 1920s."
    }
]
```

### **4. StartReadingSession**

```http
POST /api/start-reading/
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description |
| -------- |------|----------|-----------------|-------------|
| user   | int  | Yes      | -               | user id     |
| book_id     | int  | Yes      | -               | book_id     |



**Example response:**
```json
{
    "user": 1,
    "book": 1,
    "start_time": "2023-10-17T13:05:49.963951Z",
    "end_time": null
}
```


### **5. EndReadingSession**

```http
PUT /api/post/<int:post_id>/dislike/analytics
```

- Authorization: Access token

**Params:**

| Name | Type | Required | Values(default) | Description |
|------|------|----------|-----------------|-------------|
| user | int  | Yes      | -               | user_id     |
| pk    | int  | Yes      | -               | session id  |



**Example response:**
```json
{
    "user": 1,
    "book": 1,
    "start_time": "2023-10-17T13:05:49.963951Z",
    "end_time": "2023-10-17T13:08:36.697524Z"
}
```


### **6. ReadingStatistics**

```http
GET /api/reading-statistics/
```

- Authorization: Access token

**Params:**

| Name | Type | Required | Values(default) | Description |
|------|------|----------|-----------------|-------------|




**Example response:**
```json
{
    "total_reading_time_per_book": [],
    "total_reading_time_user": {
        "total_time": null
    }
}
```
