# Vue.js User Management Frontend

This frontend application provides a web interface for a user management system, built with Vue 3 and TypeScript. It communicates with a FastAPI backend to perform CRUD operations on user data.

## Technologies

- **Vue 3**: Progressive JavaScript framework
- **TypeScript**: Type-safe JavaScript
- **Vite**: Next-generation frontend build tool
- **Tailwind CSS**: Utility-first CSS framework
- **ESLint & Prettier**: Code quality and formatting
- **Docker**: Containerization

## Features

The frontend application provides user interface components for:

- Listing all users
- Creating new users
- Retrieving user details by ID
- Updating existing user information
- Deleting users

## Project Setup

### Prerequisites

- Node.js (>= 18)
- pnpm

### Installation

```bash
# Install dependencies
pnpm install
```

### Development

```bash
# Start development server
pnpm dev
```

The development server will run on http://localhost:5173 by default.

### Build for Production

```bash
# Build for production
pnpm build
```

### Type Checking

```bash
# Run type checking
pnpm type-check
```

### Linting

```bash
# Lint the codebase
pnpm lint
```

### Formatting

```bash
# Format the codebase
pnpm format
```

## Docker Integration

The frontend is containerized using Docker with a multi-stage build approach:

1. **Build stage**: Uses Node.js to compile and build the Vue application
2. **Production stage**: Uses Nginx to serve the static files

The Docker configuration automatically proxies API requests to the backend service.

### Environment Variables

- `VITE_API_URL`: URL path for API requests (default: `/api/`)

## Project Structure

```
vuejs/
├── public/            # Static assets
├── src/
│   ├── assets/        # Asset files (CSS, images)
│   ├── components/    # Vue components
│   │   ├── TheCreateUser.vue    # Create user form
│   │   ├── TheDeleteUser.vue    # Delete user component
│   │   ├── TheGetUserById.vue   # User details by ID
│   │   ├── TheListUsers.vue     # List all users
│   │   └── ThePutUser.vue       # Update user component
│   ├── lib/           # Utility functions
│   ├── types/         # TypeScript type definitions
│   ├── App.vue        # Root Vue component
│   └── main.ts        # Application entry point
├── index.html         # HTML entry point
├── vite.config.ts     # Vite configuration
├── tsconfig.json      # TypeScript configuration
├── .eslintrc.js       # ESLint configuration
└── 1_base_image.Dockerfile  # Docker configuration
```

## API Integration

The frontend communicates with the backend API to perform CRUD operations. The API base URL is configured through the `VITE_API_URL` environment variable, which is set during the Docker build process.