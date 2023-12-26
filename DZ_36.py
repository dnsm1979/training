import threading
import time
import requests
from SW_db import StarWarsDataBase
import logging

logger = logging.getLogger('SW_db_log')
logging.basicConfig(level='INFO')

semaphore = threading.Semaphore(1)

def insert_starship_to_db(starship):
    logger.info(f'Insert {starship["name"]} to db...')
    try:
        semaphore.acquire(True)
        db.insert_starship_tu_table(starship)
        logger.info(f'Insert {starship["name"]} to db... SUCCESS')
    finally:
        semaphore.release()

def get_starship(id):
    response = requests.get(f'https://swapi.dev/api/starships/{id}/')
    insert_starship_to_db(response.json())

def consequents_loading():
    start = time.time()
    for i in range(1, 10):
        try:
            logger.info(f'Getting {i} starship...')
            get_starship(i)
            logger.info(f'Getting {i} starship... SUCCESS')
        except BaseException:
            logger.info(f'Getting {i} starship... ERROR')
    logger.info(f'Consequent loading takes {time.time() - start} sec')


def parallel_loading():
    start = time.time()
    tasks = []
    for i in range(1, 10):
        task = threading.Thread(target=get_starship, args=(i, ))
        task.name = f'Getting {i} starship...'
        logger.info(task.name)
        task.start()
        tasks.append((task))
    for i_task in tasks:
        i_task.join()
        logger.info(i_task.name + 'SUCCESS')
    logger.info(f'Parallel loading takes {time.time() - start} sec')

if __name__ == '__main__':
    db = StarWarsDataBase()
    try:
    #    consequents_loading()
        parallel_loading()

    finally:
        db.close_connection()