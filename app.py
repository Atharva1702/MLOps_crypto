from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and data
model = joblib.load('rf_crypto_model.pkl')
df = pd.read_csv('top_crypto.csv')
features = ['Open', 'High', 'Low', 'Close', 'Volume', 'MA7', 'MA21', 'Daily_Return']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    selected_coin = None
    coins = df['Symbol'].unique()

    if request.method == 'POST':
        selected_coin = request.form.get('coin_name')
        
        # 1. Filter for the selected coin
        coin_df = df[df['Symbol'] == selected_coin].copy()
        coin_df = coin_df.sort_values('Date')

        # 2. Re-create the missing features (IMPORTANT)
        coin_df['MA7'] = coin_df['Close'].rolling(window=7).mean()
        coin_df['MA21'] = coin_df['Close'].rolling(window=21).mean()
        coin_df['Daily_returns'] = coin_df['Close'].pct_change()

        # 3. Select only the latest row and the specific features
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'MA7', 'MA21', 'Daily_returns']
        latest_data = coin_df.tail(1)[features]
        
        # 4. Make prediction (check if we have enough data for MAs)
        if not latest_data.isnull().values.any():
            pred_value = model.predict(latest_data)
            prediction = round(pred_value[0], 2)
        else:
            prediction = "Insufficient data for prediction"

    return render_template('index.html', coins=coins, prediction=prediction, selected_coin=selected_coin)

if __name__ == '__main__':
    # host='0.0.0.0' is REQUIRED for Docker to work
    app.run(debug=True, host='0.0.0.0', port=5001)