from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URIAction, PostbackTemplateAction, ConfirmTemplate, QuickReply, QuickReplyButton, ImageCarouselTemplate, ImageCarouselColumn


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Self-introduction
self_introduction1 = "My name is Lin Yu Chen. I’m a third grade student from National Taiwan University and the department of Information Management."
self_introduction2 = "I’m a person full of curiosity and enjoy learning new things. I have participated in several projects, such as web programming, machine learning and text-mining related. I enjoy teamworks since I can always learn new things from different people, like their insights or attitude toward difficulties."
self_introduction3 = "To know more about the works I have done, check the resume or click “Experiences” to know more."
# Contact me
phone = "0988-493-117"
mail1 = "alice95058@gmail.com"
mail2 = "b07705047@nut.edu.tw"
line = "alicelin030"
# More questions
strength="I’m an extremely communicative and organized person, since I have participated in several activities and servered as a cadre. The preparing processes are always full of communications and negotiations. Not only with my team members, but also the supervisors or external sponsors and firms. These experiences enable me to organize the operations and keep track of the progress properly. I believe all these abilities will definitely make me work competently in any team."
weakness="For what I think is important, I usually put a lot of attention to it, which sometimes leads to unnecessary anxiety and affects my performance ultimately. To overcome this shortcoming, I usually make a preparing plan for myself after measuring my ability. As long as I accomplish it, I will tell myself that I am well prepared and should have confidence in performing well. This helps me to release some stress and nervousness, and sometimes get a better result."
motivation="I have participated the Meetup of Developers activity of LINE and I was really interested in the techniques and works that some teams are doing. For example, there’s a team working on uplifting modeling to find pursuable users. I was attracted by those works combining marketing and developments since I think I can find a sense of accomplishment if I help providing better user experience. And I belief I can contribute to the team based on both business knowledge and technical skills I have learned from my department."
expectation="As I mentioned in my motivation, I expect to contribute myself to the team based on both business knowledge and technical skills I have learned from my department. Also, I’m looking forward to work with excellent managers and teammates. I will definitely grasp any opportunities to learn new things and broaden my horizons. Hope to grow along with the members and the company."
# Experiences
DL1="Title: Name and Ethnicity/Gender Prediction Deep Learning Model \n\nTools: Python(tensorflow, keras) \n\nTime: Mar, 2021 - April, 2021"
DL2="-Using ninety thousand pieces of Olympian data from Kaggle and predict each Olympian’s ethnicity/gender by his/her name.\n-My part is mainly on processing word embedding and LSTM model building.\n-Finally our accuracy reached 0.92 with CNN model."
frontend1="Title: Elite Camp 20th Anniversary Website\n\nTools: HTML, CSS \n\nTime: Jan, 2021 - Mar, 2021"
frontend2="-According to dean’s requirements, we customize the contents of the website.\n-Here's the website:http://elitecamp.management.ntu.edu.tw/2021/index.html"
backend1="Title: Managment System for IM Badminton Team \n\nTools: Django, React\n\nTime: April, 2020 - Now"
backend2="-We build up database by Django and set up website by React.\n-The functions are based on users needs.\n-I was responsible for works on backend."



 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                message = event.message.text
                print(message)
                if message == "Self-introduction":

                    line_bot_api.reply_message( 
                    event.reply_token,
                    [TextSendMessage(text=self_introduction1), 
                    TextSendMessage(text=self_introduction2), 
                    TextSendMessage(text=self_introduction3)])

                elif message == "Experiences":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    [TemplateSendMessage(
                        alt_text='ImageCarousel template',
                        template=ImageCarouselTemplate(
                            columns=[
                                ImageCarouselColumn(
                                    image_url='https://home.sophos.com/en-us/medialibrary/Microsites/Home/SecurityCenter/ai-article-pic8.jpg',
                                    action=MessageTemplateAction(
                                        label='DeepLearning',
                                        text='Deep Learning'
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url='https://miro.medium.com/max/820/1*Y4Td-XMRtuFAW_8CpO7KyA.png',
                                    action=MessageTemplateAction(
                                        label='Frontend',
                                        text='Frontend'
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url='https://www.elitewebsiteservices.com/img/backend.png',
                                    action=MessageTemplateAction(
                                        label='Backend',
                                        text='Backend'
                                    )
                                )
                            ]
                        )
                    )])

                elif message == "Deep Learning":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    [TextSendMessage(text=DL1), TextSendMessage(text=DL2)])

                elif message == "Frontend":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    [TextSendMessage(text=frontend1), TextSendMessage(text=frontend2)])

                elif message == "Backend":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    [TextSendMessage(text=backend1), TextSendMessage(text=backend2)])   


                elif message == "Links":

                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://ps.w.org/easy-affiliate-links/assets/icon-256x256.png?rev=2038635',
                                title='My links',
                                text='Please choose the link to visit~',
                                actions=[
                                    URIAction(
                                        label='Github',
                                        uri="https://github.com/yuchen3890",
                                    ),
                                    URIAction(
                                        label='Facebook',
                                        uri="https://www.facebook.com/profile.php?id=100008316302560",
                                    ),
                                ]
                            )
                        )
                    )


                    

                elif message == "More Questions":
            
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://www.apti.com.hk/wp-content/uploads/2016/12/wrong_question_header.jpg',
                                title='More questions',
                                text='Please choose one to know more~',
                                actions=[
                                    MessageTemplateAction(
                                        label='Strength',
                                        text='Strength',
                                    ),
                                    MessageTemplateAction(
                                        label='Weakness',
                                        text='Weakness',
                                    ),
                                    MessageTemplateAction(
                                        label='Motivation',
                                        text='Motivation',
                                    ),
                                    MessageTemplateAction(
                                        label='Expectation',
                                        text='Expectation',
                                    ),
                                ]
                            )
                        )
                    )
                
                elif message == "Strength":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=strength))

                elif message == "Weakness":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=weakness))

                elif message == "Motivation":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=motivation))
                
                elif message == "Expectation":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=expectation))



                elif message == "Contact me":
    
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(
                            text='Which way do you want?',
                            quick_reply=QuickReply(items=[
                            QuickReplyButton(
                                action=
                                    MessageTemplateAction(
                                        label="Phone", 
                                        text="Phone",
                                    )
                                ),
                            QuickReplyButton(
                                action=
                                    MessageTemplateAction(
                                        label="Email", 
                                        text="Email",
                                    )
                                ),
                            QuickReplyButton(
                                action=
                                    MessageTemplateAction(
                                        label="LINE", 
                                        text="LINE",
                                    )
                                ),
                            ]))
                    )

                elif message == "Phone":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=f"This is my phone number: {phone}"))

                elif message == "Email":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=f"You can contact me with either {mail1} or {mail2}"))

                elif message == "LINE":
                    line_bot_api.reply_message( 
                    event.reply_token,
                    TextSendMessage(text=f"This is my LINE ID: {line}"))
                    
                # doesn't match any request above
                else:
                    line_bot_api.reply_message(  
                    event.reply_token,
                    TextSendMessage(text="To know more about me, please view the menu below~")
                    )
                
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()