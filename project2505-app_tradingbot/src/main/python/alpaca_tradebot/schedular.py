import sys
import platform

def beep(frequency, duration):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(frequency, duration)  # frequency, duration in ms
    else:
        # ASCII BEL character; most terminals will make a beep
        sys.stdout.write('\a')
        sys.stdout.flush()





# scheduler_service.py
import logging
from typing import Callable, Any

from apscheduler.schedulers.background import BackgroundScheduler

class SchedulerService:
    """Service to manage scheduling of periodic tasks using APScheduler."""
    def __init__(self, logger: logging.Logger) -> None:
        """
        Initialize the scheduler service.

        Args:
            logger: Logger instance for logging scheduler events.
        """
        self.logger = logger
        self.scheduler = BackgroundScheduler()

    def add_job(self, func: Callable[..., Any], trigger: str, **trigger_args: Any) -> None:
        """
        Add a job to the scheduler.

        Args:
            func: The callable to execute.
            trigger: The type of trigger (e.g., 'interval', 'cron', 'date').
            **trigger_args: Arguments for the trigger (e.g., seconds=10 for interval).
        """
        self.scheduler.add_job(func, trigger, **trigger_args)
        self.logger.debug(f"Added job: {func.__name__} with trigger '{trigger}' {trigger_args}")

    def start(self) -> None:
        """Start the scheduler (jobs will begin running in background threads)."""
        self.logger.info("Starting scheduler.")
        self.scheduler.start()

    def shutdown(self, wait: bool = True) -> None:
        """
        Shutdown the scheduler.

        Args:
            wait: If True, waits until currently running jobs complete.
        """
        self.logger.info("Shutting down scheduler.")
        self.scheduler.shutdown(wait=wait)



































# utils.py
import logging
import sys
from typing import Optional

class LoggingUtility:
    """Utility class to configure and provide logger instances."""
    @staticmethod
    def configure_logging(level: int = logging.INFO, log_file: Optional[str] = None) -> logging.Logger:
        """
        Configure the root logger with console and optional file output.

        Args:
            level: Logging level (e.g., logging.INFO).
            log_file: Optional file path; if provided, logs will also be written to this file.
        
        Returns:
            Configured Logger instance.
        """
        logger = logging.getLogger("BackgroundServiceLogger")
        logger.setLevel(level)
        logger.propagate = False  # Prevent double logging if root logger is also configured elsewhere

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler (if specified)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger





















# tasks.py
import logging

from typing import Any
from .core import fetch, logic, index_logic, report, short_operation
from .orders import load_orders, cancel_all_orders_in





class TaskHandler:
    """Defines tasks/actions to be scheduled by the scheduler."""
    def __init__(self, logger: logging.Logger) -> None:
        """
        Initialize TaskHandler with a logger.

        Args:
            logger: Logger instance for logging task operations.
        """
        self.logger = logger

    def get(self, message: str = "Task1 executed!") -> None:
        """
        Example task: Log a message and emit a beep notification.

        Args:
            message: Message to log when the task is executed.
        """
        self.logger.info(f"[get]... Message: {message}")
        beep(800,200)
        # ... Implementation here ...
        # ........................................................
        fetch()
        # ........................................................
        # self.logger.info("Notification task completed.")

    def post_or_put(self, message: str = "Task2 executed!") -> None:
        """Example task: Perform cleanup of old logs or temporary data."""
        self.logger.info(f"[post]... Message: {message}")
        beep(1200,200)
        # ... Insert actual cleanup logic here ...
        # ........................................................
        if not IS_BYSTANDER and not IS_DEPRESSION: logic()
        else: fetch()
        # ........................................................
        # self.logger.info("Cleanup task completed.")


    def delete(self, message: str = "Task3 executed!") -> None:
        """Example task: Perform a system health check and report status."""
        self.logger.info(f"[delete]... Message: {message}")
        beep(1000,200)
        # ... Insert actual health check logic here ..............
        # ........................................................
        if not IS_BYSTANDER and not IS_DEPRESSION: index_logic()
        else: fetch()
        # ........................................................
        # status = "OK"  # Placeholder for real status
        # self.logger.info(f"Health check completed. Status: {status}")

    def report(self, message: str = "Tax report generated!") -> None:
        self.logger.info(f"[report]... Message: {message}")
        beep(1500, 200)
        report()
        # ........................................................
        # self.logger.info("Tax report CSVs written.")

    def shorting(self, message: str = "Short sell executed!") -> None:
        self.logger.info(f"[short]... Message: {message}")
        beep(1300, 200)
        if not IS_BYSTANDER and not IS_LONG: short_operation()
        # ........................................................
        # self.logger.info("Short sell orders placed.")

























# main.py
import time
import logging
# from scheduler_service import SchedulerService
# from tasks import TaskHandler
# from utils import LoggingUtility


# ## bystander
# IS_BYSTANDER    = True     # Set to True to disable actual trading actions for testing
# IS_LONG         = True      # Set to True to disable actual trading actions for testing

# ## v2(short)
# IS_BYSTANDER    = False
# IS_LONG         = False

## regular
IS_BYSTANDER    = False
IS_LONG         = True



def main() -> None:
    """Main entry point for the scheduling service."""
    # Configure logging
    logger = LoggingUtility.configure_logging(logging.INFO, log_file="service.log")
    logger.info("Service starting up.")

    # Create task handler and scheduler service
    task_handler = TaskHandler(logger)
    scheduler = SchedulerService(logger)





    ##########################################################################################
    # Schedule jobs (using string trigger names and trigger arguments)
    ##########################################################################################
    ### action1: get (fetch/logic)
    # Schedule asset info retrieval during trading hours (Mon-Fri, 9am-3pm)
    # at minutes 1, 16 and 46.
    scheduler.add_job(
        task_handler.get,
        trigger='cron',
        day_of_week='mon-fri',
        hour='4-19', # 4:00 AM ET (Pre-Market start) - 8:00 PM ET (Post-Market end)
        minute='1, 16, 46',
        # minute='0-59/8',  # every 8 minutes
        second=59,
        kwargs={'message': '[GET] assets info retrieved..!'}
    )
    ### action2: post_or_put
    scheduler.add_job(
        task_handler.post_or_put,
        trigger='cron',
        day_of_week='mon-fri',
        hour='4-19', # 4:00 AM ET (Pre-Market start) - 8:00 PM ET (Post-Market end)
        minute='31',
        second=59,
        kwargs={'message': '[POST/PUT] Executing trading logic.'}
    )
    ### action3: delete
    times_with_seconds = [
        {'hour': 4, 'minute': 0, 'second': 9},    # 8:00 PM ET (Post-Market end)
    ]
    for ts in times_with_seconds:
        scheduler.add_job(
            task_handler.delete,
            trigger='cron',
            day_of_week='mon-fri',
            hour=ts['hour'], minute=ts['minute'], second=ts['second'],
            kwargs={'message': '[STOCK] daily orders are made.'}
            # kwargs={'message': '[DELETE] orders are deleted for update.'}
        )

    ### action4: report (tax report generation)
    times_with_seconds = [
        {'hour': 20, 'minute': 7, 'second': 59},    # 8:00 PM ET (Post-Market end)
    ]
    for ts in times_with_seconds:
        scheduler.add_job(
            task_handler.report,
            trigger='cron',
            day_of_week='mon-fri',
            hour=ts['hour'], minute=ts['minute'], second=ts['second'],
            kwargs={'message': '[REPORT] Tax report generated at 20:05:59. (EOD)'}
        )


    ### action5: shorting (manual short sell)
    times_with_seconds = [
        {'hour': 4,     'minute': 4,    'second': 59},     # premarket start
        {'hour': 8,     'minute': 4,    'second': 59},     # premarket end

        {'hour': 11,    'minute': 25,   'second': 1 },    # market stabilize 1
        {'hour': 14,    'minute': 4,    'second': 59},    # market stabilize 2

        {'hour': 16,    'minute': 4,    'second': 59},    # postmarket stabilize
    ]
    for ts in times_with_seconds:
        scheduler.add_job(
            task_handler.shorting,
            trigger='cron',
            day_of_week='mon-fri',
            hour=ts['hour'], minute=ts['minute'], second=ts['second'],
            kwargs={'message': f"[SHORT] Firing at {ts['hour']:02d}:{ts['minute']:02d}:{ts['second']:02d}"}
        )

    ### action3: post_or_put
    # Suppose these are the times you want: 08:00:00, 09:30:00, 11:00:00, 13:00:00, 14:30:00 (daily)
    # times_with_seconds = [
    #     # pre_end = dtime(9, 29, 59)      # 9:30 AM ET (Pre-Market end)
    #     {'hour': 9, 'minute': 22, 'second': 59},    # 09:23am (opening)
    #     {'hour': 9, 'minute': 42, 'second': 59},    # 09:43am (stablize)
    #     # post_start = dtime(16, 0, 1)    # 4:00 PM ET (Post-Market start)
    #     {'hour': 15, 'minute': 52, 'second': 59},   # 03:52pm (closing)
    #     {'hour': 16, 'minute': 12, 'second': 59},   # 04:12pm (stablize)
    # ]
    # for ts in times_with_seconds:
    #     scheduler.add_job(
    #         task_handler.post_or_put,
    #         trigger='cron',
    #         day_of_week='mon-fri',
    #         hour=ts['hour'], minute=ts['minute'], second=ts['second'],
    #         kwargs={'message': f"[POST] Firing at {ts['hour']:02d}:{ts['minute']:02d}:{ts['second']:02d}"}
    #     )


    # 2. ssssssssssssssssssssssssssssssssssss

    

    # scheduler.add_job(
    #     task_handler.delete,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour=8, minute=59, second=55,               # 8:59:55am
    #     kwargs={'message': '[DELETE] orders are deleted for update.'}
    # )
    # scheduler.add_job(
    #     task_handler.delete,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour=9, minute=1, second=1,               # 8:59:55am
    #     kwargs={'message': '[DELETE] orders are deleted for update.'}
    # )
    # scheduler.add_job(
    #     task_handler.delete,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour=9, minute=3, second=1,               # 8:59:55am
    #     kwargs={'message': '[DELETE] orders are deleted for update.'}
    # )
    # scheduler.add_job(
    #     task_handler.delete,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour=9, minute=5, second=1,               # 8:59:55am
    #     kwargs={'message': '[DELETE] orders are deleted for update.'}
    # )



    ######################### EXAMPLES #########################
    # # 1. Every day at 02:30:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     hour=2, minute=30, second=0
    # )

    # # 2. Every weekday at 18:00:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour=18, minute=0, second=0
    # )

    # # 3. Every 10 minutes, any hour
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     minute='*/10',
    #     second=0
    # )

    # # 4. 1st & 15th of each month at midnight
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day='1,15',
    #     hour=0, minute=0, second=0
    # )

    # # 5. Every Saturday & Sunday at 10:00:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day_of_week='sat,sun',
    #     hour=10, minute=0, second=0
    # )

    # # 6. Every Monday at 01:15:00 and every Friday at 17:45:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day_of_week='mon',
    #     hour=1, minute=15, second=0
    # )
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day_of_week='fri',
    #     hour=17, minute=45, second=0
    # )

    # # 7. Every quarter‐hour, 08:00–17:45, weekdays only
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day_of_week='mon-fri',
    #     hour='8-17',
    #     minute='*/15',
    #     second=0
    # )

    # # 8. Every hour on Jan, Apr, Jul, Oct (month=1,4,7,10) at 00 minutes
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     month='1,4,7,10',
    #     minute=0, second=0
    # )

    # # 9. Last Friday of each month at 16:00:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     day='last fri',
    #     hour=16, minute=0, second=0
    # )

    # # 10. Once per year: January 1st at 00:00:00
    # scheduler.add_job(
    #     task_handler.some_task,
    #     trigger='cron',
    #     month=1, day=1, hour=0, minute=0, second=0
    # )











    try:
        # Start the scheduler (runs in background threads)
        scheduler.start()
        logger.info("Scheduler started. Press Ctrl+C to exit.")

        # Keep the main thread alive to allow background tasks to run
        while True:
            time.sleep(1)
            global IS_DEPRESSION 
            IS_DEPRESSION = read_check()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Termination signal received. Shutting down service.")
        scheduler.shutdown()
        logger.info("Service terminated gracefully.")









"""
Utility functions for managing a shutdown flag via a file (flag.txt).
This allows external processes, background jobs, or administrators to 
signal the running service to exit gracefully.

Functions:
----------
write_check(value: bool) -> None
    Write a boolean value ("True" or "False") into flag.txt.
    Used to request shutdown (True) or clear the shutdown request (False).

    Usage examples:
    --------------
    >>> write_check(True)   # Signal service to shut down
    >>> write_check(False)  # Reset the flag, continue running

read_check() -> None
    Read flag.txt, check if it contains "true". If so, raise SystemExit 
    to terminate the program gracefully. If the file does not exist, 
    it is ignored.

    Usage examples:
    --------------
    >>> while True:
    ...     time.sleep(1)
    ...     read_check()   # Will exit the loop if flag.txt == "True"

Typical workflow:
-----------------
1. Service runs a main loop that periodically calls `read_check()`.
2. To stop the service, another process (or user) calls `write_check(True)`.
3. On the next cycle, `read_check()` raises SystemExit, caught by the 
   main loop's exception handler, which performs cleanup and exits.
4. Optional: reset the flag with `write_check(False)` before restarting 
   the service.
"""
def write_check(value: bool) -> None:
    with open("flag.txt", "w") as f:
        f.write("True" if value else "False")

IS_DEPRESSION = False


def read_check():
    # Check the flag file
    try:
        with open("flag.txt", "r") as f:
            flag = f.read().strip().lower()
        if flag == "true": return True
        else: return False
    except FileNotFoundError:
        return False