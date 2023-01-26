import time
status = {"first castle health":20,"first castle soldiers":[],"second castle health":20,"second castle soldiers":[]}
seke = {'first':0,'second':0}
hab = ['first','second']
hab2 = ['3','10']
takhrib={'10':9,'3':2}
function = {}
def get_status():
    print(status)

def teach(team_id, soldier_id):
    if(team_id in hab and soldier_id in hab2):
        
        # سكه ايي كه بازيكن دارد بايد بيشتر از قيمت سرباز باشد
        
        if(int(soldier_id)<seke[team_id]):
            status[team_id+' '+"castle soldiers"].append((takhrib[soldier_id],0))
            seke[team_id]-=int(soldier_id)
            return True
        else:
            return False
    else:
        return False

def add_event(callback, event_id):
        function[event_id]=callback

while True:
    seke['first']+=1
    seke['second']+=1
    time.sleep(1)
    








