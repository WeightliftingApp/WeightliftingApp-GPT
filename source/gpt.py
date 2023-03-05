import openai
import keys as keys

openai.api_key = keys.openai_api_key

models = openai.Model.list()

print(models)
