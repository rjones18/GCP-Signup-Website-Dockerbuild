# GCP-Signup-Website-Dockerbuild

In this project, I designed a Docker build pipeline for my Python-based signup page application utilizing Google Cloud Build. By effectively integrating the GitHub repository with Google Cloud Source Repositories, I established a streamlined Continuous Deployment (CD) pipeline, while also incorporating Snyk to scan my GitHub repository for known vulnerabilities in my code.

To bolster code quality and guarantee smooth updates, I incorporated Cloud Build, which enabled automated unit testing before initiating the Docker build process. Upon the completion of the Docker build, the system automatically pushes the image to the Elastic Container Registry (ECR). This comprehensive approach ensures the reliability and security of the application, while maintaining an efficient deployment process.


## Architecture Breakdown

The Docker Build is broken down in the architecture below:

![app](https://github.com/rjones18/Images/blob/main/Screen%20Shot%202023-04-13%20at%209.56.43%20AM.png)
