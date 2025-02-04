# 
# User Authentication API

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up environment variables in `.env`.
4. Run the application: `flask run`.

## API Documentation
### Endpoints
- Sign-up:`/signup` (POST)
- Sign-in:`/login` (POST)
- Get User Profile:`/profile/<user_id>` (GET)
- Upload File: `/upload-file` (POST)
- Get All Files: `/all-files` (GET)
- Update File Status:`/update-file-status` (PUT)
- Get User by Phone Number: `/user-by-phone` (GET)
- Download File: `/download-file/<file_id>` (GET)
- Update User Attributes: `/update-profile` (PUT)
- Chatbot with Image Integration: `/chatbot` (POST)

## Error Handling
- 400 Bad Request: Invalid input data.
- 401 Unauthorized: Missing or invalid token.
- 403 Forbidden: Insufficient permissions.
- 404 Not Found: Resource not found.
- 500 Internal Server Error: Server error.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

