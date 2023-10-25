import openai
import parameter as parm
args = input("Enter your program need ")
openai.api_key = parm.OPENAI_API_KEY
response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo-0301",
   messages=[{"role": "user", "content": args }]
)
print(response['choices'][0]['message']['content'])