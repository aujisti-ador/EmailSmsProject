# yourapp/cron.py

import logging
from datetime import datetime
# from django.core.mail import send_mail

from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

def daily_check_birthdays():
    logger.info("===> Cron job started: checking birthdays")
    # today = datetime.now().date()
    # profiles = Profile.objects.filter(dob__day=today.day, dob__month=today.month)
    
    # if profiles:
    #     birthday_message = "Today is the birthday of:\n"
    #     for profile in profiles:
    #         birthday_message += f"- {profile.name}\n"
        
        # send_mail(
        #     'Birthdays Today',
        #     birthday_message,
        #     'from@example.com',
        #     ['to@example.com'],
        #     fail_silently=False,
        # )
    
    logger.info("===> Cron job completed: checking birthdays")
