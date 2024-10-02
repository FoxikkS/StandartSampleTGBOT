import asyncio
from utils.loader import start_polling

async def main():
    await start_polling()
    
if __name__ == '__main__':
       asyncio.run(main())