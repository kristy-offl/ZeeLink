import pyrogram

from plugins.zee5_dl import zee5_execute2
#from plugins.zee5movies import zee5_execute1


@pyrogram.Client.on_callback_query()
async def formatbuttons2(bot, update):
       
    if "|" in update.data2:
        await zee5_execute2(bot, update)
        
    elif "closeformat2" in update.data2:     
        await update.message.delete()
