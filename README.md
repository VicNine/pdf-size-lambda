# pdf-size-lambda
Repo for a lambda function that returns the size for a pdf file and stores the file in s3

CICD using aws codepipeline, push to dev branch will trigger build and update to lambda

Env `BUCKET_NAME` was created when cloudformation stacks was created

if you need packages that lambda does not provide, please rename the `buildspec-3rd-packages.yml` to `buildspec.yml`