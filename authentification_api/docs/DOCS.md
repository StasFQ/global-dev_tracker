### **1. CreateUserAPIView**

```http
POST /api/authentification/
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description       |
| -------- | ---- |----------|-----------------|-------------------|
| username   | str  | Yes      | -               |       |
| password     | str  | Yes      | -               |       |
| first_name     | str  | Yes      | -               |       |
| email     | str  | Yes      | -               |       |


**Example response:**

```json
{
    "username": "stas11",
    "email": "stas@example.com",
    "first_name": "first_name",
    "last_name": ""
}
```