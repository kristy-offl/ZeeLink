import pyrogram

#from plugins.zee5_dl import zee5_execute
from plugins.zee5movies import zee5_execute1


@pyrogram.Client.on_callback_query()
async def formatbuttons1(bot, update):
       
    if "|" in update.data:
        await zee5_execute1(bot, update)
        
    elif "closeformat1" in update.data:     
        await update.message.delete()
