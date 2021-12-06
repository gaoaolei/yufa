from kube import KubernetesClass
from settings import *

if __name__ == '__main__':
    kube = KubernetesClass(KUBE_PATH)
    job_path = os.path.join(BASE_PATH, 'job','cron-update-adv-config-cache-test.yaml')
    kube.create_job(job_path, 'micro')

    # # job的使用
    # from kubernetes.client import V1JobStatus
    #
    # print(isinstance(job.status, V1JobStatus))
    # print(job.status)
    #
    # # 列出job
    # from kubernetes.client import V1JobList, V1Job
    #
    # job_list = batch.list_namespaced_job(namespace='default')
    # assert isinstance(job_list, V1JobList)
    # assert isinstance(job_list.items, list)
    # for job in job_list:
    #     assert isinstance(job, V1Job)
    #
    # # 读取job
    # job = batch.read_namespaced_job(name='hello', namespace='default')
    # assert isinstance(job, V1Job)
    #
    # # 列出一个job的pod
    # from typing import List
    # from kubernetes.client import CoreV1Api, V1Pod
    #
    #
    # def get_pods_by(job_name: str) -> List[V1Pod]:
    #     core = CoreV1Api()
    #     pods = core.list_namespaced_pod(namespace='default', label_selector=f'job_name={job_name}', limit=1)
    #     return pods.items