from application import createApp
app = createApp()

@app.route('/')
def home():
    return "Homepage"


if __name__ == '__main__':
    app.run()