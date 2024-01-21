import sqlalchemy
from sqlalchemy import orm
Base = orm.declarative_base()

class Clients(Base):
    __tablename__ = "clients"
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))
    client_orders = sqlalchemy.orm.relationship("Orders", back_populates="order_client")
    def __init__(self, name):
        self.name = name


class Orders(Base):
    __tablename__ = "orders"
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer)
    name1 = sqlalchemy.Column(sqlalchemy.String(20))
    client_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("client.id"))
    order_client = sqlalchemy.orm.relationship("Clients", back_populates="client_orders")
    def __init__(self, name1, cost, client_id):
        self.name1 = name1
        self. cost = cost
        self.client_id = client_id

connection_string = "sqlite:///C:\\Users\\Admin\\PycharmProjects\\pythonProject\\DZ_16_Polonsky"
engine = sqlalchemy.create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

Igor = Clients("Igor")
Piter = Clients("Piter")
Dmitry = Clients("Dmitry")
Dron = Clients("Dron")

order1 = Orders("sweets", 100, 2)
order2 = Orders("whiskey", 700, 2)
order3 = Orders("diamonds", 56000000, 2)
order4 = Orders("car", 350000, 3)
order5 = Orders("plane", 3700000, 1)
order6 = Orders("house", 25000, 3)
order7 = Orders("bysicle", 150, 1)
order8 = Orders("fruits", 15, 4)
order9 = Orders("ice-cream", 10, 1)
order10 = Orders("drinks", 50, 1)

session.add_all(
    [
        Igor,
        Piter,
        Dmitry,
        Dron,
        order1,
        order2,
        order3,
        order4,
        order5,
        order6,
        order7,
        order8,
        order9,
        order10,
    ]
)
session.commit()


clients = session.query(Clients).all()
for client in clients:
    print(f"client{client.id}) {client.name}:")
    for order in client.orders:
        print(f"№{order.client_id} {(order.name)}{order.cost}")
session.close()