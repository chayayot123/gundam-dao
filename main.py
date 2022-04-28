from matplotlib.pyplot import title
from utils.gundam import Gundam
from model.gunpla_model import GunplaModel
from model.media_model import MediaModel

gundam = Gundam()

print(gundam.gunpla_info().get_all_gunpla())
print(gundam.gunpla_info().get_gunpla_by_id(20))
print(gundam.gunpla_info().get_gunpla_by_name("hizack"))
print(gundam.gunpla_info().get_gunpla_by_title("Mobile Suit Gundam"))
print(gundam.gunpla_info().get_gunpla_by_rating_design("4.5"))
new_gunpla = GunplaModel(gundam_id = 54,gundam_name = "justice gundam",title = "Mobile Suit Gundam SEED")
gundam.gunpla_info().add_new_gunpla_name(new_gunpla)

print(gundam.medias().get_all_media())
print(gundam.medias().get_media_by_id(1))
print(gundam.medias().get_media_by_title("Mobile Suit Zeta Gundam"))
print(gundam.medias().get_media_by_media_type("TV series"))
print(gundam.medias().get_media_by_release_date("2017"))
new_media = MediaModel(title_id = 100, title= "The UNKNOW",media_type = "ONA", release_date = "2055", timeline = "UC1029")
gundam.medias().add_new_title(new_media)