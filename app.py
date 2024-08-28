from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Veri setini yükleyin ve modeli eğitin
df = pd.read_csv('supermarket_sales.csv')

# Ürün adlarının listesini oluştur
unique_products = df['Product'].unique()

# Ürün çifti ve rating farkı ile bir DataFrame oluştur
product_pairs = [(unique_products[i], unique_products[i + 1]) for i in range(0, len(unique_products), 2)]

data = []
for p1, p2 in product_pairs:
    rating_p1 = df[df['Product'] == p1]['Rating'].mean()
    rating_p2 = df[df['Product'] == p2]['Rating'].mean()
    if pd.isna(rating_p1) or pd.isna(rating_p2):
        continue

    rating_diff = abs(rating_p1 - rating_p2)
    label = 1 if rating_diff <= 1.1 else 0
    data.append({'Product_1': p1, 'Product_2': p2, 'Rating_Diff': rating_diff, 'Label': label})

pairs_df = pd.DataFrame(data)

X = pairs_df[['Rating_Diff']]
y = pairs_df['Label']

# NaN değerleri kaldır
X = X.dropna()
y = y[X.index]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Ana sayfa rotası
@app.route('/')
def home():
    return render_template('index.html', products=unique_products)

# Tahmin rotası
@app.route('/predict', methods=['POST'])
def predict():
    product_1 = request.form['product1']
    product_2 = request.form['product2']

    if product_1 not in unique_products or product_2 not in unique_products:
        result = "Veri bulunamadı. Lütfen geçerli ürünler girin."
    else:
        rating_diff = abs(df[df['Product'] == product_1]['Rating'].mean() - df[df['Product'] == product_2]['Rating'].mean())

        prediction = model.predict([[rating_diff]])
        if prediction == 1:
            result = f"{product_1} ve {product_2} birlikte yerleştirilebilir."
        else:
            result = f"{product_1} ve {product_2} uzakta yerleştirilmelidir."

    return render_template('index.html', result=result, products=unique_products)

if __name__ == '__main__':
    app.run(debug=True)
