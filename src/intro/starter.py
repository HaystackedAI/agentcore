import boto3
import pprint

bedrock = boto3.client('bedrock')

pp = pprint.PrettyPrinter(depth=4)

models=bedrock.list_foundation_models()
for model in models['modelSummaries']:
    pp.pprint(model)

print(models)