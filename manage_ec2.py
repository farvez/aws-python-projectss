import boto3
import time

class EC2Manager :
    def __init__(self):
        self.ec2 = boto3.client('ec2', region_name = 'us-west-2')
    
    def stop_instance(self, instance_id):
        
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            self.ec2.get_waiter('instance_stopped').wait(InstanceIds=[instance_id])

            print(f"{instance_id} is stopped")
        except Exception as e:
            print (f"error stopping instance: {e}")

    def start_instace(self, instance_id):

        try:
            self.ec2.start_instances(InstanceIds = [instance_id])
            self.ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])
            print(f"{instance_id} is running ")
        
        except Exception as e:
            print(f"error in starting the instance : {e}")

        
    def terminate_instance(self, instance_id):

        try:
            self.ec2.terminate_instances(InstanceIds = [instance_id])
            self.ec2.get_waiter('instance_terminated').wait(InstanceIds =[instance_id])
            print(f"{instance_id} is terminated")
        except Exception as e:
            print(f"Termination is failed because of {e}")


if __name__ == "__main__":
    ec2_manager = EC2Manager()
    instance_id = 'i-0075abcfed15da19f'
    ec2_manager.stop_instance(instance_id)
    time.sleep(20)
    ec2_manager.start_instace(instance_id)
    time.sleep(20)
    ec2_manager.terminate_instance(instance_id)

