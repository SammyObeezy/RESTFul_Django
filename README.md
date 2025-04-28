# 🎥 Watchlist API

A RESTful API built with **Django Rest Framework (DRF)** for managing a list of movies, TV shows, streaming platforms, and user reviews.

---

## Features

- **WatchList Management**: Create, update, delete, and retrieve movies or shows.
- **Streaming Platforms**: Manage platforms like Netflix, Amazon Prime, etc.
- **User Reviews**: Authenticated users can review movies/shows.
- **Pagination, Filtering, Throttling, and Permissions**.
- **Custom Rate Limits** for creating and listing reviews.
- **Role-Based Permissions** (Admin/User).
- **Postman Collection** included for easy testing.

---

## Project Structure

```
watchlist_app/
├── api/
│   ├── permissions.py
│   ├── serializers.py
│   ├── throttling.py
│   ├── pagination.py
│   ├── views.py
│   ├── urls.py
├── models.py
├── admin.py
├── tests.py  # ✅ Contains unit tests for API endpoints
├── postman_collection.json  # ✅ Postman collection for API testing
├── urls.py
└── apps.py
```

---

## API Endpoints

| Method | Endpoint                        | Description                       | Permissions        |
| :----- | :------------------------------ | :-------------------------------- | :----------------- |
| GET    | `/watchlist/`                   | List all movies/shows             | Public             |
| POST   | `/watchlist/`                   | Create a movie/show               | Admin Only         |
| GET    | `/watchlist/<pk>/`              | Retrieve a movie/show             | Public             |
| PUT    | `/watchlist/<pk>/`              | Update a movie/show               | Admin Only         |
| DELETE | `/watchlist/<pk>/`              | Delete a movie/show               | Admin Only         |
| GET    | `/stream/`                      | List all streaming platforms      | Public             |
| POST   | `/stream/`                      | Add a new streaming platform      | Admin Only         |
| GET    | `/stream/<pk>/`                 | Retrieve a streaming platform     | Public             |
| PUT    | `/stream/<pk>/`                 | Update a streaming platform       | Admin Only         |
| DELETE | `/stream/<pk>/`                 | Delete a streaming platform       | Admin Only         |
| GET    | `/watchlist/<pk>/reviews/`      | List all reviews for a movie/show | Public             |
| POST   | `/watchlist/<pk>/reviews/`      | Add a review for a movie/show     | Authenticated      |
| GET    | `/review/<pk>/`                 | Retrieve, update, delete a review | Owner or Read-Only |
| GET    | `/reviews/?username=<username>` | Filter reviews by username        | Public             |

---

## Models

### StreamPlatform

- `name`: Platform name
- `about`: Short description
- `website`: URL

### WatchList

- `title`: Title of the movie/show
- `storyline`: Description
- `platform`: Linked platform
- `active`: Active status
- `avg_rating`: Average rating
- `number_rating`: Number of ratings
- `created`: Creation time

### Review

- `review_user`: User who reviewed
- `rating`: Integer rating (1-5)
- `description`: Review text
- `watchlist`: Related WatchList item
- `active`: Active status
- `created`: Creation time
- `update`: Last updated time

---

## Permissions

- `IsAdminOrReadOnly`: Admins can edit, others can only view.
- `IsReviewUserOrReadOnly`: Only the review owner can edit/delete.
- `IsAuthenticated`: Only logged-in users can create reviews.

## Throttling

- `ReviewCreateThrottle`: Limit review creation frequency.
- `ReviewListThrottle`: Limit listing frequency.
- `ScopedRateThrottle`: Fine-grained control on detail views.

---

## Pagination

- `WatchListPagination`
- `WatchListLOPagination`
- `WatchListCPagination`

---

## Filtering

Use query parameters:

```
GET /reviews/?username=john
GET /watchlist/1/reviews/?active=true
```

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/watchlist-api.git
```

2. **Navigate into the project**:

```bash
cd watchlist-api
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Apply migrations**:

```bash
python manage.py migrate
```

5. **Create a superuser**:

```bash
python manage.py createsuperuser
```

6. **Run the server**:

```bash
python manage.py runserver
```

7. **Import Postman Collection**:

- Open Postman
- Import `postman_collection.json` provided in the repo
- Test all endpoints easily!

---

## Testing

Run tests using:

```bash
python manage.py test
```

Tests are located in `tests.py`.

---

## Technologies Used

- Django 4.x
- Django Rest Framework
- PostgreSQL / SQLite
- django-filter

---

## Future Improvements

- JWT Authentication
- Swagger / Redoc API documentation
- Deployment on AWS/Heroku

---

## License

This project is licensed under the MIT License.

---

## Postman Collection

A ready-to-use Postman Collection (`postman_collection.json`) is included for quick API testing.
