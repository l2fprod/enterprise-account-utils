# Generates a diagram for IBM Cloud accounts

[![Build Status](https://travis-ci.org/l2fprod/enterprise-account-utils.svg?branch=master)](https://travis-ci.org/l2fprod/enterprise-account-utils)

## Try it now with the Docker image

1. The Docker image has all required dependencies. Just run from a directory where you want the diagram to be generated:
   ```sh
   docker run --rm --volume $PWD:/home -it l2fprod/enterprise-account-utils
   ```
1. Once the container is running, log in your IBM Cloud account inside the container:
   ```sh
   ibmcloud login
   ```
1. Run the export script:
   ```sh
   export.sh
   ```
1. Find the diagram `enterprise.png` under the current directory.

## License

This project is licensed under the Apache License Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0).