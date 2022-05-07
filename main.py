from utils.gundam import Gundam
from model.gunpla_model import GunplaModel
from model.media_model import MediaModel
# from fastapi import FastAPI

# app = FastAPI()

gundam = Gundam()

gunpla_dao = gundam.get_gunpla_dao()
media_dao = gundam.get_media_dao()


# print(gunpla_dao.get_all_gunpla())
# print(gunpla_dao.get_gunpla_by_id(20))
# print(gunpla_dao.get_gunpla_by_name("hizack"))
# print(gunpla_dao.get_gunpla_by_title("Mobile Suit Gundam"))
# print(gunpla_dao.get_gunpla_by_rating_design("4.5"))
# gunpla_model = GunplaModel(gunpla_id = 54, gunpla_name = "justice gundam", title = "Mobile Suit Gundam SEED")
# gunpla_dao.add_new_gunpla(gunpla_model)

# print(media_dao.get_all_media())
# print(media_dao.get_media_by_id(1))
# print(media_dao.get_media_by_title("Mobile Suit Zeta Gundam"))
# print(media_dao.get_media_by_media_type("TV series"))
# print(media_dao.get_media_by_release_date("2017"))
# new_media = MediaModel(title_id = 100, title= "The UNKNOW",media_type = "ONA", release_date = "2055", timeline = "UC1029")
# media_dao.add_new_title(new_media)