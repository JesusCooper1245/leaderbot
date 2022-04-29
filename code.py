import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="63d996552402bf981823cc73afebd998a7c15582b31450dce9d87bff88f545134c63c4af4c886bb3c13e0")
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
	vk_session.method("messages", {"user_id":id, "message":some_text, "random_id":0})



for event in longpoll.listen():
	if event.type == VkEventType.MESSEGE_NEW:
		if event.to_me:
			msg = event.text,lower()
			id = event.user_id
			if msg == "/checkinfo":
				send_some_msg(id, "Используйте /checkinfo NickName") 