import datetime
import vk_api
import time

token = "19d3f1537efe6357737098ced1fd2614a462f7dd48897cebe335bfe911487b7c355c0535d6a047642a8dc"
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
def main():
    while True:
        time.sleep(60)
        fuck = datetime.datetime.now()
        times = fuck.strftime("%H:%M")
        times = times.replace("1","1️⃣")
        times = times.replace("2","2️⃣")
        times = times.replace("3","3️⃣")
        times = times.replace("4","4️⃣")
        times = times.replace("5","5️⃣")
        times = times.replace("6","6️⃣")
        times = times.replace("7","7️⃣")
        times = times.replace("8","8️⃣")
        times = times.replace("9","9️⃣")
        times = times.replace("0","0️⃣")
        dialog = vk.messages.getConversations(offset=0,count=0)["count"]
        onlines = len(vk.friends.getOnline())
        #dialogs = vk.messages.getConversations(offset=0,count=10)["items"][0]["conversation"]["chat_settings"]["title"]
        fuckkk = fuck.strftime("%D")
        fuckkk = fuckkk[3:-3]
        fuckkk = fuckkk.replace("1","1️⃣")
        fuckkk = fuckkk.replace("2","2️⃣")
        fuckkk = fuckkk.replace("3","3️⃣")
        fuckkk = fuckkk.replace("4","4️⃣")
        fuckkk = fuckkk.replace("5","5️⃣")
        fuckkk = fuckkk.replace("6","6️⃣")
        fuckkk = fuckkk.replace("7","7️⃣")
        fuckkk = fuckkk.replace("8","8️⃣")
        fuckkk = fuckkk.replace("9","9️⃣")
        fuckkk = fuckkk.replace("0","0️⃣")
        print(fuckkk)
        messages = vk.messages.getDialogs(count=1)["items"][0]["message"]["title"]
        print(messages)
        getLikes = vk.photos.get(album_id = "profile", rev = "1", extended = "1", count = "1")["items"][0]["likes"]["count"]
        vk.status.set(text=f'• ⌛{times}😀 |Друзей онлайн✔: {onlines} |✉ Диалогов: {dialog} |Day:{fuckkk}😊 | 🍰 Вечный Онлайн 🍰 | ❤Лайков на аве:{getLikes}')
        
main()

"""
def valera():
        while True:
            vk.status.set(text=f'03.01.21❤')
            time.sleep(60)
            vk.status.set(text=f'03.01.21❤')
"""
