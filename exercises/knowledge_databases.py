from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,name,rating):
	article_object = Knowledge(
		topic=topic,
		name=name,
		rating=rating)
	session.add(article_object)
	session.commit()

add_article("astronomy","black holes",10)
add_article("weather","rainbow",9)

def query_all_articles():
	article=session.query(Knowledge).all()
	return article
# print(query_all_articles())


def query_article_by_topic(topic_name):
	article=session.query(Knowledge).filter_by(topic=topic_name).first()
	return article
# print(query_article_by_topic("astronomy" ))


def delete_article_by_topic(topic_name):
	article=session.query(Knowledge).filter_by(topic=topic_name).delete()
	session.commit()


# print(query_all_articles())

def delete_article_by_rating(threshold):
	article_object=session.query(Knowledge).filter(rating>threshold).delete()
	session.commit()



def delete_all_articles():
	article=session.query(Knowledge).delete()
	session.commit()
	
# delete_all_articles()


def	edit_article_rating(topic,updated_rating):
	article_object=session.query(Knowledge).filter_by(topic=topic).first()
	article_object.rating=updated_rating
	session.commit()
  
edit_article_rating("weather",10)
print(query_all_articles())
delete_article_by_rating(10)