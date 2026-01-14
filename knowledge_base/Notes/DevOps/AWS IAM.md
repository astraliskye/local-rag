# AWS IAM
Amazon Web Services Identity and Access Management
## Example policy
Allow everything on EC2 instances with the tag "Env:development"
Allow describe for everything EC2
Disallow creating or deleting tags for EC2
```json
{    
  "Version": "2012-10-17",    
  "Statement": [        
    {            
      "Effect": "Allow",            
      "Action": "ec2:*",            
      "Resource": "*",            
      "Condition": {                
        "StringEquals": {                    
          "ec2:ResourceTag/Env": "development"                
        }            
      }        
    },        
    {            
      "Effect": "Allow",            
      "Action": "ec2:Describe*",            
      "Resource": "*"        
    },        
    {            
      "Effect": "Deny",            
      "Action": [                
        "ec2:DeleteTags",                
        "ec2:CreateTags"            
      ],            
      "Resource": "*"        
    }    
  ] 
}
```
## Account alias
Can only have one alias for an account. Creating an alias for an account will override the previous alias. Friendly name to use to sign in rather than using the 12ish digit account id number. IAM users can use the URL `https://<account alias>.signin.aws.amazon.com/console` to login.
## Groups and users
Same shit different day. Users are things that can login. Groups are ways to organize users.
## Roles
Temporary groups users can 
## Policy simulator
Test access for users, groups, and roles without having to manually log into each and click around to test everything.