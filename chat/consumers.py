from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    
    #called when user wants to connect through websocket
    async def connect(self):
        await self.accept()
    
    #when user want to send data
    async def receive_json(self, data):
        if data['command'] == 'join':
            await self.channel_layer.group_add(
                data['groupname'],
                self.channel_name
            )
            print("user added")
        elif data['command'] == 'send':
            if self.scope['user'].is_authenticated:
                await self.channel_layer.group_send(
                    'publicchat',
                    {
                        'type':'chat.message', # this should be a function and . means _
                        'message':data['message'],
                        'user':str(self.scope['user'])
                    }
                )
            else:
                await self.send_json({
                    'warning':True
                })

    #when uesr is disconnected
    async def disconnect(self):
        pass

    async def chat_message(self,event):
        await self.send_json({
            'message':event['message'],
            'user':event['user']
        })