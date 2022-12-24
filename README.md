# AWS CloudWatch Log Group Cleaner

Deletes AWS CloudWatch Log Groups to keep test accounts tidy.

## Description

This tool allows you to delete AWS CloudWatch Log Groups from test AWS accounts, which have not previously been created via Infrastructure as Code.
For example, test Lambda function executions create their own CloudWatch Log Groups, which do not get deleted when you destroy the Lambda function resources.
This script can tidy up unused Log Groups to keep your AWS test account tidy and prevent unnecessary cost expenditure.

The tool will search for AWS lambda-specific Log Groups and prompt you to delete the log group before making any destructive changes.

## Getting Started

### Dependencies

* Python 3.9+
* Boto3
* Pipenv
* MyPy

### Installing

```bash
python3 -m pip install pipenv
pipenv install
````

### Executing the program

* Activate an AWS CLI profile or configure your AWS CLI with Access Keys
* Ensure an AWS region is set on your CLI or in your AWS CLI profile
* Run the script with Pipenv

#### CLI Profile

```bash
export AWS_PROFILE=my-cli-profile
pipenv run python3 main.py
```

#### Access Keys

```bash
aws configure
pipenv run python3 main.py
```

## Authors

Luke Anderson  
[@f0xtek](https://twitter.com/f0xtek)

## License

This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.
