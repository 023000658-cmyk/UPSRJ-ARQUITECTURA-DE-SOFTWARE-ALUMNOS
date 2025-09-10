import json 

class UserRepository:
    """
    Repository component that handles user data access.

    Implements the Repository design pattern to abstract data retrieval.
    """

    def get_users(self):
        """
        Returns a static list of user dictionaries.

        In a real application, this would query a database.
        """
        try:
            with open('repository/users.json', 'r') as file:
                file_data = file.read()
                return json.loads(file_data)
        except FileNotFoundError:
            return []