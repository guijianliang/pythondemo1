from . import create_app
# from flask_uploads import UploadSet, configure_uploads, ALL



app = create_app()

# photos = UploadSet('PHOTO')
# configure_uploads(app, photos)

if __name__ == '__main__':
    # app.run(dexbug=True)
    app.run(debug=True)
    # try:
    #     http_server = WSGIServer(('', 5000), app)
    #     http_server.serve_forever()
    # except Exception as e:
    #     print(e)