from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():

    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"]
    signals = ["BUY", "SELL", "WAIT"]

    pair = random.choice(pairs)
    signal = random.choice(signals)
    confidence = random.randint(70, 95)

    return f"""
    <html>

    <head>
        <title>MatomAITrader</title>

        <style>

            body {{
                background: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 50px;
            }}

            .card {{
                background: #1e293b;
                width: 80%;
                margin: auto;
                padding: 30px;
                border-radius: 20px;
            }}

            h1 {{
                color: #38bdf8;
            }}

            .signal {{
                font-size: 50px;
                margin: 20px;
            }}

            .confidence {{
                font-size: 30px;
                color: #22c55e;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>MATOM AI TRADER</h1>

            <h2>{pair}</h2>

            <div class="signal">
                {signal}
            </div>

            <div class="confidence">
                Confidence: {confidence}%
            </div>

        </div>

    </body>

    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
