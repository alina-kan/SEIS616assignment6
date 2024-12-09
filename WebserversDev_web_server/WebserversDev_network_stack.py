import os.path

from aws_cdk.aws_s3_assets import Asset as S3asset

from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
    # aws_sqs as sqs,
)

from constructs import Construct

class WebserversDevNetworkStack(Stack):

    @property
    def vpc(self):
        return self.engineering_vpc
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC. CDK by default creates and attaches internet gateway for VPC
        self.engineering_vpc = ec2.Vpc(self, "engineering_vpc", 
                            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/18"),
                            subnet_configuration=[
                                ec2.SubnetConfiguration(name="PublicSubnet01",subnet_type=ec2.SubnetType.PUBLIC),
                                ec2.SubnetConfiguration(name="PublicSubnet02",subnet_type=ec2.SubnetType.PUBLIC)
                            ]
        )
