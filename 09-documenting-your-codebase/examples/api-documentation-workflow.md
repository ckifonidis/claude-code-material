# API Documentation Workflow Example

## Comprehensive API Documentation Generation

This example demonstrates a complete workflow for documenting REST APIs using Claude Code.

### Step 1: Analyze Existing API Structure

```bash
> find all API endpoints in the routes/ directory
> show me the structure of our REST API
> identify which endpoints lack documentation
```

### Step 2: Generate OpenAPI/Swagger Documentation

```bash
> generate OpenAPI 3.0 specification for all endpoints in /api/v1/
> add request/response schemas based on the TypeScript interfaces
> include authentication requirements for protected endpoints
```

### Step 3: Create Interactive Documentation

```bash
> create a Swagger UI configuration for our API docs
> generate Postman collection from the API endpoints
> create curl examples for each endpoint
```

### Step 4: Document Error Handling

```bash
> document all error codes returned by the API
> create an error reference guide with status codes and meanings
> add troubleshooting section for common API errors
```

### Step 5: Generate Client SDKs Documentation

```bash
> generate TypeScript client SDK documentation
> create Python client usage examples
> document webhook integration patterns
```

## Example Output: User Authentication Endpoint

```javascript
/**
 * @api {post} /api/v1/auth/login User Login
 * @apiName LoginUser
 * @apiGroup Authentication
 * @apiVersion 1.0.0
 *
 * @apiDescription Authenticates a user and returns a JWT token
 *
 * @apiParam {String} email User's email address
 * @apiParam {String} password User's password
 *
 * @apiParamExample {json} Request-Example:
 *     {
 *       "email": "user@example.com",
 *       "password": "securePassword123"
 *     }
 *
 * @apiSuccess {String} token JWT authentication token
 * @apiSuccess {Object} user User information
 * @apiSuccess {String} user.id User's unique identifier
 * @apiSuccess {String} user.email User's email address
 * @apiSuccess {String} user.name User's full name
 *
 * @apiSuccessExample {json} Success-Response:
 *     HTTP/1.1 200 OK
 *     {
 *       "token": "eyJhbGciOiJIUzI1NiIs...",
 *       "user": {
 *         "id": "123456",
 *         "email": "user@example.com",
 *         "name": "John Doe"
 *       }
 *     }
 *
 * @apiError {String} error Error message
 * @apiError {Number} code Error code
 *
 * @apiErrorExample {json} Error-Response:
 *     HTTP/1.1 401 Unauthorized
 *     {
 *       "error": "Invalid credentials",
 *       "code": 401001
 *     }
 */
```

## Automation Script

Add to `package.json`:

```json
{
  "scripts": {
    "docs:api": "claude -p 'generate complete API documentation for all endpoints'",
    "docs:api:test": "claude -p 'verify all API examples in documentation work correctly'",
    "docs:api:update": "claude -p 'update API documentation to match current implementation'"
  }
}
```

## Best Practices Applied

1. **Consistent format**: All endpoints follow the same documentation pattern
2. **Real examples**: Include actual request/response examples
3. **Error documentation**: Document all possible error scenarios
4. **Version tracking**: Include API version in documentation
5. **Authentication**: Clearly mark which endpoints require authentication
6. **Testing**: Verify documentation examples actually work