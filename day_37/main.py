import datetime
from pixela import Pixela

USERNAME = ""
GRAPHID = ""

pixela = Pixela(user_name=USERNAME)

pixela.create_graph(
    graph_id=GRAPHID,
    name="Daily Bread",
    unit="chapter",
    quantity_type="int",
    color="blue"
)

print(pixela.get_graph_url(GRAPHID))

quantity = input("Berapa banyak ayat yang dibaca hari ini? ")
date = datetime.datetime.now().date()
pixela.create_pixel(graph_id=GRAPHID, quantity=quantity, date=date)
