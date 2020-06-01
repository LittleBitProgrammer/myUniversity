from application import createApp
app = createApp()

@app.route('/')
def home():
    return """
    <head>
        <title>my-university</title>
        <link rel="stylesheet" 
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" 
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" 
          crossorigin="anonymous">
    </head>
    <body>
        
        <div class="container">
            <h3 class="text-center">My-University flask application</h3>
            <div class="d-flex justify-content-center mt-4">
                <button class="btn btn-primary btn-lg mr-3"> <a class="text-white" id='chat_button'> Go to chat </a> </button>
                <button class="btn btn-primary btn-lg"> <a class="text-white" id='api_button'> Go to API </a> </button>
            </div>
        </div>
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