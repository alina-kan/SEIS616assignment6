import aws_cdk as core
import aws_cdk.assertions as assertions

from WebserversDev_web_server.ws_dev_stack import wsDevStack

def test_sqs_queue_created():
    app = core.App()
    stack = wsDevStack(app, "ws_dev_stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
