import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "21626173"))
    API_HASH = os.environ.get("API_HASH", "195b7e1cd00d5c7519b2fc9d93b01075")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5850733039:AAEH_uTN3MCSTWwul2XNP35pL4tn3k5BoXk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBu7Es0XsMx7iUVbFlz3PNhG3tnGd6akX0wInE9vi8BvWDsvCqW6dyJ9snNjbYqxws3GWH3p7IOOqdolj5AtVUlx3dMyJqZAUb3LafOY3YWNq0w2QaHUhIZSdgU9w28uk4Wvm9vE2AFlyCz29G5c5RbJIBnbHTYARPjRPEtpA8WlFtSy8O39JdhwdyPTlffPP_pF7BLFC9rWbPhDBV45218mUWd4dpzqBQzi9KOT8O7KC_JaZcrj3g7NcuM9OetXyRXBEMz7VNRBmXRS0yf-CAkcOM7BSkbXZJ-cTRcMm27JvbMJpLv0Yfy7AAlwwSwZogUOH2L8HySV4z8Xy57AWTTgY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Daisy_MusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/612b4483b2ed270c4070a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://i.ibb.co/PGFHWDr/MUSIC-BOT.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5856189193")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
