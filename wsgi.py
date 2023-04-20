from blog.app import create_app

app = create_app()
app.secret_key = "super secret key"

if __name__== "__main__":

    app.run(
        host="0.0.0.0",
        debug=True
    )
