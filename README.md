## Automated Testing Engine

### Project Overview

The _Intelligent Tutoring System_ (ITS) provides automated feedback and grading suggestions for programming assignments. As the architecture and functionality of the ITS expand, there is a need to ensure that the growing code base is maintained at high quality.

Therefore, our team has developed an automated testing engine that aims to identify existing bugs in the [ITS API](https://its.comp.nus.edu.sg/docs#/). Our solution revolves around **metamorphic testing**, where we develop metamorphic relations to identify variants of successful test cases that are potentially bug-inducing in the context of the ITS.

### Project Setup

1. Ensure that you have Python and Docker installed. Otherwise, you can download it [here](https://www.python.org/downloads/) and [here](https://www.docker.com/products/docker-desktop).
2. Run `docker build . -t automated-test-engine` to build the Docker image.
3. Run `docker run -v "<current_working_directory>":/app -it --entrypoint /bin/sh automated-test-engine` to start the Docker container, and map the current working directory to the `/app` directory in the container.
4. Run `poetry install` to install the required dependencies in the docker container.
5. Run `poetry shell` to activate the virtual environment.
6. Run `pytest` to run the test cases.
7. Run `coverage run --source=its_test_engine -m pytest && coverage report` to generate a coverage report.

### High-Level Design

```mermaid
flowchart LR
	generate_program --> generate_inputs
    generate_inputs --> mutation
    mutation --> testing
```
