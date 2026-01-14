# AWS S3
Amazon Web Services Simple Storage Service. Stores files and folders.
## Create buckets
`aws s3 mb s3://<bucket name>`
## Upload content to bucket
`aws s3 cp <local files> s3://<bucket name>`
This can also be done in the Objects tab in the bucket's management console
## Get bucket region
`aws s3api get-bucket-location --bucket <bucket name>`
## Controlling access - permissions tab
### Turn off "Block public access"
Must turn off this setting to allow public access to the bucket and its access points (custom names with associated permissions)
### Set policy in management console
Policy to allow public access to bucket contents
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::network-website-project-skyeg/*"
        }
    ]
}
```
### ACLs
Access Control Lists. Have to change object ownership from "Bucket owner enforced"
## Delete Bucket
`aws s3 rb --force s3://<bucket name>`