# React Clerk App

## Overview

This is a React application set up with Docker using Docker Compose. The application is configured to use the Node.js LTS Slim image.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. **Clone the repository:**

   ```sh
   git clone https://github.com/dimipash/users_clerk
   cd react_clerk
   ```

2. **Start the application:**

   ```sh
   docker-compose up
   ```

   This command will build and start the React application using the Docker Compose configuration specified in `compose.yaml`.

## Docker Configuration

The `compose.yaml` file defines a single service for the React application:

- **Service Name:** `react_app`
- **Image:** `node:lts-slim`
- **Volume:** Maps the local `react_clerk` directory to `/app` in the container
- **Working Directory:** `/app`
- **Command:** `sh -c "echo 'hello world'"`

## Development

For development, you can modify the `compose.yaml` file to use a different command, such as starting a development server:

```yaml
command: sh -c "npm install && npm run dev"
```

