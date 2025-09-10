from flask import Flask, jsonify
from repository.user_repository import UserRepository
from service.user_service import UserService

app = Flask(__name__)

user_repository = UserRepository()

user_service = UserService(user_repository)

@app.route("/users")
def get_users():
    """HTTP endpoint that returns a JSON list of users."""
    users = user_service.list_users()
    return jsonify(users)
