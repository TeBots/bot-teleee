import openai
import telepot

openai.api_key = "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"

def chatbot(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

def handle_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == 'text':
    message = msg['text']
    if message == 'exit':
      bot.sendMessage(chat_id, 'Goodbye!')
      return False
    else:
      response = chatbot(message)
      bot.sendMessage(chat_id, response)

bot = telepot.Bot("5923753911:AAH0X8lIvGikBoIs-TLYxcyIB_2KwReX7XQ")
bot.message_loop(handle_message)
print("Listening for messages...")

while True:
  time.sleep(10)
