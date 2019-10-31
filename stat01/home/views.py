from django.shortcuts import render

# Create your views here.
from home.models import Message

import dialogflow
from google.api_core.exceptions import InvalidArgument
import os
import uuid
#------- 新增 -------#
from gtts import gTTS
from pygame import mixer
import random
#------- 新增 -------#
DIALOGFLOW_PROJECT_ID = 'django-statbot-shtmnf'
DIALOGFLOW_LANGUAGE_CODE = 'zh-TW'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/ads/桌面/SIS.DjangoWebsite/stat01/home/Django-StatBot-ae3aee62a5a1.json"
SESSION_ID = uuid.uuid1()



# Create your views here.
def home(request):
    # --- 新增 --- #
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    if 'user_input' in request.POST: ##
        text_to_be_analyzed = request.POST.get('user_input')
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            m = Message.objects.create(user_input_text=response.query_result.query_text, detected_intent = response.query_result.intent.display_name, detected_intent_confidence = response.query_result.intent_detection_confidence, chatbot_output_text = response.query_result.fulfillment_text)
            m.save()
            messages = Message.objects.order_by('timestamp')

            context = {'user_input_text':response.query_result.query_text, 'detected_intent':  response.query_result.intent.display_name, 'detected_intent_confidence': response.query_result.intent_detection_confidence,'chatbot_output_text ': response.query_result.fulfillment_text}

            m_lastone = Message.objects.last()
            print("---")
            print("Query text:", response.query_result.query_text)
            print("Detected intent:", response.query_result.intent.display_name)
            print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            print("Fulfillment text:", response.query_result.fulfillment_text)

            #------- 新增 -------#
            mytext = response.query_result.fulfillment_text
            tts = gTTS(text=mytext, lang='zh-tw', slow=False)

            rand = random.randint(0,3)
            tts.save("./static/result_{}.mp3".format(rand))
            mixer.init()
            mixer.music.load("./static/result_{}.mp3".format(rand))
            mixer.music.play()
            while mixer.music.get_busy(): # check if the file is playing
                pass
            mixer.music.load('./static/result_copy.mp3')
            
            os.remove("./static/result_{}.mp3".format(rand))
            #------- 新增 -------#

            return render(request, 'index.html', {'m_lastone': m_lastone})

        except InvalidArgument:
            raise

    # --- --- #

    return render(request, 'index.html', locals())
