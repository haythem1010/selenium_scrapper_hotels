from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687" , auth=('neo4j', "123456789"))

driver.verify_authentication()