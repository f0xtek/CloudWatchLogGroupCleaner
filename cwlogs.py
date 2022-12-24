from typing import Optional

import boto3
from mypy_boto3_logs.client import CloudWatchLogsClient
from mypy_boto3_logs.paginator import DescribeLogGroupsPaginator
from mypy_boto3_logs.type_defs import LogGroupTypeDef


class LogGroup:
    def __init__(self, name: str, arn: str, retention_days=None) -> None:
        self.name: str = name
        self.arn: str = arn
        self.retention_days: int = retention_days

    def __repr__(self) -> str:
        if self.retention_days is None:
            self.retention_days = -1
        return (f'LogGroup(name={self.name}, short_name={self.short_name}, arn={self.arn}, '
                f'prefix={self.prefix}, retentionInDays={self.retention_days})')

    @property
    def prefix(self) -> str:
        return '/'.join(self.name.split('/')[:-1])

    @property
    def short_name(self) -> str:
        return ''.join(self.name.split('/')[-1])

    def __prompt_for_deletion(self) -> bool:
        while True:
            delete: str = input(f'Delete log group {self.name}? (y/N) ')
            if delete.lower() not in ['y', 'n', '']:
                continue
            if delete.lower() in ['y', 'yes']:
                return True
            return False

    def delete(self) -> None:
        if self.__prompt_for_deletion():
            # TODO: implement
            print(f"Deleted log group {self.name}")
        else:
            # TODO: implement
            print(f"Did not delete log group {self.name}")


def create_logs_client() -> CloudWatchLogsClient:
    return boto3.client('logs')


def delete_log_groups(client: CloudWatchLogsClient):
    log_groups: list[LogGroupTypeDef] = __describe_cloudwatch_log_groups(client)
    for log_group_object in __create_log_groups(log_groups):
        log_group_object.delete()


def __create_log_groups(log_groups_response: list[LogGroupTypeDef]) -> list[LogGroup]:
    log_group_objects: list[LogGroup] = []
    for log_group in log_groups_response:
        lg_name: str = log_group['logGroupName']
        lg_arn: str = log_group['arn']
        lg_retention: Optional[int] = log_group.get('retentionInDays', None)
        log_group_objects.append(
            LogGroup(lg_name, lg_arn, lg_retention)
        )
    __print_log_groups(log_group_objects)
    return log_group_objects


def __print_log_groups(log_groups: list[LogGroup]):
    print("Found log groups:")
    for log_group in log_groups:
        print(log_group)


def __describe_cloudwatch_log_groups(client: CloudWatchLogsClient) -> list[LogGroupTypeDef]:
    log_group_paginator: DescribeLogGroupsPaginator = client.get_paginator('describe_log_groups')
    groups: list[LogGroupTypeDef] = []
    for log_group_page in log_group_paginator.paginate():
        groups += log_group_page['logGroups']
    return groups
