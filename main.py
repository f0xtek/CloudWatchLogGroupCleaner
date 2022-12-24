from cwlogs import create_logs_client, delete_log_groups

if __name__ == '__main__':
    delete_log_groups(create_logs_client())
