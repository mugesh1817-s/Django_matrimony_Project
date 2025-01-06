# from django.utils import timezone
# from datetime import timedelta
# from .models import Member  # Adjust if needed to match your model name and app structure

# def mark_users_inactive():
#     # Define threshold date for inactivity
#     threshold_date = timezone.now() - timedelta(days=15)

#     # Find users who haven't logged in in 15+ days and have an active status (status=1)
#     inactive_users = Member.objects.filter(last_login_lt=threshold_date, status=1)

#     # Update these users to inactive (status=2)
#     inactive_users.update(status=2)

#     # Optional: Log or print details for confirmation
#     for user in inactive_users:
#         print(f"Marked as inactive: {member.email}")