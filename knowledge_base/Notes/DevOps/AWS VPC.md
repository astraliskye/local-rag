# AWS VPC
Amazon Web Services Virtual Private Cloud
A VPC exists within a region. It can be further divided into subnets.
Internet gateways allow VPCs or subnets to connect to the outside world.
## Giving a subnet internet access
1. Create internet gateway
2. Create VPC
3. Add a route to the subnet
	1. Select route table that subnet is part of
	2. Create a route where 0.0.0.0/0 is the Destination and the internet gateway is the target (automatically done in the default route table when internet gateway is attached to VPC)