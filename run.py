from flask_web_ui import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True, port=80)