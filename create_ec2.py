import boto3

class EC2Manager:
    def __init__(self):
        self.ec2 = boto3.client('ec2', region_name = 'us-west-2')
    
    def create_instance(self, instance_type='t2.micro'):
        response =self.ec2.run_instances(
            ImageId = 'ami-05f991c49d264708f',
            InstanceType = instance_type,
            MinCount = 1,
            MaxCount = 1,
            KeyName = 'boto'
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"created EC2 instance : {instance_id}")
        return instance_id
    
    def wait_for_instance(self, instance_id):
        self.ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is running")
    
if __name__ == "__main__":
    ec2_manager =EC2Manager()
    instance_id = ec2_manager.create_instance()
    ec2_manager.wait_for_instance(instance_id)
    
