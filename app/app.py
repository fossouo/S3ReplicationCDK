#!/usr/bin/env python3

from aws_cdk import core

from replication.replicationstack import replicationStack


# app = core.App()
# AppStack(app, "app")

# app.synth()

def main():
    app_stack = replicationStack()

    app = app_stack.build()
    app.synth()

main()
