
import queue

class CallCenter:
    def __init__(self):
        self.call_queue = queue.Queue()
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def handle_call(self, call):
        if not self.agents:
            self.call_queue.put(call)
            print("All agents are busy. Call is placed in the queue.")
        else:
            agent = self.agents.pop(0)
            agent.handle_call(call)

    def add_agent_back(self, agent):
        self.agents.append(agent)

class Agent:
    def __init__(self, name):
        self.name = name

    def handle_call(self, call):
      print('{}'.format(call))
      print(f"{self.name} is handling call: {call}")

class Call:
    def __init__(self, caller_name):
        self.caller_name = caller_name
        
    def __str__(self):
        return self.caller_name

# Create a call center
call_center = CallCenter()

# Create agents
agent1 = Agent("Agent 1")
agent2 = Agent("Agent 2")

# Add agents to the call center
call_center.add_agent(agent1)
call_center.add_agent(agent2)

# Create calls and route them
call1 = Call("Caller 1")
call2 = Call("Caller 2")
call3 = Call("Caller 3")

call_center.handle_call(call1)
call_center.handle_call(call2)
call_center.handle_call(call3)

# Add an agent back
call_center.add_agent_back(agent1)

# Handle the queued call
queued_call = call_center.call_queue.get()
agent1.handle_call(queued_call)

# import queue
# class call_center:
#   def __init__(self):
#     self.call_queue = queue.Queue()
#     self.agents =[]
    
#   def add_Agent(self, agent):
#     self.agents.append(agent)
#   def handle_call(self, call):
#     if not self.call_queue:
#       print('all agents are busy call added to queue')
#       self.call_queue.put(call)
#     else:
#       agent = self.agents.pop()
#       agent.handle_call(agent)
      
#   def agent_back(self,agent):
#     self.agents.append(agent)
    
# class Agent:
#   def __init__(self, name):
#     self.name =name
#   def handle_call(self,caller):
#     print(f"{self.name} handling call from {caller}")
    
# class Call:
#   def __init__(self, caller_name):
#     self.caller_name = caller_name
    
# c_c = call_center()
# ag = Agent('sumit')
# call = Call('akshay')

# c_c.add_Agent(ag)
# c_c.handle_call(call)
# queued_call = c_c.call_queue.get()
# ag.handle_call(queued_call)