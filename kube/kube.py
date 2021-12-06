from kubernetes.client import BatchV1Api
from kubernetes import config
from kubernetes.watch import Watch
import yaml
import json


class KubernetesClass(object):
    def __init__(self, path):
        """初始化kubernetes"""
        config.load_kube_config(path)
        self.batch = BatchV1Api()

    def create_job(self, job_path, namespace):
        '''创建job'''
        try:
            with open(job_path) as f:
                cfg = yaml.safe_load(f)
            self.batch.create_namespaced_job(namespace=namespace, body=cfg)
            return True
        except Exception as e:
            if e.status in [409, 422]:
                print(e)
                print(e.body)
                print(json.loads(e.body)['message'])
            else:
                print('创建job报错')
                print(e)
                return False

    def check_exist(self, job_name, namespace):
        '''检查job是否存在'''
        try:
            self.batch.read_namespaced_job(name=job_name, namespace=namespace)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_job(self, job_name, namespace):
        '''删除job'''
        try:
            self.batch.delete_namespaced_job(job_name, namespace)
            return True
        except Exception as e:
            print(e)
            return False

    def watch_job(self, job_name, namespace):
        """
        监控job是否完成 bool
        """
        watcher = Watch()
        try:
            for event in watcher.stream(self.batch.list_namespaced_job, namespace=namespace,
                                        label_selector=f'job-name={job_name}'):
                succeed = event['object'].status.succeeded
                active = event['object'].status.active
                if succeed == 1 and active == None:
                    watcher.stop()
                    return True
        except Exception as e:
            print(e)
            return False
