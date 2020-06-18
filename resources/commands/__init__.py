from discord import message
import asyncio


async def success_and_delete(message, wait=5):
    await message.add_reaction("✅")
    await asyncio.sleep(wait)
    await message.delete()


async def error_and_delete(message, wait=5):
    await message.add_reaction("❌")
    await asyncio.sleep(wait)
    await message.delete()
    return
