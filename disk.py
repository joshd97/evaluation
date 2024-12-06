class Disk:
    def __init__(self, total, used):
        self.total = total 
        self.used = used    

    @property
    def free(self):
        return self.total - self.used

    @property
    def used_perc(self):
        return self.used / self.total

    def __str__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        return self.used_perc < other.used_perc

if __name__ == "__main__":
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)
    
    print(disk1) 
    print(disk2)  
    
    print(disk1.free)  
    print(disk2.free)  
    
    print(disk1.used_perc)  
    print(disk2.used_perc) 
    
    disks = [disk1, disk2]
    disks_sorted = sorted(disks) 
    for disk in disks_sorted:
        print(disk) 