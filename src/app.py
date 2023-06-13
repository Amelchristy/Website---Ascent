@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        email = request.form.get('email')

        # read existing emails
        df = pd.read_excel('emails.xlsx')

        # append new email
        df = df.append({'email': email}, ignore_index=True)

        # save to excel
        df.to_excel('emails.xlsx', index=False)

        return "Subscription successful", 200
    except Exception as e:
        return str(e), 500
