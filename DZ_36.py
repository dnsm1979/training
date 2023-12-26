import threading
import time
import requests
from star_wars_starship import StarWarsDataBase
import logging

logger = logging.getLogger('main_db')
logging.basicConfig(level='INFO')

lock = threading.Lock()

def insert_human_to_db(human):
    logger.info(f'Insert {human["name"]} to db...')
    try:
        lock.acquire(True)
        db.insert_human_tu_table(human)
        logger.info(f'Insert {human["name"]} to db... SUCCESS')
    finally:
        lock.release()
        # logger.info(f'Insert {human["name"]} to db... ERROR')

def get_human(human_ig):
    response = requests.get(f'https://swapi.dev/api/people/{human_ig}/')
    insert_human_to_db(response.json())

def consequents_loading():
    start = time.time()
    for i in range(1, 10):
        try:
            logger.info(f'Getting {i} human...')
            get_human(i)
            logger.info(f'Getting {i} numan... SUCCESS')
        except BaseException:
            logger.info(f'Getting {i} human... ERROR')
    logger.info(f'Consequent loading takes {time.time() - start} sec')


def parallel_loading():
    start = time.time()
    tasks = []
    for i in range(1, 10):
        task = threading.Thread(target=get_human, args=(i, ))
        task.name = f'Getting {i} human...'
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