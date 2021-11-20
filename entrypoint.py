from app import create_app


app = create_app()
app.run(debug=False, port = 3000)