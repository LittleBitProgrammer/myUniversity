from application import createApp
app = createApp()

@app.route('/')
def home():
    return """
    <body>
        <button> <a id='chat_button'> chat </a> </button>
        <button> <a id='api_button'> api </a> </button>
    </body>
    
    <script>
        let chat_address = window.location + '/chat';
        let api_address = window.location + '/api';        
        document.getElementById("chat_button").setAttribute("href", chat_address);
        document.getElementById("api_button").setAttribute("href", api_address);
    </script>
    """


if __name__ == '__main__':
    app.run(threaded=True, port=5000)