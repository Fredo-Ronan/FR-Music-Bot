def get_response(message) -> str:
    p_message = message.lower()

    if p_message == "?help":
        return """
> ## ``Help to FR Music bot``
> ```
> ?help               ---> show the manual of how to interact with this bot
> ?play <youtube-url> ---> play music with the provided youtube url
> ?pause              ---> pause the current playing music
> ?resume             ---> resume the current playing music  
> ?stop               ---> stop the current playing music and the bot disconnect from current voice channel
> 
> NOTE : The ?stop command also can be use to only disconnect the bot from voice channel even if there is no music that currently playing
> ```
> `Enjoy` 🎶
> 
> Developed with ❤ by Fredo Ronan
> Give support to developer on [this link](https://saweria.co/fredo06)
        """
    
    if p_message.startswith("?play"):
        return '`▶ Joined voice channel and play the music from given youtube link.......🎶`'
    
    if p_message == "?pause":
        return '`⏸ Pause the current playing music.......Waiting ?resume command....`'
    
    if p_message == "?resume":
        return '`▶ Resume playing music.......🎶`'
    
    if p_message == "?stop":
        return '`🟥 Stop the music and disconnected from voice channel.......👋`'