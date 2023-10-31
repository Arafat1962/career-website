import mysql.connector


def connection_test():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'arafat5426',
            database = 'arafat_career'
        )

        if connection.is_connected():
            return connection
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    

def fetch_record():
    connection = connection_test()    
    cursor = connection.cursor(dictionary=True)

    cursor.execute('select * from jobs')
    records = cursor.fetchall()

    result_dicts = records
            # for record in records:
            #     result_dicts.append(dict(record))
    cursor.close()
    connection.close()
    return result_dicts


def load_job_from_db(id):
    connection = connection_test()

    cursor = connection.cursor(dictionary=True)
    query = ('select * from jobs where id=%s')


    # cursor.execute(query, (int(id)),)
    cursor.execute(query, (int(id),))

    record = cursor.fetchone()

    cursor.close()
    connection.close()

    return record if record else None

def add_application_to_db(job_id, application):
    connection = connection_test()
    cursor = connection.cursor()

    create_table_query = """
    create table if not exists applicants(
    id int auto_increment primary key not null,
    job_id int not null,
    full_name varchar(255) not null,
    email varchar(255) not null,
    linkedin varchar(255) not null,
    experience varchar(2000),
    education varchar(2000) not null
    )
    """

    cursor.execute(create_table_query)

    insert_query = """
    insert into applicants (job_id, full_name, email, linkedin, experience, education) values (%s,%s,%s,%s,%s,%s)
    """

    data = (job_id, application.get('full_name'), application.get('email'), application.get('linkedin'), application.get('experience'), application.get('education'))

    cursor.execute(insert_query, data)

    connection.commit()
    cursor.close()
    connection.close()




            