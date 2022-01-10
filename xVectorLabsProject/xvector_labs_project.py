from mysql.connector.errors import ProgrammingError, InterfaceError
from mysql.connector import connection
from socket import gaierror
from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
from logger_file import logger
import json
import sys


app = Flask(__name__)


@app.route('/dataset', methods=['GET'])
def get_records():
    try:
        conn = connection.MySQLConnection(user='saigopi',
                                          password='sai3121@',
                                          host='localhost',
                                          database='employees_new')
        cursor = conn.cursor()
        cursor.execute('SELECT * from employee')
        res = list(cursor)

    except (ProgrammingError, InterfaceError, gaierror):
        logger.error(sys.exc_info())

    except Exception as ex:
        logger.error(type(ex))

    else:
        cursor.close()
        conn.close()

        return jsonify({'message': 'successful',
                        'data': res})


@app.route('/dataset', methods=['POST'])
def write_record():
    try:
        conn = connection.MySQLConnection(user='saigopi',
                                          password='sai3121@',
                                          host='localhost',
                                          database='employees_new')

        rec = json.loads(request.data)
        rec1 = tuple([rec[i] for i in rec])
        cursor = conn.cursor()

        cursor.execute('insert into employee (eid, salary, age) values ' + str(rec1))

    except (ProgrammingError, InterfaceError, gaierror):
        logger.error(sys.exc_info())

    except Exception as ex:
        logger.error(type(ex))

    else:
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'successfully added'})


@app.route('/dataset/<col_name>/<operation>', methods=['POST'])
def filtered_value(col_name, operation):
    try:
        conn = connection.MySQLConnection(user='saigopi',
                                          password='sai3121@',
                                          host='localhost',
                                          database='employees_new')

        cursor = conn.cursor()
        cursor.execute('SELECT ' + operation + '(' + col_name + ')' + ' from employee')
        res = list(cursor)
    except (ProgrammingError, InterfaceError, gaierror):
        logger.error(sys.exc_info())

    except Exception as ex:
        logger.error(type(ex))

    else:

        cursor.close()
        conn.close()

        return jsonify({'data': res,
                        'message': 'successful'})


@app.route('/dataset/<col_1>/<col_2>', methods=['GET'])
def _plotting(col_1, col_2):
    try:
        conn = connection.MySQLConnection(user='saigopi',
                                          password='sai3121@',
                                          host='localhost',
                                          database='employees_new')
        cursor = conn.cursor()
        query1 = 'SELECT ' + col_1 + ' from employee limit 20'
        query2 = 'SELECT ' + col_2 + ' from employee limit 20'

        cursor.execute(query1)
        x_axis = list(cursor)

        cursor.execute(query2)
        y_axis = list(cursor)

        plt.plot(x_axis, y_axis)
        plt.show()

    except (ProgrammingError, InterfaceError, gaierror, UserWarning):
        logger.error(sys.exc_info())

    except Exception as ex:
        logger.error(type(ex))

    else:

        cursor.close()
        conn.close()

        return jsonify({'message': 'output directed to other thread/process'})


if __name__ == "__main__":
    app.run(debug=True)
