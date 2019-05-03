import _sqlite3

db = _sqlite3.connect("Info.db")


def create_table():
    db.row_factory = _sqlite3.Row
    db.execute("Create Table if not exists Student(id int, name text)")
    db.commit()


def add_data(name, id):
    db.row_factory = _sqlite3.Row
    db.execute("Insert into Student(id,name) values (?,?)", (id, name))
    db.commit()
    print("Added successfully")


def get_data():
    cursor = db.execute("Select * From Student")
    for i in cursor:
        print("ID:" + str(i["id"]) + "\tName:" + i["name"])


def main():
    create_table()
    add_data("Shudipto", int(1))
    add_data("Trafder", int(2))
    # print data
    get_data()


if __name__ == '__main__':
    main()
