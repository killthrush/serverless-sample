# serverless-sample
A sample AWS Lambda project using the Serverless Framework and Python 3.6.  This installs some basic building blocks like Lambda functions, API Gateway, and DynamoDB using the [Serverless Framework](https://serverless.com/)

# Requirements
In order to run the sample, you will need:
* An AWS account with API keys.  See [this guide](http://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) for instructions.
* The AWS CLI should be installed on your computer
* A Docker daemon running on your computer.  Install instructions are [here](https://docs.docker.com/engine/installation/#supported-platforms)
* [NPM](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/en/) installed globally
* Python 3.6 and a suitable editor for modifying/testing python code

# Installation
* Clone this repository and `cd` into this directory.  All the following commands should be run here.
* Set up a profile using the CLI tool: `aws configure`.  Enter your API keys and region.
* Run `npm install` or `yarn install` (your choice).  This will install the serverless framework itself, along with a few plugins.
* Run the following command to build the code payload for deployment: `docker run -it -v $(pwd)/src:/src lambci/lambda:build-python3.6 /bin/sh -c "cd /src;pip install -r requirements.txt --upgrade -t vendored/"`
* Run `serverless deploy aws --aws-profile <your profile name>` to deploy your code.

# Notes
* The docker trick above ensures that the python environment being deployed, including native depdendencies, is compatible with the AWS Lambda python environment.
* There are many other ways to configure AWS profiles and call serverless - the noted steps are but one way.
