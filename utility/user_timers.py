import time

async def user_timers(message, user_id, response, interval, recent):
        current_time = time.time()

        recent_response = recent.get(user_id, 0)

        if current_time - recent_response >= interval:
            await message.channel.send(response)
            recent[user_id] = current_time