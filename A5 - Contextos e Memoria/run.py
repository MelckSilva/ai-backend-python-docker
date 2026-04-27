from groq import Groq
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from dotenv import load_dotenv
import uuid

load_dotenv()

client = Groq()

engine = create_engine("sqlite:///chat.db")
Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    session_id = Column(String)
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def save_message(user_id, session_id, role, content):
    msg = Message(
        user_id=user_id,
        session_id=session_id,
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()


def load_memory(user_id, session_id, limit=10):
    messages = (
        db.query(Message)
        .filter_by(user_id=user_id, session_id=session_id)
        .order_by(Message.id.desc())
        .limit(limit)
        .all()
    )
    
    messages.reverse()
    
    return [
        {"role": m.role, "content": m.content}
        for m in messages
    ]

def chat():
    print("Chat com SQLAlchemy + session_id")
    user_id = input("Digite seu user_id: ")
    session_id = str(uuid.uuid4())
    print(f"Sessão iniciada: {session_id}")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        
        if user_input.lower() == "/new":
            session_id = str(uuid.uuid4())
            print(f"Nova sessão criada: {session_id}")
            continue
        
        save_message(user_id, session_id, "user", user_input)
        memory = load_memory(user_id, session_id)
        
        messages = [
            {"role": "system", "content": "Você é um assistente útil"}
        ] + memory
        
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages
        )
        
        answer = response.choices[0].message.content
        save_message(user_id, session_id, "assistant", answer)
        print("Bot:", answer)
        print("-" * 50)


if __name__ == "__main__":
    chat()