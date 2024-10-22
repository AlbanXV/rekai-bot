import time

async def user_timers(message, user_id, response, interval, recent):
    """
        A temporary function to add a limit to a message the bot can
        send to a specific user.

        It takes the current time and the time of the sent message from the user
        and sends a message if the time of the message is equal or larger than
        the interval

        Example: Interval of 10 seconds. The user sends a specific message
        to trigger this function. Let's assume the message is "Hello".
        The bot replies with "Hi" and the timer starts. The user can type "Hello"
        again but the bot will not respond till the registered timer is equal or
        above the interval timer.

        This is to avoid bot spam.

        (This function will be replaced when I implement SQL)

        args: 
            - message: str
            - user_id: int
            - response: str
            - interval: int
            - recent: dict

        returns:
            - None
        
    """
    
    current_time = time.time()

    recent_response = recent.get(user_id, 0)

    if current_time - recent_response >= interval:
        await message.channel.send(response)
        recent[user_id] = current_time