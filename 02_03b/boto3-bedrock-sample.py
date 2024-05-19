#Imports

#Create the bedrock client

#Setting the prompt

#Model specification

#Configuring parameters to invoke the model

#Invoke the model

#Parsing and displaying the output


#Imports
import boto3
import json
#Create the bedrock client
bedrock = boto3.client('bedtock-runtime')
#Setting the prompt
prompt_data = """Command: Write me a blof about coching employees as leader.
Blog:
"""
#Model specification
modelId = "amazon.titan-text-express-v1"
accept = "application/json"
contentType = "application/json"

#Configuring parameters to invoke the model
body = json.dumps({
"inputText" : prompt_data,
"textGenerationConfig" :{
  "maxTokenCount" : 1000
}

})
#Invoke the model

response = bedrock.invoke_model(
  body = body,modelId=modelId,accept=accept,contentType=contentType
)
#Parsing and displaying the output

response_body = json.loads(response.get('body').read())
output = response_body.get('result')[0].get("outputText")
print(output)
