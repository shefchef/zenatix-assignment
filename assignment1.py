pip3 install psutil

import psutil
import platform
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

#CPU information

# number of cores
Physical_cores = psutil.cpu_count(logical=False)
Total_cores = psutil.cpu_count(logical=True)
# CPU frequencies
cpufreq = psutil.cpu_freq()
Max_Frequency = {cpufreq.max:.2f}Mhz
Min_Frequency = {cpufreq.min:.2f}Mhz
Current_Frequency = {cpufreq.current:.2f}Mhz
# CPU usage
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    Core {i} =  {percentage}%"
Total_CPU_Usage = {psutil.cpu_percent()}%

# Memory Information

# memory details
svmem = psutil.virtual_memory()
Total = {get_size(svmem.total)}
Available = {get_size(svmem.available)}
Used = {get_size(svmem.used)}
Percentage = {svmem.percent}%

# swap memory details (if exists)
swap = psutil.swap_memory()
Total = {get_size(swap.total)}
Free = {get_size(swap.free)}
Used = {get_size(swap.used)}
Percentage = {swap.percent}%

es.indices.delete(index='CPU')
{'acknowledged': True}
es.index(
 index='CPU',
 body={
  Total_CPU_Usage = {psutil.cpu_percent()}%
 })

es.index(
 index='memory',
 body={
  memory_Percentage = {svmem.percent}%
 })


es.indices.refresh(index='CPU')
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
