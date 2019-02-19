# aws-mfa-gen #
Provides aws-mfa-gen command that uses AWS STS to assume role and place result into aws cli credentials file.

Motivation around this is that not all tools can handle STS authentication or MFA so this tool will place access key, secret key and session token in credentials file.


## Installation ##
The project is available as pip package, so to install it just invoke pip:

`pip install aws-mfa-gen`

## Basic usage ##
- You will need at least two aws profiles
  - source profile with correct access and secret keys
  - profile for any role that you want to assume
- Create a new profiles in ~/.aws/config file. You can find sample configuration below
- Make sure to put proper login_source_profile, login_role_arn and login_mfa_serial
- Select the above configured AWS CLI profile: `export AWS_PROFILE=dev`
- Invoke aws-mfa-gen. You will be asked for the password and MFA token (for details about MFA - see below):
```
$ aws-mfa-gen                                                                                                                                                                         <aws:blocx-tf5>
Signing in using MFA device: arn:aws:iam::123456789012:mfa/name.surname
MFA token: 123456


--------------------------------------------------------------------------------------------------------
Your are now signed in. The token will expire at 2019-02-20T00:09:50Z.
After this time, you may safely rerun this script to refresh your access key pair.
--------------------------------------------------------------------------------------------------------
```
- The script has saved credentials to ~/.aws/credentials file, under the profile section, so now you are able to run any AWS CLI command.

## Sample configuration ##
- `~/.aws/config`
```
[profile organization]
region = eu-west-1
output = json

[profile dev]
region = eu-west-1
output = json
login_source_profile = organization
login_role_arn = arn:aws:iam::098765432109:role/developer
login_mfa_serial = arn:aws:iam::123456789012:mfa/name.surname
```
- `~/.aws/credentials`
```
[organization]
aws_access_key_id = ACCESS_KEY
aws_secret_access_key = SECRET_KEY
```

## Extended session duration ##
If you AWS role supports longer session duration, you can add `login_duration_seconds = 43200`