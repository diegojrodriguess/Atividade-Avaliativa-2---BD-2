from query import Database
class TeacherCRUD:
    def __init__(self):
        self.db = Database("bolt://184.73.19.50:7687", "neo4j", "searches-religions-crops")

    def create(self, name, ano_nasc, cpf):
        query = f"""
        CREATE(:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})
        """
        self.db.run(query)

    def read(self, name):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        RETURN t
        """
        result = self.db.run(query)
        return result

    def delete(self, name):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        DELETE t
        """
        self.db.run(query)

    def update(self, name, new_cpf):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        SET t.cpf = '{new_cpf}'
        """
        self.db.run(query)
