import mysql.connector
from  datetime import datetime
class dbconnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="MuHamdammed@77",
                database="gym_membership"
            )
            return self.connection
        except Exception as e:
            return None
class gym_membership(dbconnect):
    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from gym3 where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def get(self):
     try:
         self.connect = super().get_connection()  # for connect it from inheitance
         self.cursor = self.connect.cursor()
         query = "select * from gym3"
         self.cursor.execute(query)
         record = self.cursor.fetchall()
         for i in record:
             print(i)
     except Exception as e:
         print(e)
    def post(self,**kwargs):
        self.connect=super().get_connection()
        self.cursor=self.connect.cursor()
        query="insert into gym3 (name,place,mobile,plan,fee,joined_date) values(%s,%s,%s,%s,%s,%s)"
        values=[v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connect.commit()
        print("new member added successfully")
    def retrieve(self,id=None):
     try:
        self.connect=super().get_connection()
        self.cursor=self.connect.cursor()
        query="select * from gym3 where id =%s"
        values=(id,)
        self.cursor.execute(query,values)
        result=self.cursor.fetchone()
        print(result)

     except Exception as e:
         print(e)


    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from gym3 where id=%s"
                self.cursor.execute(query, values)
                self.connect.commit()
                print("member success full deleted")
            else:
                print("member is not found")
        except Exception as e:
            print(e)


    def put(self, id=None, **kwargs):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query = "select * from gym3 where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result != None:
            placeholder = ""
            for k in kwargs.keys():
                placeholder += k + "=%s,"
            placeholder = placeholder.rstrip(", ")
            query = f"update gym3 set {placeholder} where id=%s"
            values = [v for v in kwargs.values()]
            values.append(id)
            self.cursor.execute(query, values)
            self.connect.commit()
            print("member details updated successfully..")
        else:
            print("member is not found")

# connection_instance=dbconnect()
# print(connection_instance.get_connection())
member_instance=gym_membership()
#member_instance.get()
#member_instance.post(name="amal",place="kochi",mobile="665566670707",plan="2 month",fee=34556,joined_date=datetime.today())
#member_instance.post(name="arjun",place="kollam",mobile="906666670707",plan="6 month",fee=5000,joined_date=datetime.today())
#member_instance.get()
member_instance.delete(id=1)
member_instance.get()
#member_instance.retrieve(id=1)

























