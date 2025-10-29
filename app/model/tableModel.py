from ..DB.database import Base
from sqlalchemy import Column ,Integer , String ,Boolean,text,TIMESTAMP,ForeignKey
from sqlalchemy.orm import Mapped , mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    # id = Column(Integer,primary_key= True, nullable = False)
    # title = Column(String,nullable = False)
    # content = Column(String , nullable  = False)
    # published = Column(Boolean , server_default='TRUE' , nullable=False)
    # created_at = Column(TIMESTAMP(timezone=True) , nullable=False , server_default=text('now()'))
    # user_id = Column(Integer, nullable=False , foreign_key="users.id")
    id : Mapped[int] = mapped_column(primary_key= True, nullable = False)
    title : Mapped[str] = mapped_column(String,nullable = False)    
    content : Mapped[str] = mapped_column(String , nullable  = False)
    published : Mapped[bool] = mapped_column(Boolean , server_default='TRUE' , nullable=False)
    created_at : Mapped[str] = mapped_column(TIMESTAMP(timezone=True) , nullable=False , server_default=text('now()'))
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    user = relationship("User")

class User(Base):
    __tablename__ = "users"
    # email = Column(String,nullable=False,unique=True)
    # password = Column(String,nullable=False)
    # id = Column(Integer,primary_key = True,nullable=False)
    # created_at = Column(TIMESTAMP(timezone = True) , nullable = False, server_default=text('now()'))
    email: Mapped[str] = mapped_column(String , nullable= False , unique= True)
    password: Mapped[str] = mapped_column(String , nullable= False)
    id: Mapped[int] = mapped_column(primary_key=True , nullable= False , unique= True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True) , nullable= False , server_default=text('now()') )
    