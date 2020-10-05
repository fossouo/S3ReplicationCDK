from aws_cdk import core

from replication.s3stack import S3Stack

class replicationStack:

    def __init__(self):
        self.app = core.App()

    def build(self) -> core.App:

        setup_stack = S3Stack(
            self.app,
            "setup-stack",
            env={'region':'us-east-1'}
        )

        replication_stack = S3Stack(
            self.app,
            "replication-stack",
            env={'region':'us-west-2'}
        )

        return self.app
