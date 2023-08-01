# Zomato Chronicles - Restaurant Menu Management
Welcome to Zomato Chronicles! This is a restaurant menu management web application built with Python and Flask. The project allows users to view the restaurant's menu, add new dishes, update dish availability, and delete dishes from the menu.

## Features
- **Menu Display:** The application displays the restaurant's menu, showing dish IDs, names, prices, and availability status.
- **Add New Dish:** Users can add new dishes to the menu by providing the dish name, price, and availability status.
- **Update Availability:** The application enables users to update the availability status of existing dishes.
- **Delete Dish:** Users can delete dishes from the menu that are no longer served.
- **MySQL Database:** The menu and order data are stored in a MySQL database, ensuring data persistence and scalability.

## Technologies Used
- Python
- Flask: A lightweight web framework for Python that enables rapid development of web applications.
- Flask-MySQL: An extension that simplifies MySQL database integration with Flask applications.

## How to Use
1. Clone the repository to your local machine.
2. Set up a virtual environment and install the required dependencies.
3. Configure the MySQL connection settings in the Flask application.
4. Run the Flask application with python app.py.
5. Access the application through your browser at http://localhost:5000/.

## Project Structure
The project follows a simple structure:

- **app.py:** The main Flask application file containing route definitions and database configuration.
- **static/:** Contains static files such as CSS and images for styling the templates.
- **templates/:** Contains HTML templates for rendering web pages.

## Contribution
Contributions to Zomato Chronicles are welcome! If you have any ideas for enhancements or bug fixes, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## About
Zomato Chronicles was created as a sample project to showcase web development with Flask and MySQL. It is not intended for production use but can serve as a foundation for building more sophisticated restaurant management systems.

Thank you for checking out Zomato Chronicles! We hope you find it helpful and inspiring for your web development journey. Happy coding!
