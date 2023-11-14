from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        self._driver = None

        try:
            self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def run(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return result.data()
        
db = Database("bolt://184.73.19.50:7687", "neo4j", "searches-religions-crops")

# Questão 01
query1 = """
MATCH (t:Teacher{name:'Renzo'})
RETURN t.ano_nasc, t.cpf
"""

query2 = """
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name, t.cpf
"""

query3 = """
MATCH (c:City)
RETURN c.name
"""

query4 = """
MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name, s.address, s.number
"""

# Questão 02
query5 = """
MATCH (t:Teacher)
WITH COLLECT(t.ano_nasc) AS birth_years
RETURN MIN(birth_years[0]) AS min_birth_year, MAX(birth_years[1]) AS max_birth_year
"""

query6 = """
MATCH (c:City)
RETURN AVG(c.population) AS average_population
"""

query7 = """
MATCH (c:City{cep:'37540-000'})
RETURN REPLACE(c.name, 'a', 'A') AS modified_name
"""

query8 = """
MATCH (t:Teacher)
RETURN SUBSTRING(t.name, 3, 1) AS third_letter
"""

result_query1 = db.run(query1)
print("Query 1 Result:", result_query1)

result_query2 = db.run(query2)
print("Query 2 Result:", result_query2)

result_query3 = db.run(query3)
print("Query 3 Result:", result_query3)

result_query4 = db.run(query4)
print("Query 4 Result:", result_query4)

result_query5 = db.run(query5)
print("Query 5 Result:", result_query5)

result_query6 = db.run(query6)
print("Query 6 Result:", result_query6)

result_query7 = db.run(query7)
print("Query 7 Result:", result_query7)

result_query8 = db.run(query8)
print("Query 8 Result:", result_query8)
