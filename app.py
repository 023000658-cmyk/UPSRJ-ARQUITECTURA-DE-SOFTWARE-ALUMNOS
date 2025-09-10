from flask import Flask, jsonify
from repository.user_repository import UserRepository 
from service.user_service import UserService
from controller.routes import app

if __name__ == "__main__":
    # Entry point: runs the Flask development server in debug mode.
    app.run(debug=True)