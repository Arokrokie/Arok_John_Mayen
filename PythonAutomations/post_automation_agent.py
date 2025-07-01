import requests
import schedule
import time
import random
from datetime import datetime
import logging

# Telegram Bot API credentials
BOT_TOKEN = "8058579721:AAFc88I66qukrNM-Bce2JF5PlOx6Idw5lXQ"
CHAT_ID = "-1002852299862"

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Complete set of 20 tips for each day (Monday-Sunday)
daily_tips = {
    "Monday": [
        "Monday Motivation 1: Start your week by listing 3 key goals to accomplish",
        "Monday Motivation 2: Dress for success - your appearance affects your mindset",
        "Monday Motivation 3: Create a power playlist for focused work sessions",
        "Monday Motivation 4: Review your long-term goals to stay aligned",
        "Monday Motivation 5: Send one appreciation message to a colleague",
        "Monday Motivation 6: Block time for deep work in your calendar",
        "Monday Motivation 7: Hydrate well - keep a water bottle at your desk",
        "Monday Motivation 8: Stand up and stretch every hour",
        "Monday Motivation 9: Learn one new professional skill this week",
        "Monday Motivation 10: Clear your workspace for better focus",
        "Monday Motivation 11: Practice the 2-minute rule for small tasks",
        "Monday Motivation 12: Visualize your ideal week ahead",
        "Monday Motivation 13: Connect with a mentor or mentee",
        "Monday Motivation 14: Update your professional profiles",
        "Monday Motivation 15: Read industry news for 15 minutes",
        "Monday Motivation 16: Practice gratitude - list 3 work-related wins",
        "Monday Motivation 17: Optimize your computer workspace setup",
        "Monday Motivation 18: Prepare healthy snacks for the week",
        "Monday Motivation 19: Set phone to Do Not Disturb during focus time",
        "Monday Motivation 20: End your day by planning tomorrow's priorities",
    ],
    "Tuesday": [
        "Tuesday Tip 1: Batch similar tasks to maintain workflow momentum",
        "Tuesday Tip 2: The 90-minute work cycle boosts productivity",
        "Tuesday Tip 3: Color-code your calendar for visual organization",
        "Tuesday Tip 4: Implement the 'touch it once' rule for emails",
        "Tuesday Tip 5: Take walking meetings when possible",
        "Tuesday Tip 6: Use the Pomodoro technique for tough tasks",
        "Tuesday Tip 7: Automate one repetitive task today",
        "Tuesday Tip 8: Practice the 80/20 rule - focus on high-impact work",
        "Tuesday Tip 9: Clean up your computer files and folders",
        "Tuesday Tip 10: Learn keyboard shortcuts for your most-used programs",
        "Tuesday Tip 11: Schedule buffer time between meetings",
        "Tuesday Tip 12: Create email templates for frequent responses",
        "Tuesday Tip 13: Track your time for one day to identify waste",
        "Tuesday Tip 14: Implement a 'no-meeting' block in your schedule",
        "Tuesday Tip 15: Back up important files and documents",
        "Tuesday Tip 16: Set app limits for social media distractions",
        "Tuesday Tip 17: Organize your browser bookmarks",
        "Tuesday Tip 18: Try a new productivity app or tool",
        "Tuesday Tip 19: Practice saying no to low-priority requests",
        "Tuesday Tip 20: End your day by celebrating small wins",
    ],
    "Wednesday": [
        "Wednesday Wisdom 1: Midweek check-in - how are your weekly goals progressing?",
        "Wednesday Wisdom 2: Sometimes good enough is better than perfect",
        "Wednesday Wisdom 3: Creativity thrives under constraints",
        "Wednesday Wisdom 4: Progress compounds - small steps matter",
        "Wednesday Wisdom 5: Your network determines your net worth",
        "Wednesday Wisdom 6: Energy management trumps time management",
        "Wednesday Wisdom 7: The best apology is changed behavior",
        "Wednesday Wisdom 8: Done is better than perfect",
        "Wednesday Wisdom 9: Focus on being productive, not just busy",
        "Wednesday Wisdom 10: Comparison is the thief of joy",
        "Wednesday Wisdom 11: You can't pour from an empty cup",
        "Wednesday Wisdom 12: Habits are the compound interest of self-improvement",
        "Wednesday Wisdom 13: The obstacle is the way",
        "Wednesday Wisdom 14: Start before you're ready",
        "Wednesday Wisdom 15: Done consistently > done intensely",
        "Wednesday Wisdom 16: Your environment shapes your behavior",
        "Wednesday Wisdom 17: Motivation follows action, not vice versa",
        "Wednesday Wisdom 18: The plural of anecdote is not data",
        "Wednesday Wisdom 19: What gets measured gets managed",
        "Wednesday Wisdom 20: Rest is part of the work",
    ],
    "Thursday": [
        "Thursday Thought 1: What's one thing you can delegate today?",
        "Thursday Thought 2: How can you add 10% more value today?",
        "Thursday Thought 3: What professional relationship should you nurture?",
        "Thursday Thought 4: What skill would make you 10% more effective?",
        "Thursday Thought 5: What outdated process can you improve?",
        "Thursday Thought 6: What's worth doing poorly today? (Good enough)",
        "Thursday Thought 7: What feedback have you been avoiding?",
        "Thursday Thought 8: What can you automate or systemize?",
        "Thursday Thought 9: What's your most important task today?",
        "Thursday Thought 10: What's draining your energy unnecessarily?",
        "Thursday Thought 11: What can you eliminate to simplify your work?",
        "Thursday Thought 12: What's the next step on your big project?",
        "Thursday Thought 13: Who could benefit from your knowledge today?",
        "Thursday Thought 14: What's your biggest time waster?",
        "Thursday Thought 15: What's one professional development activity?",
        "Thursday Thought 16: What task are you procrastinating on?",
        "Thursday Thought 17: What's your most productive work environment?",
        "Thursday Thought 18: What's worth saying no to today?",
        "Thursday Thought 19: What's your energy level telling you?",
        "Thursday Thought 20: What will make tomorrow easier?",
    ],
    "Friday": [
        "Friday Fun 1: Plan something enjoyable for the weekend",
        "Friday Fun 2: Share a funny work-appropriate meme with colleagues",
        "Friday Fun 3: Listen to upbeat music while working",
        "Friday Fun 4: Wear something that makes you feel great",
        "Friday Fun 5: Try a standing or walking meeting",
        "Friday Fun 6: Decorate your workspace for the weekend vibe",
        "Friday Fun 7: Share appreciation for a coworker's contribution",
        "Friday Fun 8: Take an extra 10 minutes for lunch",
        "Friday Fun 9: Plan a virtual coffee chat with a colleague",
        "Friday Fun 10: Share an interesting article with your team",
        "Friday Fun 11: Clean your workspace for a fresh start Monday",
        "Friday Fun 12: Celebrate your weekly accomplishments",
        "Friday Fun 13: Try a new lunch spot or recipe",
        "Friday Fun 14: Organize a quick team game or activity",
        "Friday Fun 15: Share a professional win from the week",
        "Friday Fun 16: End meetings 5 minutes early when possible",
        "Friday Fun 17: Wear comfortable shoes to work",
        "Friday Fun 18: Plan your outfit for Monday today",
        "Friday Fun 19: Leave work on time today",
        "Friday Fun 20: Do a digital detox for part of the weekend",
    ],
    "Saturday": [
        "Saturday Self-Care 1: Sleep in and recharge",
        "Saturday Self-Care 2: Disconnect from work completely",
        "Saturday Self-Care 3: Spend time in nature",
        "Saturday Self-Care 4: Practice a hobby just for fun",
        "Saturday Self-Care 5: Connect with friends or family",
        "Saturday Self-Care 6: Prepare healthy meals for the week",
        "Saturday Self-Care 7: Get some physical activity you enjoy",
        "Saturday Self-Care 8: Read something unrelated to work",
        "Saturday Self-Care 9: Try a new restaurant or cuisine",
        "Saturday Self-Care 10: Do a digital detox for a few hours",
        "Saturday Self-Care 11: Visit a museum or cultural site",
        "Saturday Self-Care 12: Take a long bath or relaxing shower",
        "Saturday Self-Care 13: Listen to your favorite music",
        "Saturday Self-Care 14: Practice mindfulness or meditation",
        "Saturday Self-Care 15: Watch a movie or show you love",
        "Saturday Self-Care 16: Declutter one small space",
        "Saturday Self-Care 17: Write in a journal",
        "Saturday Self-Care 18: Do something creative",
        "Saturday Self-Care 19: Help someone without expectation",
        "Saturday Self-Care 20: Plan something fun for next week",
    ],
    "Sunday": [
        "Sunday Prep 1: Review your upcoming week's schedule",
        "Sunday Prep 2: Plan and prepare your outfits for the week",
        "Sunday Prep 3: Grocery shop and meal prep",
        "Sunday Prep 4: Set your top 3 priorities for the week",
        "Sunday Prep 5: Charge all your devices",
        "Sunday Prep 6: Clean and organize your workspace",
        "Sunday Prep 7: Review your personal and professional goals",
        "Sunday Prep 8: Schedule your workouts for the week",
        "Sunday Prep 9: Plan your morning routines",
        "Sunday Prep 10: Set intentions, not just to-do lists",
        "Sunday Prep 11: Reflect on last week's successes",
        "Sunday Prep 12: Practice gratitude for the week ahead",
        "Sunday Prep 13: Prepare your lunch for Monday",
        "Sunday Prep 14: Wind down early for better sleep",
        "Sunday Prep 15: Visualize a successful week",
        "Sunday Prep 16: Connect with loved ones",
        "Sunday Prep 17: Read something inspirational",
        "Sunday Prep 18: Prepare your work bag and essentials",
        "Sunday Prep 19: Do something creative or fun",
        "Sunday Prep 20: Get to bed early for a fresh start",
    ],
}

# Updated media library with working URLs
media_library = {
    "images": [
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&auto=format",  # Working image
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&auto=format",  # Working image
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&auto=format",  # Working image
    ],
    "videos": [
        "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",  # Sample video
        "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_2mb.mp4",  # Sample video
    ],
}


def get_day_name():
    """Get current day name"""
    return datetime.now().strftime("%A")


def get_random_tip():
    """Get random tip for current day"""
    day = get_day_name()
    return random.choice(daily_tips.get(day, ["Daily inspiration!"]))


def send_telegram_message(text):
    """Send text message with improved error handling"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"✅ Message sent: {text[:50]}...")  # Log first 50 chars
        return True
    except Exception as e:
        logger.error(f"❌ Message failed: {str(e)}")
        return False


def send_telegram_media(media_type, media_url, caption=""):
    """Generic function to send media"""
    endpoint = f"send{media_type.capitalize()}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{endpoint}"

    # For photos, we can use the URL directly
    if media_type == "photo":
        payload = {
            "chat_id": CHAT_ID,
            "photo": media_url,
            "caption": caption,
            "parse_mode": "HTML",
        }
    # For videos, we need to ensure it's a direct video file
    elif media_type == "video":
        payload = {
            "chat_id": CHAT_ID,
            "video": media_url,
            "caption": caption,
            "parse_mode": "HTML",
        }

    try:
        response = requests.post(url, data=payload, timeout=15)
        response.raise_for_status()
        logger.info(
            f"✅ {media_type.capitalize()} sent with caption: {caption[:50]}..."
        )
        return True
    except Exception as e:
        logger.error(f"❌ {media_type.capitalize()} failed: {str(e)}")
        return False


def post_content():
    """Post content with 70% text, 20% image, 10% video probability"""
    content_type = random.choices(
        ["text", "image", "video"], weights=[70, 20, 10], k=1
    )[0]

    tip = get_random_tip()

    if content_type == "text":
        send_telegram_message(tip)
    elif content_type == "image" and media_library["images"]:
        media = random.choice(media_library["images"])
        send_telegram_media("photo", media, tip)
    elif content_type == "video" and media_library["videos"]:
        media = random.choice(media_library["videos"])
        send_telegram_media("video", media, tip)


# Schedule every 5 minutes, 24 hours a day
for hour in range(0, 24):  # All 24 hours
    for minute in range(0, 60, 5):  # Every 5 minutes
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(post_content)

if __name__ == "__main__":
    logger.info("🚀 Starting Daily Tips Bot (20 tips/day every 5 mins from 8AM-10PM)")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
