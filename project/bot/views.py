from chatterbot.ext.django_chatterbot.models import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response,get_most_frequent_response
from chatterbot.filters import get_recent_repeated_responses as filter
chatbot = ChatBot('ReadingHub',
				  storage_adapter='chatterbot.storage.DjangoStorageAdapter',
				  database_uri='sqlite:///db.sqlite3',
				  preprocessors=[
					  'chatterbot.preprocessors.convert_to_ascii'
				  ],
				  logic_adapters=[
					  {
						  'import_path': 'chatterbot.logic.SpecificResponseAdapter',
						  'input_text': 'Can you show my the highest rated book list please !',
						  'output_text': 'Ok, here is a link: localhost:8000/high'
					  },
					  {
						  "import_path": "chatterbot.logic.BestMatch",
						  "statement_comparison_function": levenshtein_distance,
						  "response_selection_method": get_first_response,
					  },
				  ]
				  )
#Statement.objects.all().delete()

book = open('bot/dataset/book.txt','r').readlines()
trainer1 = ListTrainer(chatbot)
trainer2 = ChatterBotCorpusTrainer(chatbot)
#
#Train based on the english corpus
trainer1.train(book)
trainer2.train("chatterbot.corpus.english.greetings",
 			   "chatterbot.corpus.english.conversations")

@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="bot/bot.html"):

	context = {'title': 'HUB-BOT'}
	return render_to_response(template_name, context)
