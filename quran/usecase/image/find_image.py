from quran.utils.response import Response


class FindImage:

    def __init__(self, image_repo):
        self.image_repo = image_repo

    def by_ayah_id(self, ayah_id):
        image = self.image_repo.find_by_ayah_id(ayah_id)
        return self._image_response(image)

    def _image_response(self, image):
        response = Response()
        response.image = image
        return response