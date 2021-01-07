from app import app
from app import bot_logic
from app.bot_logic import updater
from datetime import datetime


#start_time = datetime.utcnow()
bot_logic.startBot()

updater.idle()



if __name__ == "__main__":
    app.run(debug=True)

