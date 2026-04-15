Python Crypto Monitoring Project

This project calls Telegram API to get the crypto value for BTC, ETH and SOL

Is running with Python 3.12.x

Once you've created the virtual environment you have to install de dependencies that you have listed on requirements.txt

Configure .env

Run script

Take in mind you need to created your own bot for Telegram @BotFather, and when you have you API_key, configure it on your project


## Installation

git clone <url-del-repo>
cd crypto-monitor
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Configuration

Create a .env file in the root with:

TELEGRAM_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
COINGECKO_URL=https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd

## Usage

python main.py