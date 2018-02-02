"""
Interprets incoming messages, passes them to an inner handler, gets the response
and transforms it into an outgoing message, returned by Lambda.
"""
import os
import sys

# if the message adapter zip file has been included, put it in the path
# it'll be used instead of the version from the requirements file
if os.path.isfile('cumulus-message-adapter.zip'):
    sys.path.insert(0, 'cumulus-message-adapter.zip')

from message_adapter.message_adapter import message_adapter

class WorkflowError(Exception):
    pass

def run_cumulus_task(task_function, cumulus_message, context):
    """
    Interprets incoming messages, passes them to an inner handler, gets the response
    and transforms it into an outgoing message, returned by Lambda.

    Arguments:
        task_function -- the function containing the business logic of the cumulus task
        cumulus_message -- either a full Cumulus Message or a Cumulus Remote Message
        context -- an AWS Lambda context dict
    """

    message_adapter_disabled = os.environ.get('CUMULUS_MESSAGE_ADAPTER_DISABLED')

    if message_adapter_disabled is True:
        try:
            return task_function(cumulus_message, context)
        except Exception as exception:
            cumulus_message['payload'] = None
            cumulus_message['exception'] = 'WorkflowError'
            return cumulus_message

    adapter = message_adapter()
    full_event = adapter.loadRemoteEvent(cumulus_message)
    nested_event = adapter.loadNestedEvent(full_event, vars(context))
    message_config = nested_event.get('messageConfig', {})

    try:
        return task_function(cumulus_message, context)
    except Exception as exception:
        cumulus_message['payload'] = None
        cumulus_message['exception'] = 'WorkflowError'
        return cumulus_message

    return adapter.createNextEvent(task_response, full_event, message_config)
