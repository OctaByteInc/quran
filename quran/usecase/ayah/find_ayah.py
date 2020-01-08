class FindAyah:

    def __init__(self, ayah_repo):
        self.ayah_repo = ayah_repo

    def by_id(self, ayah_id):
        return self.ayah_repo.find_by_id(ayah_id)

    def by_number(self, ayah_number):
        return self.ayah_repo.find_by_number(ayah_number)

    def by_number_in_surah(self, number_in_surah):
        return self.ayah_repo.find_by_number_in_surah(number_in_surah)

    def by_juz(self, juz):
        return self.ayah_repo.find_by_juz(juz)

    def by_manzil(self, manzil):
        return self.ayah_repo.find_by_manzil(manzil)

    def by_ruku(self, ruku):
        return self.ayah_repo.find_by_ruku(ruku)

    def by_hizb_quarter(self, hizb_quarter):
        return self.ayah_repo.find_by_hizb_quarter(hizb_quarter)

    def by_sajda(self, sajda):
        return self.ayah_repo.find_by_sajda(sajda)