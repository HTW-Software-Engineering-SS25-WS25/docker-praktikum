# Task 4

## Working with Registries

After working with Registries in the previous task, you should now be familiar with how to build and push Docker images. In this task, you will practice pushing your images to a registry and pulling them from another environment.

1. Create a Dockerfile for your own architecture (frontend or backend or both) with the following requirements:

   - The Dockerfile should be able to build your application.
   - The Dockerfile should be able to run your application.
   - The Dockerfile should expose the necessary ports for your application.

2. Build your Docker image using the Dockerfile you created in step 1.

3. Tag your Docker image with a meaningful name and version. For example, if your application is called "myapp" and the version is "1.0", you can tag it as `myapp:1.0`.

4. Push your Docker image to a public registry (e.g., Docker Hub). Make sure you have an account on the registry and are logged in.

5. Pull your Docker image from the registry to another environment (e.g., a different machine or a cloud service).
6. Run your Docker image in the new environment and verify that your application is running correctly.
