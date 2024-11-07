import asyncio
from aiogram.types import BotCommand, BotCommandScopeDefault

from app.bot.bot import SubscriptionChecker
from app.bot.handlers import start_handler, payment_handler
from app.utils.logger import setup_logger

log = setup_logger(__name__)


async def main():
    bot = SubscriptionChecker().get_bot()
    log.info("Бот запущен")
    dp = SubscriptionChecker().get_dispatcher()
    log.info("Диспетчер создан")

    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Запустить бота")
        ])
    dp.include_router(start_handler.start_router)
    dp.include_router(payment_handler.payment_router)

    log.info("Роутеры добавлены")
    await bot.delete_my_commands(
        scope=BotCommandScopeDefault()
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())