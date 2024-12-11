import aws_cdk as core
import aws_cdk.assertions as assertions

from WebserversDev_web_server.wsDev_web_server_stack import WebserversDevWebServerStack

def test_sqs_queue_created():
    app = core.App()
    stack = WebserversDevWebServerStack(app, "WebserversDev-web-server")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
