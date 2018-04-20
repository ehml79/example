# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test?charset=utf8')
# 创建对象的基类:
Base = declarative_base()
# 创建DBSession类型:
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(127))
    password = Column(String(127))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

if __name__ == '__main__':

    # 创建session对象:

    # 创建数据库
    Base.metadata.create_all(engine)
    # 删除数据库
    # Base.metadata.drop_all(engine)

    # 创建session对象:
    session = Session()

    # 添加记录
    # user = User()
    # user.name = "user1"
    # user.password = "password"
    # session.add(user)

    # 查询记录
    # user = session.query(User).filter_by(name="user1").first()
    # print('{} {}'.format(user.name,user.password))

    # 更新记录
    # user = session.query(User).filter_by(name="user1").first()
    # user.password = "newpassword"

    # 删除记录
    user = session.query(User).filter_by(name="user1").first()
    session.delete(user)
    session.commit()

    # 提交并关闭session:
    session.commit()
    session.close()





