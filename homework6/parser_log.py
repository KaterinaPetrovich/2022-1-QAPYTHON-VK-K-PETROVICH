from collections import Counter

import os


def get_path_to_log(log_file):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), log_file))


def count_requests(log_file):
    log_path = get_path_to_log(log_file)
    counter = 0
    with open(log_path) as file:
        for _ in file:
            counter += 1
    return counter


def count_types(log_file):
    log_path = get_path_to_log(log_file)
    types = []
    with open(log_path) as file:
        for line in file:
            types.append(line.split()[5])
    cnt = Counter(types)
    return cnt


def count_most_common_requests(count, log_file):
    log_path = get_path_to_log(log_file)
    urls = []
    with open(log_path) as file:
        for line in file:
            urls.append(line.split()[6])
    cnt = Counter(urls)

    return dict(cnt.most_common(count))


def count_users_with_server_error(count, log_file):
    log_path = get_path_to_log(log_file)
    users = []
    with open(log_path) as file:
        for line in file:
            if line.split()[8].startswith("5"):
                users.append(line.split()[0])
    cnt = Counter(users)
    return dict(cnt.most_common(count))


def count_longest_requests_with_error(log_file):
    log_path = get_path_to_log(log_file)
    data = []
    with open(log_path) as file:
        for line in file:
            if line.split()[8].startswith("4"):
                data.append(
                    [line.split()[6], line.split()[8], line.split()[9], line.split()[0]])
    data.sort(key=lambda x: int(x[2]), reverse=True)
    return data[:5]


def write_to_file(result_file):
    with open(result_file, "w", encoding="utf-8") as result:
        result.write(f"Общее количество запросов:{count_requests('access.log')}\n")

        result.write("Общее количество запросов по типу:\n")
        types_counter = count_types('access.log')
        for key in types_counter:
            result.write(f"{key}: {types_counter[key]}\n")

        result.write("Топ 10 самых частых запросов:\n")
        urls = count_most_common_requests(10, 'access.log')
        for key in urls:
            result.write(f"{key}: {urls[key]}\n")

        result.write("Топ 5 пользователей с ошибкой сервера:\n")
        users = count_users_with_server_error(5, 'access.log')
        for key in users:
            result.write(f"{key}: {users[key]}\n")

        result.write("Топ самых больших запросов с ошибкой:\n")
        requests = count_longest_requests_with_error('access.log')
        for req in requests:
            result.write(f"url: {req[0]} status: {req[1]} size: {req[2]} ip:{req[3]}\n")
