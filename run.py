from app import app
from app import INI
from app import BASE_DIR


if __name__ == '__main__':
    app.run(debug=INI[0], host=INI[1], port=INI[2])
