from storages.backends.gcloud import GoogleCloudStorage

storage = GoogleCloudStorage()


class Upload:

    # @staticmethod
    def upload_image(file, filename):
        try:
            target_path = 'images/' + filename
            path = storage.save(target_path, file)
            print(f"path: {path}")
            return storage.url(path)
        except Exception as e:
            print('Failed to upload to GCS: ', e)